#!/usr/bin/python
# Classification (U)

"""Program:  mongo_rep_admin.py

    Description:  Administration program for Mongo replica set.  The program
        has a number of functions to monitor the status of replication between
        primary and secondary databases.  The program can monitor and check on
        a number of different aspects in replication to include checking master
        status, membership status, replication time lag between primary and
        secondaries, and replication configuration status.

    Usage:
        mongo_rep_admin.py -c file -d path
            {-L [-j [-f]] [-z] [-o dir_path/file [-a]] [-i [db:coll] -m file]
                [-e toEmail {toEmail2, [...]} [-s subject]] |
             -N [ [-f] [-e toEmail {toEmail2, [...]} [-s subject]] [-z] |
             -M | -P | -S | -T }
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.

        -L => Check Replication lag.
            -j => Set output to JSON format.
            -f => Flatten the JSON data structure to file and standard out.
            -i [database:collection] => Name of database and collection.
                Delimited by colon (:).  Default: sysmon:mongo_rep_lag
            -m file => Mongo config file used for the insertion into a Mongo
                database.  Do not include the .py extension.
            -o path/file => Directory path and file name for output.
                Default is to overwrite the file.
            -a => Append output to output file.
            -e to_email_addresses => Sends output to one or more email
                addresses.  Email addresses are space delimited.
            -s subject_line => Subject line of email.
            -z => Suppress standard out.

        -M => Show current members in replication set.

        -N => Node health check.  Returns if a node has a problem or is down.
            -e to_email_addresses => Sends output to one or more email
                addresses.  Email addresses are space delimited.
            -s subject_line => Subject line of email.

        -P => Show priority for members in replication set.

        -S => Check status of rep for members in rep set, but will only print
            the status if errors are detected.

        -T => Check status of rep for members in rep set and will print the
            status in all checks.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format is for connecting to a Mongo database or
            replica set for monitoring.  A second configuration file can also
            be used to connect to a Mongo database or replica set to insert the
            results of the performance monitoring into.

            There are two ways to connect methods:  single Mongo database or a
            Mongo replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = 27017
            conf_file = None
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"
            use_arg = True
            use_uri = False

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:

            repset = None
            repset_hosts = None
            db_auth = None

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_rep_admin.py -c mongo -d config -L -j

"""

# Libraries and Global Variables

# Standard
import sys
import datetime

# Third party
import json

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.cmds_gen as cmds_gen
import lib.gen_class as gen_class
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def rep_health_chk(rep_stat, prt_all=False, prt_lvl=1, **kwargs):

    """Function:  rep_health_chk

    Description:  Checks the replication health status for a member.

    Arguments:
        (input) rep_stat -> Member document from replSetGetStatus.
        (input) prt_all -> True|False - To print all or just errors.
        (input) prt_lvl -> Integer - Level at which to print message.

    """
    rep_stat = dict(rep_stat)

    if not rep_stat.get("health"):
        gen_libs.prt_msg("Health", "Bad", prt_lvl)

    elif prt_all:
        gen_libs.prt_msg("Health", "Good", prt_lvl)


def rep_state_chk(rep_stat, prt_all=False, prt_lvl=1, **kwargs):

    """Function:  rep_state_chk

    Description:  Checks the state for a member.  Requires the member document
        from a "replSetGetStatus" command to be passed to the function.

    Arguments:
        (input) rep_stat -> Member document from replSetGetStatus.
        (input) prt_all -> True|False - To print all or just errors.
        (input) prt_lvl -> Integer - Level at which to print message.

    """

    # Good state is 1 (Primary), 2 (Secondary), 7 (Abriter).
    good_state = [1, 2, 7]
    rep_stat = dict(rep_stat)

    if rep_stat.get("state") not in good_state or prt_all:
        gen_libs.prt_msg("State", rep_stat.get("state"), prt_lvl)
        gen_libs.prt_msg("State Msg", rep_stat.get("stateStr"), prt_lvl + 1)


def rep_msg_chk(rep_stat, prt_lvl=1, **kwargs):

    """Function:  rep_msg_chk

    Description:  Print data if the infoMessage field is present.

    Arguments:
        (input) rep_stat -> Member document from replSetGetStatus.
        (input) prt_lvl -> Integer - Level at which to print message.

    """

    rep_stat = dict(rep_stat)

    if rep_stat.get("infoMessage"):
        gen_libs.prt_msg("Error Message", rep_stat.get("infoMessage"), prt_lvl)


