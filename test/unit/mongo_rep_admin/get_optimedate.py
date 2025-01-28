# Classification (U)

"""Program:  get_optimedate.py

    Description:  Unit testing of get_optimedate in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/get_optimedate.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import datetime
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
        test_get_optimedate

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.t_format = "%Y-%m-%d %H:%M:%S"
        self.rep_stat = \
            {"members": [{"optimeDate":
                          datetime.datetime.strptime("2019-07-26 11:13:01",
                                                     self.t_format),
                          "name": "server1"},
                         {"optimeDate":
                          datetime.datetime.strptime("2019-07-26 11:13:02",
                                                     self.t_format),
                          "name": "server2"}]}
        self.results = datetime.datetime.strptime("2019-07-26 11:13:02",
                                                  self.t_format)

    def test_get_optimedate(self):

        """Function:  test_get_optimedate

        Description:  Test get_optimedate function.

        Arguments:

        """

        self.assertEqual(mongo_rep_admin.get_optimedate(self.rep_stat),
                         self.results)


if __name__ == "__main__":
    unittest.main()
