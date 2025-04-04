#!/bin/sh
# Classification (U)

# Shell commands follow
# Next line is bilingual: it starts a comment in Python & is a no-op in shell
""":"

# Find a suitable python interpreter (can adapt for specific needs)
# NOTE: Ignore this section if passing the -h option to the program.
#   This code must be included in the program's initial docstring.
for cmd in python3.12 python3.9 ; do
   command -v > /dev/null $cmd && exec $cmd $0 "$@"
done

echo "OMG Python not found, exiting...."

exit 2

# Previous line is bilingual: it ends a comment in Python & is a no-op in shell
# Shell commands end here

   Program:  mongo_rep_admin.py

    Description:  Administration program for Mongo replica set.  The program
        has a number of functions to monitor the status of replication between
        primary and secondary databases.  The program can monitor and check on
        a number of different aspects in replication to include checking master
        status, membership status, replication time lag between primary and
        secondaries, and replication configuration status.

    Usage:
        mongo_rep_admin.py -c file -d path
            {-L [-m config_file -i [db_name:table_name]]
                [-o dir_path/file [-a a|w]] [-z] [-r [-k N]]
                [-e to_email [to_email2 ...] [-s subject_line] [-u]]} |
############################################################################
# Replaced with mongo-db-admin -M option
#            {-L [-j [-f]] [-z] [-o dir_path/file [-a]] [-i [db:coll] -m file]
#                [-e toEmail {toEmail2, [...]} [-s subject] [-u]] |
             -N [ [-f] [-e toEmail {toEmail2, [...]} [-s subject] [-u]] [-z] |
############################################################################
             -M | -P | -S | -T }
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.

        -L => Check Replication lag.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mongo_rep_lag
            -o path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are space
                    delimited.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -r => Expand the JSON format using Pretty Print.
                -k N => Indentation for expanded JSON format.
############################################################################
# Replaced with mongo-db-admin -M option
#R            -j => Set output to JSON format.
#R            -f => Flatten the JSON data structure to file and standard out.
#            -i [database:collection] => Name of database and collection.
#                Delimited by colon (:).  Default: sysmon:mongo_rep_lag
#            -m file => Mongo config file used for the insertion into a Mongo
#                database.  Do not include the .py extension.
#            -o path/file => Directory path and file name for output.
#                Default is to overwrite the file.
#                -a => Append output to output file.
#            -e to_email_addresses => Sends output to one or more email
#                addresses.  Email addresses are space delimited.
#            -s subject_line => Subject line of email.
#            -u => Override the default mail command and use mailx.
#            -z => Suppress standard out.
############################################################################

        -M => Show current members in replication set.

        -N => Node health check.  Returns if a node has a problem or is down.
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
                -i {database:collection} => Name of database and collection.
                    Default: sysmon:mongo_rep_lag
            -o path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file. Default is
                    write.
            -e to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are space
                    delimited.
                -s subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -z => Suppress standard out.
            -r => Expand the JSON format using Pretty Print.
                -k N => Indentation for expanded JSON format.
            -n => Only report if errors detected.
############################################################################
# Replaced with mongo-db-admin -M option
#R            -f => Flatten the JSON data structure to file and standard out.
#            -e to_email_addresses => Sends output to one or more email
#                addresses.  Email addresses are space delimited.
#            -s subject_line => Subject line of email.
#            -u => Override the default mail command and use mailx.
#            -z => Suppress standard out.
############################################################################

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

            Single database connection:

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

            Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.  By
                default all these entries are set to None to represent not
                connecting to a replica set.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            If Mongo is set to use TLS or SSL connections, then one or more of
                the following entries will need to be completed to connect
                using TLS or SSL protocols.
                Note:  Read the configuration file to determine which entries
                    will need to be set.

                SSL:
                    auth_type = None
                    ssl_client_ca = None
                    ssl_client_key = None
                    ssl_client_cert = None
                    ssl_client_phrase = None
                TLS:
                    auth_type = None
                    tls_ca_certs = None
                    tls_certkey = None
                    tls_certkey_phrase = None

            Note:  FIPS Environment for Mongo.
              If operating in a FIPS 104-2 environment, this package will
              require at least a minimum of pymongo==3.8.0 or better.  It will
              also require a manual change to the auth.py module in the pymongo
              package.  See below for changes to auth.py.

            - Locate the auth.py file python installed packages on the system
                in the pymongo package directory.
            - Edit the file and locate the "_password_digest" function.
            - In the "_password_digest" function there is an line that should
                match: "md5hash = hashlib.md5()".  Change it to
                "md5hash = hashlib.md5(usedforsecurity=False)".
            - Lastly, it will require the Mongo configuration file entry
                auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_rep_admin.py -c mongo -d config -L -j

":"""
# Python program follows