def chk_rep_stat(repset, args_array, **kwargs):

    """Function:  chk_rep_stat

    Description:  Fetch the replication status and process each member in the
        set.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            prt_all -> True|False on printing all status messages.

    """

    args_array = dict(args_array)
    print("\nReplication Status Check for Rep Set:  %s" % (repset.repset))
    prt_all = kwargs.get("prt_all", False)

    # Process each member in replica set.
    for item in repset.adm_cmd("replSetGetStatus").get("members"):
        print("\nServer: %s" % (item.get("name")))
        rep_health_chk(item, prt_all)
        rep_state_chk(item, prt_all)
        rep_msg_chk(item)


def prt_rep_stat(repset, args_array, **kwargs):

    """Function:  prt_rep_stat

    Description:  Set the print all flag and call chk_rep_stat function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    args_array = dict(args_array)
    chk_rep_stat(repset, args_array, prt_all=args_array["-T"])


def fetch_priority(repset, args_array, **kwargs):

    """Function:  fetch_priority

    Description:  Fetch and print members in the replication set.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    args_array = dict(args_array)
    print("\nMembers => priority of replica set: %s" % (repset.repset))
    coll = mongo_class.Coll(
        repset.name, repset.user, repset.japd, host=repset.host,
        port=repset.port, db="local", coll="system.replset", auth=repset.auth,
        conf_file=repset.conf_file, auth_db=repset.auth_db,
        use_arg=repset.use_arg, use_uri=repset.use_uri,
        auth_mech=repset.auth_mech)
    status = coll.connect()

    if status[0]:

        for item in coll.coll_find1()["members"]:
            print("\t{0} => {1}".format(item["host"], item["priority"]))

        mongo_libs.disconnect([coll])

    else:
        print("fetch_priority:  Connection failure:  %s" % (status[1]))


