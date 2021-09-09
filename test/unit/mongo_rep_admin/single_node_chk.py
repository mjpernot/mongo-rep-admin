#!/usr/bin/python
# Classification (U)

"""Program:  single_node_chk.py

    Description:  Unit testing of single_node_chk in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/single_node_chk.py

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

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin
import version

__version__ = version.__version__


class Server(object):

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
                       []}

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
        test_two_failures
        test_message_fail
        test_state_fail
        test_health_fail
        test_good

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.node = {"name": "MemberName", "health": 1.0, "state": 1,
                     "stateStr": None, "infoMessage": None}
        self.results = {}
        self.results2 = {"Health": "Bad"}
        self.results3 = {"State": 8, "State_Message": "MessageHere"}
        self.results4 = {"Error_Message": "Error_Message_Here"}
        self.results5 = {"Health": "Bad",
                         "Error_Message": "Error_Message_Here"}

    def test_two_failures(self):

        """Function:  test_two_failures

        Description:  Test with two failures.

        Arguments:

        """

        self.node["infoMessage"] = "Error_Message_Here"
        self.node["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.single_node_chk(self.node), self.results5)

    def test_message_fail(self):

        """Function:  test_message_fail

        Description:  Test with message failure check.

        Arguments:

        """

        self.node["infoMessage"] = "Error_Message_Here"

        self.assertEqual(
            mongo_rep_admin.single_node_chk(self.node), self.results4)

    def test_state_fail(self):

        """Function:  test_state_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.node["state"] = 8
        self.node["stateStr"] = "MessageHere"

        self.assertEqual(
            mongo_rep_admin.single_node_chk(self.node), self.results3)

    def test_health_fail(self):

        """Function:  test_health_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.node["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.single_node_chk(self.node), self.results2)

    def test_good(self):

        """Function:  test_good

        Description:  Test with good status return on all checks.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.single_node_chk(self.node), self.results)


if __name__ == "__main__":
    unittest.main()
