#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin
import version

__version__ = version.__version__


def fetch_priority(repset, args_array, **kwargs):

    """Function:  fetch_priority

    Description:  Stub holder for mongo_rep_admin.fetch_priority function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    mail = kwargs.get("mail", None)
    status = True

    if args_array and repset and mail:
        status = True

    return status


def prt_rep_stat(repset, args_array, **kwargs):

    """Function:  prt_rep_stat

    Description:  Stub holder for mongo_rep_admin.prt_rep_stat function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    mail = kwargs.get("mail", None)
    status = True

    if args_array and repset and mail:
        status = True

    return status


class Coll(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.Coll.connect method.
        coll_cnt -> Stub holder for mongo_class.Coll.coll_cnt method.
        coll_find1 -> Stub holder for mongo_class.Coll.coll_find1 method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.count = 1

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True

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
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.RepSet.connect method.

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

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.RepSet.connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_repset_not_set -> Test with repset name not set in config.
        test_email -> Test with setting up email.
        test_replication -> Test with replication setup.
        test_no_replication -> Test with no replication setup.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Methods:
                __init__ -> Initialize configuration environment.

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
                self.use_arg = True
                self.use_uri = False

        self.server = CfgTest()
        self.server2 = CfgTest()
        self.server2.repset = None
        self.repset = RepSet()
        self.coll = Coll()
        self.args_array = {"-T": True, "-c": "config", "-d": "dir/path"}
        self.args_array2 = {"-T": True, "-c": "config", "-d": "dir/path",
                            "-e": "Email_Address"}
        self.func_dict = {"-P": fetch_priority, "-T": prt_rep_stat}

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

        self.assertFalse(mongo_rep_admin.run_program(self.args_array,
                                                     self.func_dict))

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

        self.assertFalse(mongo_rep_admin.run_program(self.args_array2,
                                                     self.func_dict))

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

        self.assertFalse(mongo_rep_admin.run_program(self.args_array,
                                                     self.func_dict))

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

        self.assertFalse(mongo_rep_admin.run_program(self.args_array,
                                                     self.func_dict))


if __name__ == "__main__":
    unittest.main()
