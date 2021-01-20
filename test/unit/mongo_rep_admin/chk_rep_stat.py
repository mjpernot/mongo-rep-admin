#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin
import lib.gen_libs as gen_libs
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
        setUp -> Initialize testing environment.
        test_chk_rep_stat -> Test chk_rep_stat function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-c": "config"}
        self.status = (True, None)

    @mock.patch("mongo_rep_admin.rep_msg_chk")
    @mock.patch("mongo_rep_admin.rep_state_chk")
    @mock.patch("mongo_rep_admin.rep_health_chk")
    def test_chk_rep_stat(self, mock_health, mock_state, mock_msg):

        """Function:  test_chk_rep_stat

        Description:  Test chk_rep_stat function.

        Arguments:

        """

        mock_health.return_value = True
        mock_state.return_value = True
        mock_msg.return_value = True

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.chk_rep_stat(
                    self.server, self.args_array), self.status)


if __name__ == "__main__":
    unittest.main()
