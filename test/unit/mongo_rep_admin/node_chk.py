# Classification (U)

"""Program:  node_chk.py

    Description:  Unit testing of node_chk in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/node_chk.py

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
        self.status = {"members":
                       [{"name": "MemberName", "health": 1.0, "state": 1,
                         "stateStr": None, "infoMessage": None}]}
        self.host = "HostName"

    def adm_cmd(self, cmd):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:
            (input) cmd -> Command.

        """

        self.cmd = cmd

        return self.status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_message_fail
        test_state_fail
        test_health_fail
        test_good_no_report
        test_good

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.server = Server()
        self.data_config = {"to_addr": "ToAddress"}
        self.data_config2 = {"to_addr": "ToAddress", "no_report": True}
        self.status = (True, None)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out",
                mock.Mock(return_value=(True, None)))
    def test_health_fail(self):

        """Function:  test_health_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.dtg, **self.data_config), self.status)

    def test_good_no_report(self):

        """Function:  test_good_no_report

        Description:  Test with good status return on all checks.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.dtg, **self.data_config2), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out",
                mock.Mock(return_value=(True, None)))
    def test_good(self):

        """Function:  test_good

        Description:  Test with good status return on all checks.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.dtg, **self.data_config), self.status)


if __name__ == "__main__":
    unittest.main()
