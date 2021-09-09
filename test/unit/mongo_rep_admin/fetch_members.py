#!/usr/bin/python
# Classification (U)

"""Program:  fetch_members.py

    Description:  Unit testing of fetch_members in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/fetch_members.py

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
        __init__
        adm_cmd

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "spock"
        self.data = {"members": [{"name": "mongo1:27017", "state": 1},
                                 {"name": "mongo2:27017", "state": 2},
                                 {"name": "mongo3:27017", "state": 2}]}
        self.cmd = None

    def adm_cmd(self, cmd):

        """Method:  adm_cmd

        Description:  adm_cmd method.

        Arguments:

        """

        self.cmd = cmd

        return self.data


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_members

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-T": "TimeLag"}
        self.status = (True, None)

    def test_fetch_members(self):

        """Function:  test_fetch_members

        Description:  Test fetch_members function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.fetch_members(
                    self.server, self.args_array), self.status)


if __name__ == "__main__":
    unittest.main()
