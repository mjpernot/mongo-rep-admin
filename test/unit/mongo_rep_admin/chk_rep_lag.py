#!/usr/bin/python
# Classification (U)

"""Program:  chk_rep_lag.py

    Description:  Unit testing of chk_rep_lag in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/chk_rep_lag.py

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


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.
        adm_cmd -> Stub holder for mongo_class.Server.adm_cmd method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "RepsetName"

    def adm_cmd(self, cmd):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:
            (input) cmd -> Command.

        """

        return {"members": [{"name": "MemberName"}]}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_secondary_chk -> Test with time lag for secondary check.
        test_primary_chk -> Test with time lag for primary check.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.get_master = {"optimeDate": "2019-07-26 11:13:02"}
        self.server = Server()
        self.args_array = {"-m": "config", "-d": "directory/path"}

    @mock.patch("mongo_rep_admin.get_optimedate")
    @mock.patch("mongo_rep_admin.chk_mem_rep_lag")
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.get_master")
    def test_secondary_chk(self, mock_mst, mock_load, mock_lag, mock_time):

        """Function:  test_secondary_chk

        Description:  Test with time lag for secondary check.

        Arguments:

        """

        mock_mst.return_value = {}
        mock_load.return_value = "Mongo_Cfg"
        mock_lag.return_value = True
        mock_time.return_value = "2019-07-26 11:13:02"

        self.assertFalse(mongo_rep_admin.chk_rep_lag(self.server,
                                                     self.args_array))

    @mock.patch("mongo_rep_admin.chk_mem_rep_lag")
    @mock.patch("mongo_rep_admin.gen_libs.load_module")
    @mock.patch("mongo_rep_admin.get_master")
    def test_primary_chk(self, mock_mst, mock_load, mock_lag):

        """Function:  test_primary_chk

        Description:  Test with time lag for primary check.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_load.return_value = "Mongo_Cfg"
        mock_lag.return_value = True

        self.assertFalse(mongo_rep_admin.chk_rep_lag(self.server,
                                                     self.args_array))


if __name__ == "__main__":
    unittest.main()
