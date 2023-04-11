# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/run_program.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def fetch_priority(repset, args_array, **kwargs):

    """Function:  fetch_priority

    Description:  Stub holder for mongo_rep_admin.fetch_priority function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    err_msg = "Error Message"
    mail = kwargs.get("mail", None)
    status = (False, err_msg)

    if args_array and repset and mail:
        status = (False, err_msg)

    return status


def prt_rep_stat(repset, args_array, **kwargs):

    """Function:  prt_rep_stat

    Description:  Stub holder for mongo_rep_admin.prt_rep_stat function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    mail = kwargs.get("mail", None)
    status = (True, None)

    if args_array and repset and mail:
        status = (True, None)

    return status


class Coll(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__
        connect
        coll_cnt
        coll_find1

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.count = 1
        self.conn = True
        self.errmsg = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return self.conn, self.errmsg

    def coll_cnt(self):

        """Method:  coll_cnt

        Description:  Stub holder for mongo_class.Coll.coll_cnt method.

        Arguments:

        """

        return self.count

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return {"_id": "RepSetName"}


class RepSet(object):

    """Class:  RepSet

    Description:  Class stub holder for mongo_class.RepSet class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = None
        self.host = "host"
        self.port = 27017
        self.auth = "auth"
        self.conf_file = "conffile"
        self.auth_db = "authentication_db"
        self.conn = True
        self.errmsg = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.RepSet.connect method.

        Arguments:

        """

        return self.conn, self.errmsg


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = None
        self.host = "host"
        self.port = 27017
        self.auth = "auth"
        self.conf_file = "conffile"
        self.repset = "repsetname"
        self.repset_hosts = "localhost:27017,localhost:27016"
        self.auth_db = "authentication_db"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_func_no_error
        test_func_error
        test_auth_mech
        test_failed_conn_repset
        test_successful_conn_repset
        test_failed_conn_coll
        test_successful_conn_coll
        test_repset_not_set
        test_email
        test_replication
        test_no_replication

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = CfgTest()
        self.server2 = CfgTest()
        self.server2.repset = None
        self.repset = RepSet()
        self.coll = Coll()
        self.err_msg = "Error Message"
        self.args_array = {"-T": True, "-c": "config", "-d": "dirpath"}
        self.args_array2 = {"-T": True, "-c": "config", "-d": "dirpath",
                            "-e": "Email_Address"}
        self.args_array3 = {"-P": True, "-c": "config", "-d": "dirpath"}
        self.func_names = {"-P": fetch_priority, "-T": prt_rep_stat}

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_func_no_error(self, mock_coll, mock_repset, mock_load):

        """Function:  test_func_no_error

        Description:  Test with no error returned from function call.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_func_error(self, mock_coll, mock_repset, mock_load):

        """Function:  test_func_error

        Description:  Test with error returned from function call.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_rep_admin.run_program(self.args_array3, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_auth_mech(self, mock_coll, mock_repset, mock_load):

        """Function:  test_auth_mech

        Description:  Test with auth_mech passed.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_failed_conn_repset(self, mock_coll, mock_repset, mock_load):

        """Function:  test_failed_conn_repset

        Description:  Test with failed connection.

        Arguments:

        """

        self.repset.conn = False
        self.repset.errmsg = self.err_msg

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_successful_conn_repset(self, mock_coll, mock_repset, mock_load):

        """Function:  test_successful_conn_repset

        Description:  Test with successful connection.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_failed_conn_coll(self, mock_coll, mock_load):

        """Function:  test_failed_conn_coll

        Description:  Test with failed connection.

        Arguments:

        """

        self.coll.conn = False
        self.coll.errmsg = self.err_msg

        mock_coll.return_value = self.coll
        mock_load.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_successful_conn_coll(self, mock_coll, mock_repset, mock_load):

        """Function:  test_successful_conn_coll

        Description:  Test with successful connection.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_repset_not_set(self, mock_coll, mock_repset, mock_load):

        """Function:  test_repset_not_set

        Description:  Test with repset name not set in config.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server2

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_class.setup_mail")
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_email(self, mock_coll, mock_repset, mock_load,
                   mock_mail):

        """Function:  test_email

        Description:  Test with setting up email.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server
        mock_mail.return_value = "Mail Instance"

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array2, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.prt_msg",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_no_replication(self, mock_coll, mock_load):

        """Function:  test_no_replication

        Description:  Test with no replication setup.

        Arguments:

        """

        self.coll.count = 0
        mock_coll.return_value = self.coll
        mock_load.return_value = self.server

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_replication(self, mock_coll, mock_repset, mock_load):

        """Function:  test_replication

        Description:  Test with replication setup.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_repset.return_value = self.repset
        mock_load.return_value = self.server

        self.assertFalse(
            mongo_rep_admin.run_program(self.args_array, self.func_names))


if __name__ == "__main__":
    unittest.main()