# Libraries and Global Variables

# Standard
import sys
import datetime

try:
    import simplejson as json
except ImportError:
    import json

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mongo_lib import mongo_libs
    from .mongo_lib import mongo_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import mongo_lib.mongo_libs as mongo_libs           # pylint:disable=R0402
    import mongo_lib.mongo_class as mongo_class         # pylint:disable=R0402
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def create_header(name, dtg):

    """Function:  create_header

    Description:  Create standard JSON header for reports.

    Arguments:
        (input) name -> Name of check
        (input) dtg -> TimeFormat instance
        (output) header -> Dictionary header for reports

    """

    header = {
        "Application": "Mongo_Rep_Admin",
        "Check": name,
        "AsOf": dtg.get_time("zulu")}

    return header


def rep_health_chk(rep_stat, prt_all=False, prt_lvl=1):

    """Function:  rep_health_chk

    Description:  Checks the replication health status for a member.

    Arguments:
        (input) rep_stat -> Member document from replSetGetStatus
        (input) prt_all -> True|False - To print all or just errors
        (input) prt_lvl -> Integer - Level at which to print message

    """

    rep_stat = dict(rep_stat)

    if not rep_stat.get("health"):
        gen_libs.prt_msg("Health", "Bad", prt_lvl)

    elif prt_all:
        gen_libs.prt_msg("Health", "Good", prt_lvl)


def rep_state_chk(rep_stat, prt_all=False, prt_lvl=1):

    """Function:  rep_state_chk

    Description:  Checks the state for a member.  Requires the member document
        from a "replSetGetStatus" command to be passed to the function.

    Arguments:
        (input) rep_stat -> Member document from replSetGetStatus
        (input) prt_all -> True|False - To print all or just errors
        (input) prt_lvl -> Integer - Level at which to print message

    """

    # Good state is 1 (Primary), 2 (Secondary), 7 (Abriter).
    good_state = [1, 2, 7]
    rep_stat = dict(rep_stat)

    if rep_stat.get("state") not in good_state or prt_all:
        gen_libs.prt_msg("State", rep_stat.get("state"), prt_lvl)
        gen_libs.prt_msg("State Msg", rep_stat.get("stateStr"), prt_lvl + 1)


def rep_msg_chk(rep_stat, prt_lvl=1):

    """Function:  rep_msg_chk

    Description:  Print data if the infoMessage field is present.

    Arguments:
        (input) rep_stat -> Member document from replSetGetStatus
        (input) prt_lvl -> Integer - Level at which to print message

    """

    rep_stat = dict(rep_stat)

    if rep_stat.get("infoMessage"):
        gen_libs.prt_msg("Error Message", rep_stat.get("infoMessage"), prt_lvl)


def chk_rep_stat(repset, args, **kwargs):

    """Function:  chk_rep_stat

    Description:  Fetch the replication status and process each member in the
        set.

    Arguments:
        (input) repset -> Replication set instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            mail -> Mail instance
            prt_all -> True|False on printing all status messages
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    status = (True, None)
    print(f"\nReplication Status Check for Rep Set:  {repset.repset}")
    prt_all = kwargs.get("prt_all", False)

    # Process each member in replica set.
    for item in repset.adm_cmd("replSetGetStatus").get("members"):
        print(f'\nServer: {item.get("name")}')
        rep_health_chk(item, prt_all)
        rep_state_chk(item, prt_all)
        rep_msg_chk(item)

    return status


def prt_rep_stat(repset, args, **kwargs):               # pylint:disable=W0613

    """Function:  prt_rep_stat

    Description:  Set the print all flag and call chk_rep_stat function.

    Arguments:
        (input) repset -> Replication set instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            mail -> Mail instance
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    status = (True, None)
    chk_rep_stat(repset, args, prt_all=args.get_val("-T"))

    return status


