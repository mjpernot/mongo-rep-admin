#!/usr/bin/python
# Classification (U)

"""Program:  chk_mem_rep_lag.py

    Description:  Unit testing of chk_mem_rep_lag in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/chk_mem_rep_lag.py

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
        test_std_out -> Test with standard out.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rep_status = {"set": "ReplicaSet",
                           "members": [{"state": 1, "name": "server1",
                                        "optimeDate": "2019-07-26 11:13:01",
                                        "optime": True},
                                       {"state": 2, "name": "server2",
                                        "optimeDate": "2019-07-26 11:13:02",
                                        "optime": True}]}
        self.get_master = {"name": "master_server"}

    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_std_out(self, mock_mst, mock_lag):

        """Function:  test_std_out

        Description:  Test with standard out.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(self.rep_status))


if __name__ == "__main__":
    unittest.main()
