#!/usr/bin/python
# Classification (U)

"""Program:  mongo_rep_admin.py

    Description:  Administration program for Mongo Replication system.  Has a
        number of functions to monitor the status of the replication between
        primary and secondary databases.  The program can monitor and check on
        a number of different aspects in replication to include checking master
        status, membership status, replication time lag between primary and
        secondaries, and replication configuration status.

    Usage:
        mongo_rep_admin.py -c file -d path {-L | -M | -P  | -S | -T | -j |
            -o dir_path/file | -i db:coll | -m file} [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -L => Check Replication lag.
        -M => Show current members in replication set.
        -P => Show priority for members in replication set.
        -S => Check status of rep for members in rep set, print errors.
        -T => Check status of rep for members in rep set and print all.
        -j => Set output to JSON format.
        -i database:collection => Name of database and collection.
            Delimited by colon (:).  Default: sysmon:mongo_rep_lag
        -m file => Mongo config file used for the insertion into a Mongo
            database.  Do not include the .py extension.  Used only with the
            -i option.
        -o path/file => Directory path and file name for output.
        -e to_email_addresses => Enables emailing capability for an option if
            the option allows it.  Sends output to one or more email addresses.
        -s subject_line => Subject line of email.  Optional, will create own
            subject line if one is not provided.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -o and -j options is only available for -L option.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_rep_admin.py -c mongo -d config -L

    Workaround:   To disable printing to standard out, use the -o option to
        print to a file.  This is most often useful if wanting to insert into
        a database, but not receive anything on standard out.

"""

# Libraries and Global Variables

# Standard
import sys
import datetime
import getpass
import socket

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
    for x in repset.adm_cmd("replSetGetStatus").get("members"):
        print("\nServer: %s" % (x.get("name")))
        rep_health_chk(x, prt_all)
        rep_state_chk(x, prt_all)
        rep_msg_chk(x)


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
    COLL = mongo_class.Coll(repset.name, repset.user, repset.passwd,
                            repset.host, repset.port, "local",
                            "system.replset", repset.auth, repset.conf_file)
    COLL.connect()

    for x in COLL.coll_find1()["members"]:
        print("\t{0} => {1}".format(x["host"], x["priority"]))

    cmds_gen.disconnect([COLL])


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

    if (repset.is_primary()):
        x = repset.fetch_adr()
        print("\t" + ":".join([x[0], str(x[1])]) + "  (Primary)")

    # Process secondary servers.
    for x in repset.fetch_nodes().difference(set([repset.fetch_adr()])):
        print("\t" + ":".join([x[0], str(x[1])]))


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


def fetch_rep_lag(dtg, **kwargs):

    """Function:  fetch_rep_lag

    Description:  Computes the difference between the Primary|best oplog
        datetime and Secondary oplog datetime.

    Arguments:
        (input) dtg -> Oplog date time for Secondary.
        (input) **kwargs:
            optdt -> Primary|Best Oplog date time.
            suf -> Primary|Freshest Secondary who has latest date time.
            json -> True|False - JSON format.
            ofile -> file name - Name of output file.
        (output) sec_ago -> Replication lag in seconds.

    """

    # Total seconds and hours behind.
    sec_ago = gen_libs.get_secs(kwargs["optdt"] - dtg)
    hrs_ago = (sec_ago / 36) / 100
    json_fmt = kwargs.get("json", False)

    if json_fmt:
        return sec_ago

    else:
        gen_libs.prt_msg("synced to", str(dtg), 1)
        print("\t{0} secs ({1} hrs) behind the {2}".format(sec_ago, hrs_ago,
                                                           kwargs["suf"]))