def fetch_priority(repset, args, **kwargs):             # pylint:disable=W0613

    """Function:  fetch_priority

    Description:  Fetch and print members in the replication set.

    Arguments:
        (input) repset -> Replication set instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            mail -> Mail instance
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    coll = mongo_class.Coll(
        repset.name, repset.user, repset.japd, host=repset.host,
        port=repset.port, db="local", coll="system.replset", auth=repset.auth,
        conf_file=repset.conf_file, auth_db=repset.auth_db,
        auth_mech=repset.auth_mech, ssl_client_ca=repset.ssl_client_ca,
        ssl_client_cert=repset.ssl_client_cert,
        ssl_client_key=repset.ssl_client_key,
        ssl_client_phrase=repset.ssl_client_phrase, auth_type=repset.auth_type,
        tls_ca_certs=repset.tls_ca_certs, tls_certkey=repset.tls_certkey,
        tls_certkey_phrase=repset.tls_certkey_phrase)
    status = coll.connect()

    if status[0]:
        print(f"\nMembers => priority of replica set: {repset.repset}")

        for item in coll.coll_find1()["members"]:
            print(f'\t{item["host"]} => {item["priority"]}')

        mongo_libs.disconnect([coll])

    else:
        status = (
            status[0], f"fetch_priority:  Connection failure:  {status[1]}")

    return status


def fetch_members(repset, args, **kwargs):              # pylint:disable=W0613

    """Function:  fetch_members

    Description:  Fetch and print members in the replication set and identify
        the primary server.

    Arguments:
        (input) repset -> Replication set instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            mail -> Mail instance
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    status = (True, None)
    print(f"\nMembers of replica set: {repset.repset}")
    rep_status = repset.adm_cmd("replSetGetStatus")
    primary = get_master(rep_status)
    print(f'\t{primary["name"]} (Primary)')

    secondaries = [member for member in rep_status.get("members")
                   if member.get("state") == 2]

    for second in secondaries:
        print(f'\t{second["name"]}')

    return status


def get_master(rep_status):

    """Function:  get_master

    Description:  Find the Primary in the replSetGetStatus document.

    Arguments:
        (input) rep_status -> Members document from replSetGetStatus
        (output) primary -> Primary entry from replSetGetStatus doc

    """

    rep_status = dict(rep_status)
    primary = None

    # Process each member in replica set.
    for member in rep_status.get("members"):
        if member.get("state") == 1:
            primary = member
            break

    return primary


def get_optimedate(rep_status):

    """Function:  get_optimedate

    Description:  Get the Best oplog date time from one of the Secondaries.

    Arguments:
        (input) rep_status -> Members document from replSetGetStatus
        (output) optime_date -> Best oplog datetime from Secondaries

    """

    rep_status = dict(rep_status)
    optime_date = datetime.datetime.strptime(
        "1900-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")

    # Find best datetime from Secondary servers.
    for member in rep_status.get("members"):
        optime_date = max(optime_date, member.get('optimeDate'))

    return optime_date


