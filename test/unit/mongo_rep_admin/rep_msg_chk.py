# Classification (U)

"""Program:  rep_msg_chk.py

    Description:  Unit testing of rep_msg_chk in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/rep_msg_chk.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_error_msg
        test_error_msg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"infoMessage": "StringHere"}
        self.rep_stat2 = {"state": 3, "stateStr": "StringHere"}

    def test_no_error_msg(self):

        """Function:  test_no_error_msg

        Description:  Test with no error message.

        Arguments:

        """

        self.assertFalse(mongo_rep_admin.rep_msg_chk(self.rep_stat2))

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    def test_error_msg(self, mock_prt):

        """Function:  test_error_msg

        Description:  Test with error message.

        Arguments:

        """

        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.rep_msg_chk(self.rep_stat))


if __name__ == "__main__":
    unittest.main()
