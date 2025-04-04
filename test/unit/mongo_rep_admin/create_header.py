# Classification (U)

"""Program:  create_header.py

    Description:  Unit testing of create_header in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/create_header.py

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
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_header

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.name = "NodeCheck"
        self.results = "NodeCheck"

    def test_header(self):

        """Function:  test_state_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.create_header(self.name, self.dtg)["Check"],
            self.results)


if __name__ == "__main__":
    unittest.main()