def chk_mem_rep_lag(rep_status, dtg, **kwargs):

    """Function:  chk_mem_rep_lag

    Description:  Process each member in the replication set and check for
        replication lag.

    Arguments:
        (input) rep_status -> Member document from replSetGetStatus
        (input) dtg -> DateFormat instance
        (input) **kwargs:
            to_addr -> To email address
            subj -> Email subject line
            mailx -> True|False - Use mailx command
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            use_pprint -> True|False - Expand the JSON format
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            db_tbl -> database:table - Database name:Table name
            mongo -> Mongo configuration settings
            no_report -> Only report if errors detected
            suf -> Primary|Freshest Secondary who has latest date time
            optdt -> Primary|Best Oplog date time
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

#    t_format = "%Y-%m-%d %H:%M:%S"
    rep_status = dict(rep_status)
#    json_fmt = kwargs.get("json", False)

    outdata = {
        "Application": "Mongo Replication", "RepSet": rep_status.get("set"),
        "Master": get_master(rep_status).get("name"),
        "AsOf": dtg.get_time("zulu"), "Slaves": []}

#        "AsOf": datetime.datetime.strftime(datetime.datetime.now(), t_format),

    # Process each member in replica set
    for member in rep_status.get("members"):

        # Ignore if member is Primary or Abriter
        if member.get("state") in [1, 7]:
            continue

        # Fetch rep lag time
        if member.get("optime"):
            sec_ago = gen_libs.get_secs(
                kwargs["optdt"] - member.get("optimeDate"))
            outdata["Slaves"].append(
                {"Name": member.get("name"),
                 "SyncTo": datetime.datetime.strftime(
                     member.get("optimeDate"), "%Y-%m-%d %H:%M:%S"),
                 "LagTime": sec_ago})

        else:
            gen_libs.prt_msg("Warning", "No replication info available.", 0)

    status = mongo_libs.data_out(outdata, **kwargs)
#    if json_fmt:
#        status = process_json(outdata, **kwargs)
#
#    else:
#        status = process_std(outdata, **kwargs)

    return status


#def process_std(outdata, **kwargs):

    """Function:  process_std

    Description:  Process standard out formatted data.

    Arguments:
        (input) outdata -> JSON document from chk_mem_rep_lag function
        (input) **kwargs:
            json -> True|False - JSON format
            ofile -> file name - Name of output file
            outfile -> Name of output file
            db_tbl -> database:collection - Name of db and collection
            class_cfg -> Server class configuration settings
            mail -> Mail instance
            args -> ArgParser class instance
            suf -> Primary|Freshest Secondary who has latest date time
            optdt -> Primary|Best Oplog date time
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    """
    status = (True, None)
    mode = "w"
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)
    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)
    args = kwargs.get("args", None)
    body = []

    if args.get_val("-a", def_val=False):
        mode = "a"

    body.append(f'\nReplication lag for Replica set: {outdata["RepSet"]}')

    for item in outdata["Slaves"]:
        body.append(f'\nSource: {item["Name"]}')
        body.append(f'\tsynced to:  {item["SyncTo"]}')
        body.append(f'\t{item["LagTime"]} secs'
                    f' ({int((item["LagTime"] / 36) / 100)} hrs) behind the'
                    f' {kwargs["suf"]}')

    if mongo_cfg and db_tbl:
        dbs, tbl = db_tbl.split(":")
        status = mongo_libs.ins_doc(mongo_cfg, dbs, tbl, outdata)

    if not status[0]:
        status = (status[0], "process_std: " + status[1])

    if ofile:
        f_hldr = gen_libs.openfile(ofile, mode)

        for line in body:
            gen_libs.write_file2(f_hldr, line)

    if mail:
        for line in body:
            mail.add_2_msg(line)

        mail.send_mail(use_mailx=args.get_val("-u", def_val=False))

    if not args.get_val("-z", def_val=False):
        for item in body:
            print(item)

    return status
    """


#def process_json(outdata, **kwargs):

    """Function:  process_json

    Description:  Process JSON data.

    Arguments:
        (input) outdata -> JSON document from chk_mem_rep_lag function
        (input) **kwargs:
            json -> True|False - JSON format
            ofile -> file name - Name of output file
            db_tbl -> database:collection - Name of db and collection
            class_cfg -> Server class configuration settings
            mail -> Mail instance
            args -> ArgParser class instance
            suf -> Primary|Freshest Secondary who has latest date time
            optdt -> Primary|Best Oplog date time
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    """
    status = (True, None)
    mode = "w"
    indent = 4
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)
    ofile = kwargs.get("ofile", None)
    mail = kwargs.get("mail", None)
    args = kwargs.get("args", None)

    if args.get_val("-a", def_val=False):
        mode = "a"

    if args.get_val("-f", def_val=False):
        indent = None

    jdata = json.dumps(outdata, indent=indent)

    if mongo_cfg and db_tbl:
        dbs, tbl = db_tbl.split(":")
        status = mongo_libs.ins_doc(mongo_cfg, dbs, tbl, outdata)

    if not status[0]:
        status = (status[0], "process_json: " + status[1])

    if ofile:
        gen_libs.write_file(ofile, mode, jdata)

    if mail:
        mail.add_2_msg(jdata)
        mail.send_mail(use_mailx=args.get_val("-u", def_val=False))

    if not args.get_val("-z", def_val=False):
        gen_libs.display_data(jdata)

    return status
    """


def chk_rep_lag(repset, dtg, **kwargs):

    """Function:  chk_rep_lag

    Description:  See if replication is running and find the best Oplog
        datetime whether Primary or Secondary.

    Arguments:
        (input) repset -> Replication set instance
        (input) dtg -> DateFormat instance
        (input) **kwargs:
            to_addr -> To email address
            subj -> Email subject line
            mailx -> True|False - Use mailx command
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            use_pprint -> True|False - Expand the JSON format
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            db_tbl -> database:table - Database name:Table name
            mongo -> Mongo configuration settings
            no_report -> Only report if errors detected
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

