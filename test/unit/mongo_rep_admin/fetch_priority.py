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
        __init__
        connect
        coll_find1

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.members = {"members": [{"host": "HostName", "priority": 1}]}
        self.conn = True
        self.errmsg = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return self.conn, self.errmsg

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return self.members


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__

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
        self.auth_mech = "SCRAM-SHA-1"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_failed_connection
        test_succesful_connection
        test_multiple_list
        test_empty_list
        test_fetch_priority

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.coll = Coll()
        self.args_array = {"-T": "TimeLag"}
        self.status = (True, None)
        self.status2 = (False,
                        "fetch_priority:  Connection failure:  Error Message")

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_failed_connection(self, mock_coll):

        """Function:  test_failed_connection

        Description:  Test with failed connection.

        Arguments:

        """

        self.coll.conn = False
        self.coll.errmsg = "Error Message"

        mock_coll.return_value = self.coll

        self.assertEqual(
            mongo_rep_admin.fetch_priority(
                self.server, self.args_array), self.status2)

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_succesful_connection(self, mock_coll):

        """Function:  test_succesful_connection

        Description:  Test with successful connection.

        Arguments:

        """

        mock_coll.return_value = self.coll

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.fetch_priority(
                    self.server, self.args_array), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_multiple_list(self, mock_coll):

        """Function:  test_multiple_list

        Description:  Test return multiple members.

        Arguments:

        """

        self.coll.members["members"].append(
            {"host": "HostName2", "priority": 1})

        mock_coll.return_value = self.coll

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.fetch_priority(
                    self.server, self.args_array), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_empty_list(self, mock_coll):

        """Function:  test_empty_list

        Description:  Test return no members.

        Arguments:

        """

        self.coll.members["members"] = []

        mock_coll.return_value = self.coll

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.fetch_priority(
                    self.server, self.args_array), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_fetch_priority(self, mock_coll):

        """Function:  test_fetch_priority

        Description:  Test fetch_priority function.

        Arguments:

        """

        mock_coll.return_value = self.coll

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.fetch_priority(
                    self.server, self.args_array), self.status)


if __name__ == "__main__":
    unittest.main()