def chk_mem_rep_lag(rep_status, **kwargs):

    """Function:  chk_mem_rep_lag

    Description:  Process each member in the replication set and check for
               replication lag.

    Arguments:
        (input) rep_status -> Member document from replSetGetStatus.
        (input) **kwargs:
            optdt -> Primary Oplog date time of latest transaction.
            suf -> Primary|Freshest Secondary who has latest optdt.
            json -> True|False - JSON format.
            ofile -> file name - Name of output file.
            db_tbl -> database:collection - Name of db and collection.
            class_inst -> Server class instance or equivalent class.
            mail -> Mail instance.

    """

    rep_status = dict(rep_status)
    json_fmt = kwargs.get("json", False)

    if json_fmt:
        outdata = {"application": "Mongo Replication",
                   "repSet": rep_status.get("set"),
                   "master": get_master(rep_status).get("name"),
                   "asOf": datetime.datetime.strftime(datetime.datetime.now(),
                                                      "%Y-%m-%d %H:%M:%S"),
                   "slaves": []}

    else:
        print("\nReplication lag for Replica set: %s."
              % (rep_status.get("set")))

    # Process each member in replica set.
    for member in rep_status.get("members"):

        # Ignore if member is Primary or Abriter.
        if member.get("state") in [1, 7]:
            continue

        if not json_fmt:
            print("\nSource: {0}".format(member.get("name")))

        # Fetch rep lag time.
        if member.get("optime"):
            if json_fmt:
                sec_ago = fetch_rep_lag(member.get("optimeDate"), **kwargs)

                outdata["slaves"].append({"name": member.get("name"),
                                          "syncTo":
                                          datetime.datetime.strftime(
                                              member.get("optimeDate"),
                                              "%Y-%m-%d %H:%M:%S"),
                                          "lagTime": sec_ago})

            else:
                fetch_rep_lag(member.get("optimeDate"), **kwargs)

        else:
            gen_libs.prt_msg("Warning", "No replication info available.", 0)

    if json_fmt:
        jdata = json.dumps(outdata, indent=4)
        mail = kwargs.get("mail", None)

        mongo_libs.json_prt_ins_2_db(outdata,
                                     class_cfg=kwargs.get("class_inst", None),
                                     **kwargs)

        if mail:
            mail.add_2_msg(jdata)
            mail.send_mail()


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

    chk_mem_rep_lag(rep_status, optdt=optime_date, suf=suffix,
                    json=json_fmt, ofile=outfile, db_tbl=db_tbl,
                    class_inst=mongo_cfg, **kwargs)


def setup_mail(to_line, subj=None, frm_line=None, **kwargs):

    """Function:  setup_mail

    Description:  Initialize a mail instance.  Provide 'from line' if one is
        not passed.

    Arguments:
        (input) to_line -> Mail to line.
        (input) subj -> Mail subject line.
        (input) frm_line -> Mail from line.
        (output) Mail instance.

    """

    to_line = list(to_line)

    if isinstance(subj, list):
        subj = list(subj)

    if not frm_line:
        frm_line = getpass.getuser() + "@" + socket.gethostname()

    return gen_class.Mail(to_line, subj, frm_line)


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
    coll = mongo_class.Coll(server.name, server.user, server.passwd,
                            server.host, server.port, "local",
                            "system.replset", server.auth, server.conf_file)
    coll.connect()

    # Is replication setup.
    if coll.coll_cnt() != 0:
        # Fetch the replication set name.
        rep_set = coll.coll_find1().get("_id")
        repinst = mongo_class.RepSet(server.name, server.user, server.passwd,
                                     server.host, server.port, server.auth,
                                     repset=rep_set)
        repinst.connect()

        if args_array.get("-e", None):
            mail = setup_mail(args_array.get("-e"),
                              subj=args_array.get("-s", None))


        # Call function(s) - intersection of command line and function dict.
        for x in set(args_array.keys()) & set(func_dict.keys()):
            func_dict[x](repinst, args_array, mail=mail, **kwargs)

        cmds_gen.disconnect([repinst])

    else:
        gen_libs.prt_msg("Error", "No replication found.", 0)

    cmds_gen.disconnect([coll])


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

    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-L": chk_rep_lag, "-M": fetch_members, "-S": chk_rep_stat,
                 "-P": fetch_priority, "-T": prt_rep_stat}
    opt_con_req_list = {"-i": ["-m"], "-s": ["-e"]}
    opt_def_dict = {"-j": False, "-i": "sysmon:mongo_rep_lag"}
    opt_multi_list = ["-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-i", "-m", "-o", "-e", "-s"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list, opt_def_dict,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                           file_crt_list):
        run_program(args_array, func_dict)


if __name__ == "__main__":
    sys.exit(main())
