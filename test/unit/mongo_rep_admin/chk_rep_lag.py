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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin                          # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        adm_cmd

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "RepsetName"
        self.cmd = None

    def adm_cmd(self, cmd):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:
            (input) cmd -> Command.

        """

        self.cmd = cmd

        return {"members": [{"name": "MemberName"}]}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_secondary_chk
        test_primary_chk

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.get_master = {"optimeDate": "2019-07-26 11:13:02"}
        self.server = Server()
        self.data_config = {"to_addr": "ToAddress", "suppress": True}
        self.dtg = gen_class.TimeFormat()
        self.status = (True, None)
        self.status2 = (False, "_process_std: Error Message")
        self.status3 = (False, "_process_json: Error Message")
        self.results = (True, None)
        self.results2 = (False, "_process_std: Error Message")
        self.results3 = (False, "_process_json: Error Message")

    @mock.patch("mongo_rep_admin.get_optimedate")
    @mock.patch("mongo_rep_admin.chk_mem_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_secondary_chk(self, mock_mst, mock_lag, mock_time):

        """Function:  test_secondary_chk

        Description:  Test with time lag for secondary check.

        Arguments:

        """

        mock_mst.return_value = {}
        mock_lag.return_value = self.status
        mock_time.return_value = "2019-07-26 11:13:02"

        self.assertEqual(
            mongo_rep_admin.chk_rep_lag(
                self.server, self.dtg, **self.data_config), self.results)

    @mock.patch("mongo_rep_admin.chk_mem_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_primary_chk(self, mock_mst, mock_lag):

        """Function:  test_primary_chk

        Description:  Test with time lag for primary check.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_rep_lag(
                self.server, self.dtg, **self.data_config), self.results)


if __name__ == "__main__":
    unittest.main()
