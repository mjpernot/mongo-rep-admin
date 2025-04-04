# Classification (U)

"""Program:  call_func.py

    Description:  Unit testing of call_func in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/call_func.py

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
import mongo_rep_admin                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def fetch_priority(repset, data_config, dtg):

    """Function:  fetch_priority

    Description:  Stub holder for mongo_rep_admin.fetch_priority function.

    Arguments:

    """

    err_msg = "Error Message"
    status = (False, err_msg)

    if data_config and repset and dtg:
        status = (False, err_msg)

    return status


def prt_rep_stat(repset, data_config, dtg):

    """Function:  prt_rep_stat

    Description:  Stub holder for mongo_rep_admin.prt_rep_stat function.

    Arguments:

    """

    status = (True, None)

    if data_config and repset and dtg:
        status = (True, None)

    return status


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_args_keys
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Coll():

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


class RepSet():                                         # pylint:disable=R0903

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
        self.use_arg = True
        self.use_uri = False
        self.conn = True
        self.errmsg = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_func_no_error
        test_func_error
        test_email

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repset = RepSet()
        self.err_msg = "Error Message"
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-T": True, "-c": "config", "-d": "dirpath"}
        self.args2.args_array = {
            "-T": True, "-c": "config", "-d": "dirpath", "-e": "Email_Address"}
        self.args3.args_array = {"-P": True, "-c": "config", "-d": "dirpath"}
        self.func_names = {"-P": fetch_priority, "-T": prt_rep_stat}
        self.data_config = {"to_addr": "ToAddress", "suppress": True}

    @mock.patch("mongo_rep_admin.create_data_config")
    def test_func_no_error(self, mock_config):

        """Function:  test_func_no_error

        Description:  Test with no error returned from function call.

        Arguments:

        """

        mock_config.return_value = self.data_config

        self.assertFalse(
            mongo_rep_admin.call_func(
                self.args, self.func_names, self.repset))

    @mock.patch("mongo_rep_admin.create_data_config")
    def test_func_error(self, mock_config):

        """Function:  test_func_error

        Description:  Test with error returned from function call.

        Arguments:

        """

        mock_config.return_value = self.data_config

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_rep_admin.call_func(
                    self.args3, self.func_names, self.repset))


if __name__ == "__main__":
    unittest.main()