#    json_fmt = args.get_val("-j", def_val=False)
#    outfile = args.get_val("-o", def_val=None)
#    db_tbl = args.get_val("-i", def_val=None)

    rep_status = repset.adm_cmd("replSetGetStatus")
    primary = get_master(rep_status)

#    mongo_cfg = None
#
#    if args.get_val("-m", def_val=None):
#        mongo_cfg = gen_libs.load_module(
#            args.get_val("-m"), args.get_val("-d"))

    if primary:
        optime_date = primary.get("optimeDate")
        suffix = "primary"

    # Use best datetime from Secondaries.
    else:
        optime_date = get_optimedate(rep_status)
        suffix = "freshest secondary"

    status = chk_mem_rep_lag(
        rep_status, dtg, optdt=optime_date, suf=suffix, **kwargs)
#    status = chk_mem_rep_lag(
#        rep_status, optdt=optime_date, suf=suffix, json=json_fmt,
#        ofile=outfile, db_tbl=db_tbl, class_cfg=mongo_cfg, args=args, **kwargs)

    return status


def node_chk(mongo, dtg, **kwargs):

    """Function:  node_chk

    Description:  Check the status of all Mongo nodes.  Will only output
        something if a node is down or an error is detected.

    Arguments:
        (input) mongo -> Mongo instance
        (input) dtg -> DateFormat instance
        (input) **kwargs:
            to_addr -> To email address
            subj -> Email subject line
            mailx -> True|False - Use mailx command
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            use_pprint -> True|False - Expand the JSON format
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            db_tbl -> database:table - Database name:Table name
            mongo -> Mongo configuration settings
            no_report -> Only report if errors detected
        (output) status -> Tuple on connection status
            status[0] - True|False - Connection successful
            status[1] - Error message if connection failed

    """

    status = (True, None)
#    mail = kwargs.get("mail", None)
    node_status = {}

#    indent = None if args.get_val("-f", def_val=False) else 4

    for node in mongo.adm_cmd("replSetGetStatus").get("members"):
        tstatus = single_node_chk(node)

        if tstatus:
            node_status[node.get("name")] = tstatus

    if not kwargs.get("no_report", False) or (
            kwargs.get("no_report", False) and node_status):
        data = create_header("NodeCheck", dtg)
        data["node_status"] = node_status
        status = mongo_libs.data_out(data, **kwargs)

#    if node_status:
#        jnode_status = json.dumps(node_status, indent=indent)
#
#        if not args.get_val("-z", def_val=False):
#            gen_libs.display_data(jnode_status)
#
#        if mail:
#            if not mail.subj:
#                subj = f"Node Status Check for Rep Set:  {mongo.repset}"
#                mail.create_subject(subj=subj)
#
#            mail.add_2_msg(jnode_status)
#            mail.send_mail(use_mailx=args.get_val("-u", def_val=False))

    return status


def single_node_chk(node):

    """Function:  single_node_chk

    Description:  Check the status of a single node.  Will only output
        something if a node is down or an error is detected.

    Arguments:
        (input) node -> Dictionary of Mongo node health stats
        (output) status -> Dictionary of node stats found

    """

    # Good state is 1 (Primary), 2 (Secondary), 7 (Abriter).
    good_state = [1, 2, 7]
    node = dict(node)
    status = {}

    if not node.get("health"):
        status["Health"] = "Bad"

    if node.get("state") not in good_state:
        status["State"] = node.get("state")
        status["State_Message"] = node.get("stateStr")

    if node.get("infoMessage"):
        status["Error_Message"] = node.get("infoMessage")

    return status


def create_data_config(args):

    """Function:  create_data_config

    Description:  Create data out config parameters.

    Arguments:
        (input) args -> ArgParser class instance
        (output) data_config -> Dictionary for data out config parameters

    """

    data_config = {}
    data_config["to_addr"] = args.get_val("-e")
    data_config["subj"] = args.get_val("-s")
    data_config["mailx"] = args.get_val("-u", def_val=False)
    data_config["outfile"] = args.get_val("-o")
    data_config["mode"] = args.get_val("-a", def_val="w")
    data_config["use_pprint"] = args.get_val("-r", def_val=False)
    data_config["indent"] = args.get_val("-k")
    data_config["suppress"] = args.get_val("-z", def_val=False)
    data_config["db_tbl"] = args.get_val("-i")
    data_config["no_report"] = args.get_val("-n", def_val=False)

    if args.get_val("-m", def_val=False):
        data_config["mongo"] = gen_libs.load_module(
            args.get_val("-m"), args.get_val("-d"))

    return data_config


