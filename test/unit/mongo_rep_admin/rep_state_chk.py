#!/usr/bin/python
# Classification (U)

"""Program:  rep_state_chk.py

    Description:  Unit testing of rep_state_chk in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/rep_state_chk.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_print_all -> Test with print all option.
        test_good_state -> Test with good state.
        test_bad_state -> Test with bad state.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"state": 1, "stateStr": "StringHere"}
        self.rep_stat2 = {"state": 3, "stateStr": "StringHere"}

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    def test_print_all(self, mock_prt):

        """Function:  test_print_all

        Description:  Test with print all option.

        Arguments:

        """

        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.rep_state_chk(self.rep_stat,
                                                       prt_all=True))

    def test_good_state(self):

        """Function:  test_good_state

        Description:  Test with good state.

        Arguments:

        """

        self.assertFalse(mongo_rep_admin.rep_state_chk(self.rep_stat))

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    def test_bad_state(self, mock_prt):

        """Function:  test_bad_state

        Description:  Test with bad state.

        Arguments:

        """

        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.rep_state_chk(self.rep_stat2))


if __name__ == "__main__":
    unittest.main()
