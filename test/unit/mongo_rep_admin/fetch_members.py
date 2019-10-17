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
        is_primary -> Stub holder for mongo_class.Server.is_primary method.
        fetch_adr ->Stub holder for mongo_class.Server.fetch_adr method.
        fetch_nodes -> Stub holder for mongo_class.Server.fetch_nodes method.
        

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "RepsetName"
        self.primary = True

    def is_primary(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Server.is_primary method.

        Arguments:

        """

        return self.primary

    def fetch_adr(self):

        """Method:  fetch_adr

        Description:  Stub holder for mongo_class.Server.fetch_adr method.

        Arguments:

        """

        return ("server1", 27017)

    def fetch_nodes(self):

        """Method:  fetch_nodes

        Description:  Stub holder for mongo_class.Server.fetch_nodes method.

        Arguments:

        """

        return set([("server1", 27017), ("server2", 27017)])


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_members -> Test fetch_members function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-T": "TimeLag"}

    def test_fetch_members(self):

        """Function:  test_fetch_members

        Description:  Test fetch_members function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_rep_admin.fetch_members(self.server,
                                                           self.args_array))


if __name__ == "__main__":
    unittest.main()
