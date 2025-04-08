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
        test_state_bad_nr_false
        test_state_bad_nr_true
        test_state_good_nr_false
        test_state_good_nr_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"state": 1, "stateStr": "StringHere"}
        self.rep_stat2 = {"state": 3, "stateStr": "StringHere2"}
        self.server = {}
        self.no_report = True
        self.no_report2 = False
        self.results = {}
        self.results2 = {'Status': {'State': 1, 'StateMsg': 'StringHere'}}
        self.results3 = {'Status': {'State': 3, 'StateMsg': 'StringHere2'}}

    def test_state_bad_nr_false(self):

        """Function:  test_state_bad_nr_false

        Description:  Test with state is bad and no report false.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_state_chk(
                self.rep_stat2, self.server, self.no_report2), self.results3)

    def test_state_bad_nr_true(self):

        """Function:  test_state_bad_nr_true

        Description:  Test with state is vad and no report true.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_state_chk(
                self.rep_stat2, self.server, self.no_report), self.results3)

    def test_state_good_nr_false(self):

        """Function:  test_state_good_nr_false

        Description:  Test with state is good and no report false.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_state_chk(
                self.rep_stat, self.server, self.no_report2), self.results2)

    def test_state_good_nr_true(self):

        """Function:  test_state_good_nr_true

        Description:  Test with state is good and no report true.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.rep_state_chk(
                self.rep_stat, self.server, self.no_report), self.results)


if __name__ == "__main__":
    unittest.main()
