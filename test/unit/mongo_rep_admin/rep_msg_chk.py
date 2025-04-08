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

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin                          # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_error_msg_true_nr_false
        test_error_msg_true_nr_true
        test_error_msg_false_nr_false
        test_error_msg_false_nr_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"infoMessage": None}
        self.rep_stat2 = {"infoMessage": "StringHere"}
#        self.rep_stat2 = {"state": 3, "stateStr": "StringHere"}
        self.server = {}
        self.no_report = True
        self.no_report2 = False
        self.results = {}
        self.results2 = {'ErrorMessage': None}
        self.results3 = {'ErrorMessage': 'StringHere'}

    def test_error_msg_true_nr_false(self):

        """Function:  test_error_msg_true_nr_false

        Description:  Test with error message false and no report false.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_msg_chk(
                self.rep_stat2, self.server, self.no_report2), self.results3)

    def test_error_msg_true_nr_true(self):

        """Function:  test_error_msg_true_nr_true

        Description:  Test with error message false and no report true.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_msg_chk(
                self.rep_stat2, self.server, self.no_report), self.results3)

    def test_error_msg_false_nr_false(self):

        """Function:  test_error_msg_false_nr_false

        Description:  Test with error message false and no report false.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_msg_chk(
                self.rep_stat, self.server, self.no_report2), self.results2)

    def test_error_msg_false_nr_true(self):

        """Function:  test_error_msg_false_nr_true

        Description:  Test with error message false and no report true.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_msg_chk(
                self.rep_stat, self.server, self.no_report), self.results)


if __name__ == "__main__":
    unittest.main()