def fetch_members(repset, args_array, **kwargs):

    """Function:  fetch_members

    Description:  Fetch and print members in the replication set and identify
        the primary server.

    Arguments:
        (ininput) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    args_array = dict(args_array)
    print("\nMembers of replica set: %s" % (repset.repset))
    rep_status = repset.adm_cmd("replSetGetStatus")
    primary = get_master(rep_status)
    print("\t%s (Primary)" % (primary["name"]))

    secondaries = [member for member in rep_status.get("members")
                   if member.get("state") == 2]

    for second in secondaries:
        print("\t%s" % (second["name"]))


def get_master(rep_status, **kwargs):

    """Function:  get_master

    Description:  Find the Primary in the replSetGetStatus document.

    Arguments:
        (input) rep_status -> Members document from replSetGetStatus.
        (output) primary -> Primary entry from replSetGetStatus doc.

    """

    rep_status = dict(rep_status)
    primary = None

    # Process each member in replica set.
    for member in rep_status.get("members"):
        if member.get("state") == 1:
            primary = member
            break

    return primary


def get_optimedate(rep_status, **kwargs):

    """Function:  get_optimedate

    Description:  Get the Best oplog date time from one of the Secondaries.

    Arguments:
        (input) rep_status -> Members document from replSetGetStatus.
        (output) optime_date -> Best oplog datetime from Secondaries.

    """

    rep_status = dict(rep_status)
    optime_date = datetime.datetime.strptime("1900-01-01 00:00:01",
                                             "%Y-%m-%d %H:%M:%S")

    # Find best datetime from Secondary servers.
    for member in rep_status.get("members"):
        if member.get("optimeDate") > optime_date:
            optime_date = member.get("optimeDate")

    return optime_date


def chk_mem_rep_lag(rep_status, **kwargs):

    """Function:  chk_mem_rep_lag

    Description:  Process each member in the replication set and check for
               replication lag.

    Arguments:
        (input) rep_status -> Member document from replSetGetStatus.
        (input) **kwargs:
            json -> True|False - JSON format.
            ofile -> file name - Name of output file.
            db_tbl -> database:collection - Name of db and collection.
            class_cfg -> Server class configuration settings.
            mail -> Mail instance.
            args_array -> Array of command line options and values.
            suf -> Primary|Freshest Secondary who has latest date time.
            optdt -> Primary|Best Oplog date time.

    """

    t_format = "%Y-%m-%d %H:%M:%S"
    rep_status = dict(rep_status)
    json_fmt = kwargs.get("json", False)

    outdata = {"Application": "Mongo Replication",
               "RepSet": rep_status.get("set"),
               "Master": get_master(rep_status).get("name"),
               "AsOf": datetime.datetime.strftime(datetime.datetime.now(),
                                                  t_format),
               "Slaves": []}

    # Process each member in replica set.
    for member in rep_status.get("members"):

        # Ignore if member is Primary or Abriter.
        if member.get("state") in [1, 7]:
            continue

        # Fetch rep lag time.
        if member.get("optime"):
            sec_ago = gen_libs.get_secs(
                kwargs["optdt"] - member.get("optimeDate"))
            outdata["Slaves"].append(
                {"Name": member.get("name"),
                 "SyncTo": datetime.datetime.strftime(
                     member.get("optimeDate"), t_format),
                 "LagTime": sec_ago})

        else:
            gen_libs.prt_msg("Warning", "No replication info available.", 0)

    if json_fmt:
        _process_json(outdata, **kwargs)

    else:
        _process_std(outdata, **kwargs)


def _process_std(outdata, **kwargs):

    """Function:  _process_std

    Description:  Private function for chk_mem_rep_lag().  Process standard out
        formatted data.

    Arguments:
        (input) outdata -> JSON document from chk_mem_rep_lag function.
        (input) **kwargs:
            suf -> Primary|Freshest Secondary who has latest date time.
            args_array -> Array of command line options and values.
        (output) status -> Tuple on connection status.
            status[0] - True|False - Connection successful.
            status[1] - Error message if connection failed.

    """

    status = (True, None)
    mode = "w"
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)
    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)
    args_array = dict(kwargs.get("args_array", {}))
    body = []

    if args_array.get("-a", False):
        mode = "a"

    body.append("\nReplication lag for Replica set: %s." % (outdata["RepSet"]))

    for item in outdata["Slaves"]:
        body.append("\nSource: {0}".format(item["Name"]))
        body.append("\tsynced to:  {0}".format(item["SyncTo"]))
        body.append("\t{0} secs ({1} hrs) behind the {2}".format(
            item["LagTime"], (item["LagTime"] / 36) / 100, kwargs["suf"]))

    if mongo_cfg and db_tbl:
        dbs, tbl = db_tbl.split(":")
        status = mongo_libs.ins_doc(mongo_cfg, dbs, tbl, outdata)

    if ofile:
        f_hldr = gen_libs.openfile(ofile, mode)

        for line in body:
            gen_libs.write_file2(f_hldr, line)

    if mail:
        for line in body:
            mail.add_2_msg(line)

        mail.send_mail()

    if not args_array.get("-z", False):
        for item in body:
            print(item)

    return status


def _process_json(outdata, **kwargs):

    """Function:  _process_json

    Description:  Private function for chk_mem_rep_lag().  Process JSON data.

    Arguments:
        (input) outdata -> JSON document from chk_mem_rep_lag function.
        (input) **kwargs:
            ofile -> file name - Name of output file.
            db_tbl -> database:collection - Name of db and collection.
            class_cfg -> Server class configuration settings.
            mail -> Mail instance.
            args_array -> Array of command line options and values.
        (output) status -> Tuple on connection status.
            status[0] - True|False - Connection successful.
            status[1] - Error message if connection failed.

    """

    status = (True, None)
    mode = "w"
    indent = 4
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)
    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)
    args_array = dict(kwargs.get("args_array", {}))

    if args_array.get("-a", False):
        mode = "a"

    if args_array.get("-f", False):
        indent = None

    jdata = json.dumps(outdata, indent=indent)

    if mongo_cfg and db_tbl:
        dbs, tbl = db_tbl.split(":")
        status = mongo_libs.ins_doc(mongo_cfg, dbs, tbl, outdata)

    if ofile:
        gen_libs.write_file(ofile, mode, jdata)

    if mail:
        mail.add_2_msg(jdata)
        mail.send_mail()

    if not args_array.get("-z", False):
        gen_libs.display_data(jdata)

    return status


def chk_rep_lag(repset, args_array, **kwargs):

    """Function:  chk_rep_lag

    Description:  See if replication is running and find the best Oplog
        datetime whether Primary or Secondary.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    args_array = dict(args_array)
    json_fmt = args_array.get("-j", False)
    outfile = args_array.get("-o", None)
    db_tbl = args_array.get("-i", None)
    rep_status = repset.adm_cmd("replSetGetStatus")
    primary = get_master(rep_status)
    mongo_cfg = None

    if args_array.get("-m", None):
        mongo_cfg = gen_libs.load_module(args_array["-m"], args_array["-d"])

    if primary:
        optime_date = primary.get("optimeDate")
        suffix = "primary"

    # Use best datetime from Secondaries.
    else:
        optime_date = get_optimedate(rep_status)
        suffix = "freshest secondary"

    chk_mem_rep_lag(
        rep_status, optdt=optime_date, suf=suffix, json=json_fmt,
        ofile=outfile, db_tbl=db_tbl, class_cfg=mongo_cfg,
        args_array=args_array, **kwargs)


