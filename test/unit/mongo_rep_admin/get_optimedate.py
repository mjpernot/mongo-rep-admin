#!/usr/bin/python
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
        test_get_optimedate -> Test get_optimedate function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_stat = {"members": [{"optimeDate": "2019-07-26 11:13:01",
                                      "name": "server1"},
                                     {"optimeDate": "2019-07-26 11:13:02",
                                      "name": "server2"}]}
        self.results = "2019-07-26 11:13:02"

    def test_get_optimedate(self):

        """Function:  test_get_optimedate

        Description:  Test get_optimedate function.

        Arguments:

        """

        self.assertEqual(mongo_rep_admin.get_optimedate(self.rep_stat),
                         self.results)


if __name__ == "__main__":
    unittest.main()
