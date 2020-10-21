#!/usr/bin/python
# Classification (U)

"""Program:  fetch_priority.py

    Description:  Unit testing of fetch_priority in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/fetch_priority.py

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


class Coll(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.Coll.connect method.
        coll_find1 -> Stub holder for mongo_class.Coll.coll_find1 method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return {"members": [{"host": "HostName", "priority": 1}]}


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
        self.name = "name"
        self.user = "user"
        self.japd = None
        self.host = "host"
        self.port = 27017
        self.auth = "auth"
        self.conf_file = "conffile"
        self.auth_db = "authentication_db"
        self.use_arg = True
        self.use_uri = False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_priority -> Test fetch_priority function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.coll = Coll()
        self.args_array = {"-T": "TimeLag"}

    @mock.patch("mongo_rep_admin.cmds_gen.disconnect")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_fetch_priority(self, mock_coll, mock_cmd):

        """Function:  test_fetch_priority

        Description:  Test fetch_priority function.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_cmd.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mongo_rep_admin.fetch_priority(self.server,
                                                            self.args_array))


if __name__ == "__main__":
    unittest.main()
