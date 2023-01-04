# Classification (U)

"""Program:  rep_health_chk.py

    Description:  Unit testing of rep_health_chk in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/rep_health_chk.py

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
        test_print_all
        test_good_health
        test_bad_health

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"health": False}
        self.rep_stat2 = {"health": True}

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    def test_print_all(self, mock_prt):

        """Function:  test_print_all

        Description:  Test with print all option.

        Arguments:

        """

        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.rep_health_chk(self.rep_stat2,
                                                        prt_all=True))

    def test_good_health(self):

        """Function:  test_good_health

        Description:  Test with good health.

        Arguments:

        """

        self.assertFalse(mongo_rep_admin.rep_health_chk(self.rep_stat2))

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    def test_bad_health(self, mock_prt):

        """Function:  test_bad_health

        Description:  Test with bad health.

        Arguments:

        """

        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.rep_health_chk(self.rep_stat))


if __name__ == "__main__":
    unittest.main()
