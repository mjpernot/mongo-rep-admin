# Classification (U)

"""Program:  chk_rep_stat.py

    Description:  Unit testing of chk_rep_stat in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/chk_rep_stat.py

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
        test_errors_detected
        test_no_report_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.status = (True, None)
        self.rep_health_chk = {}
        self.rep_health_chk2 = {"Health": "Bad"}
        self.rep_state_chk = {}
        self.rep_state_chk2 = {"State": 3}
        self.rep_msg_chk = {}
        self.rep_msg_chk2 = {"ErrorMessage": "MessageHere"}

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.rep_msg_chk")
    @mock.patch("mongo_rep_admin.rep_state_chk")
    @mock.patch("mongo_rep_admin.rep_health_chk")
    def test_errors_detected(self, mock_health, mock_state, mock_msg, mock_out):

        """Function:  test_errors_detected

        Description:  Test with errors detected.

        Arguments:

        """

        mock_health.return_value = self.rep_health_chk2
        mock_state.return_value = self.rep_state_chk2
        mock_msg.return_value = self.rep_msg_chk2
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_rep_stat(
                self.server, self.dtg, no_report=True), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.rep_msg_chk")
    @mock.patch("mongo_rep_admin.rep_state_chk")
    @mock.patch("mongo_rep_admin.rep_health_chk")
    def test_no_report_true(self, mock_health, mock_state, mock_msg, mock_out):

        """Function:  test_no_report_true

        Description:  Test with no report set to true.

        Arguments:

        """

        mock_health.return_value = self.rep_health_chk
        mock_state.return_value = self.rep_state_chk
        mock_msg.return_value = self.rep_msg_chk
        mock_out.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_rep_stat(
                self.server, self.dtg, no_report=True), self.status)


if __name__ == "__main__":
    unittest.main()
