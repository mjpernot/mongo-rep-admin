#!/usr/bin/python
# Classification (U)

"""Program:  fetch_rep_lag.py

    Description:  Unit testing of fetch_rep_lag in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/get_optimedate.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_std_out -> Test with standard out option.
        test_json -> Test with JSON option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.optdt = "2019-07-26 11:13:02"
        self.dtg = "2019-07-26 11:12:12"
        self.results = 50

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    def test_std_out(self, mock_prt):

        """Function:  test_std_out

        Description:  Test with standard out option.

        Arguments:

        """

        mock_prt.return_value = True

        #with gen_libs.no_std_out():
        self.assertFalse(mongo_rep_admin.fetch_rep_lag(self.dtg,
                                                       optdt=self.optdt,
                                                       suf="Primary"))

    def test_json(self):

        """Function:  test_json

        Description:  Test with JSON option.

        Arguments:

        """

        self.assertEqual(mongo_rep_admin.fetch_rep_lag(self.dtg,
                                                       optdt=self.optdt,
                                                       json=True),
                         self.results)


if __name__ == "__main__":
    unittest.main()
