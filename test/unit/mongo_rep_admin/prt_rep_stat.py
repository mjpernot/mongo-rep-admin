#!/usr/bin/python
# Classification (U)

"""Program:  prt_rep_stat.py

    Description:  Unit testing of prt_rep_stat in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/prt_rep_stat.py

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


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "RepsetName"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_prt_rep_stat -> Test prt_rep_stat function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-T": "TimeLag"}

    @mock.patch("mongo_rep_admin.chk_rep_stat")
    def test_prt_rep_stat(self, mock_stat):

        """Function:  test_prt_rep_stat

        Description:  Test prt_rep_stat function.

        Arguments:

        """

        mock_stat.return_value = True

        self.assertFalse(mongo_rep_admin.prt_rep_stat(self.server,
                                                      self.args_array))


if __name__ == "__main__":
    unittest.main()