def node_chk(mongo, args_array, **kwargs):

    """Function:  node_chk

    Description:  Check the status of all Mongo nodes.  Will only output
        something if a node is down or an error is detected.

    Arguments:
        (input) mongo -> Mongo instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            mail -> Mail instance.

    """

    # Good state is 1 (Primary), 2 (Secondary), 7 (Abriter).
    good_state = [1, 2, 7]
    indent = 4
    args_array = dict(args_array)
    mail = kwargs.get("mail", None)
    node_status = {}

    if args_array.get("-f", False):
        indent = None

    # Check each node.
    for node in mongo.adm_cmd("replSetGetStatus").get("members"):
        status = {}

        if not node.get("health"):
            status["Health"] = "Bad"

        if node.get("state") not in good_state:
            status["State"] = node.get("state")
            status["State_Message"] = node.get("stateStr")

        if node.get("infoMessage"):
            status["Error_Message"] = node.get("infoMessage")

        if status:
            node_name = "Node: %s" % node.get("name")
            node_status[node_name] = status

    if node_status:
        jnode_status = json.dumps(node_status, indent=indent)

        if not args_array.get("-z", False):
            gen_libs.display_data(jnode_status)

        if mail:
            if not mail.subj:
                subj = "Node Status Check for Rep Set:  %s" % mongo.repset
                mail.create_subject(subj=subj)

            mail.add_2_msg(jnode_status)
            mail.send_mail()


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    mail = None
    server = gen_libs.load_module(args_array["-c"], args_array["-d"])

    # Only pass authorization mechanism if present.
    auth_mech = {"auth_mech": server.auth_mech} if hasattr(
        server, "auth_mech") else {}

    coll = mongo_class.Coll(
        server.name, server.user, server.japd, host=server.host,
        port=server.port, db="local", coll="system.replset", auth=server.auth,
        conf_file=server.conf_file, auth_db=server.auth_db,
        use_arg=server.use_arg, use_uri=server.use_uri, **auth_mech)
    status = coll.connect()

    if status[0]:

        # Is replication setup.
        if coll.coll_cnt() != 0:

            # Get replica set name if not in config.
            if server.repset:
                rep_set = server.repset

            else:
                rep_set = coll.coll_find1().get("_id")

            repinst = mongo_class.RepSet(
                server.name, server.user, server.japd, host=server.host,
                port=server.port, auth=server.auth, repset=rep_set,
                repset_hosts=server.repset_hosts, auth_db=server.auth_db,
                use_arg=server.use_arg, use_uri=server.use_uri, **auth_mech)
            status2 = repinst.connect()

            if status2[0]:

                if args_array.get("-e", None):
                    mail = gen_class.setup_mail(
                        args_array.get("-e"), subj=args_array.get("-s", None))

                # Call function: Intersection of command line & function dict.
                for item in set(args_array.keys()) & set(func_dict.keys()):
                    func_dict[item](repinst, args_array, mail=mail, **kwargs)

                mongo_libs.disconnect([repinst])

            else:
                print("run_program.RepSet: Connection failure:  %s"
                      % (status2[1]))

        else:
            gen_libs.prt_msg("Error", "No replication found.", 0)

        mongo_libs.disconnect([coll])

    else:
        print("run_program.Coll: Connection failure:  %s" % (status[1]))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_con_req_list -> contains the options that require other options.
        opt_def_dict -> contains options with their default values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-L": chk_rep_lag, "-M": fetch_members, "-S": chk_rep_stat,
                 "-P": fetch_priority, "-T": prt_rep_stat, "-N": node_chk}
    opt_con_req_list = {"-i": ["-m"], "-s": ["-e"]}
    opt_def_dict = {"-j": False, "-i": "sysmon:mongo_rep_lag"}
    opt_multi_list = ["-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-i", "-m", "-o", "-e", "-s"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       opt_def_dict, multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list):
        run_program(args_array, func_dict)


if __name__ == "__main__":
    sys.exit(main())