def call_func(args, func_dict, repinst):

    """Function:  call_func

    Description:  Call each function selected.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options
        (input) repset -> Replication set instance

    """

    func_dict = dict(func_dict)
    data_config = dict(create_data_config(args))
    dtg = gen_class.TimeFormat()
    dtg.create_time()

#######################################################################
# Move to individual functions
#    mail = None
#
#    if args.get_val("-e", def_val=None):
#        mail = gen_class.setup_mail(
#            args.get_val("-e"), subj=args.get_val("-s", def_val=None))
#######################################################################

    # Call function: Intersection of command line & function dict.
    for item in set(args.get_args_keys()) & set(func_dict.keys()):
        status = func_dict[item](repinst, dtg, **data_config)
#        status = func_dict[item](repinst, args, mail=mail)

        if not status[0]:
            print(f"Error detected:  {status[1]}")


def run_program(args, func_dict):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options

    """

    func_dict = dict(func_dict)
    server = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))

    coll = mongo_class.Coll(
        server.name, server.user, server.japd, host=server.host,
        port=server.port, db="local", coll="system.replset", auth=server.auth,
        conf_file=server.conf_file, auth_db=server.auth_db,
        auth_mech=server.auth_mech, ssl_client_ca=server.ssl_client_ca,
        ssl_client_cert=server.ssl_client_cert,
        ssl_client_key=server.ssl_client_key,
        ssl_client_phrase=server.ssl_client_phrase, auth_type=server.auth_type,
        tls_ca_certs=server.tls_ca_certs, tls_certkey=server.tls_certkey,
        tls_certkey_phrase=server.tls_certkey_phrase)
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
                auth_mech=server.auth_mech, ssl_client_ca=server.ssl_client_ca,
                ssl_client_cert=server.ssl_client_cert,
                ssl_client_key=server.ssl_client_key,
                ssl_client_phrase=server.ssl_client_phrase,
                auth_type=server.auth_type, tls_ca_certs=server.tls_ca_certs,
                tls_certkey=server.tls_certkey,
                tls_certkey_phrase=server.tls_certkey_phrase)
            status2 = repinst.connect()

            if status2[0]:

                call_func(args, func_dict, repinst)
                mongo_libs.disconnect([repinst])

            else:
                print(f"run_program.RepSet: Connection failure:  {status2[1]}")

        else:
            gen_libs.prt_msg("Error", "No replication found.", 0)

        mongo_libs.disconnect([coll])

    else:
        print(f"run_program.Coll: Connection failure:  {status[1]}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        file_perm_chk -> file check options with their perms in octal
        file_crt -> contains options which require files to be created
        func_dict -> dictionary list for the function calls or other options
        opt_con_req_list -> contains the options that require other options
        opt_def_dict -> contains options with their default values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5}
    file_perm_chk = {"-o": 6}
    file_crt = ["-o"]
    func_dict = {
        "-L": chk_rep_lag, "-M": fetch_members, "-S": chk_rep_stat,
        "-P": fetch_priority, "-T": prt_rep_stat, "-N": node_chk}
    opt_con_req_list = {"-i": ["-m"], "-s": ["-e"], "-u": ["-e"], "-k": ["-r"]}
    opt_def_dict = {"-i": "sysmon:mongo_rep_lag"}
    opt_multi_list = ["-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-i", "-m", "-o", "-e", "-s", "-k", "-a"]

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, opt_def=opt_def_dict,
        multi_val=opt_multi_list)

    if args.arg_parse2()                                                    \
       and not gen_libs.help_func(args, __version__, help_message)          \
       and args.arg_require(opt_req=opt_req_list)                           \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)                  \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)                    \
       and args.arg_file_chk(file_perm_chk=file_perm_chk, file_crt=file_crt):
        run_program(args, func_dict)


if __name__ == "__main__":
    sys.exit(main())
