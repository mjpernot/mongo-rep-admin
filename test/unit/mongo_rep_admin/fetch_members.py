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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin                          # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                                         # pylint:disable=R0903

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
        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.status = (True, None)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out",
                mock.Mock(return_value=(True, None)))
    def test_fetch_members2(self):

        """Function:  test_fetch_members2

        Description:  Test fetch_members function with one member state 3.

        Arguments:

        """

        self.server.data = {
            "members": [{"name": "mongo1:27017", "state": 1},
                        {"name": "mongo2:27017", "state": 2},
                        {"name": "mongo3:27017", "state": 3}]}

        self.assertEqual(
            mongo_rep_admin.fetch_members(self.server, self.dtg), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out",
                mock.Mock(return_value=(True, None)))
    def test_fetch_members(self):

        """Function:  test_fetch_members

        Description:  Test fetch_members function.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.fetch_members(self.server, self.dtg), self.status)


if __name__ == "__main__":
    unittest.main()
