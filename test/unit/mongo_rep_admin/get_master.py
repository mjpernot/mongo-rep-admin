# Classification (U)

"""Program:  get_master.py

    Description:  Unit testing of get_master in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/get_master.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party

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
        test_error_msg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"members": [{"state": 3, "name": "server1"},
                                     {"state": 1, "name": "server2"}]}
        self.results = {"state": 1, "name": "server2"}

    def test_get_master(self):

        """Function:  test_get_master

        Description:  Test get_master function.

        Arguments:

        """

        self.assertEqual(mongo_rep_admin.get_master(self.rep_stat),
                         self.results)


if __name__ == "__main__":
    unittest.main()
