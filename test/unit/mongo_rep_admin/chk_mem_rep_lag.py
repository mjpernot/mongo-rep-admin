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
import datetime
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_empty_repset
        test_only_primary
        test_no_rep_info
        test_single_rep_member
        test_multiple_rep_members

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.date = "2019-07-26 11:13:02"
        self.t_format = "%Y-%m-%d %H:%M:%S"
        self.primary = "primary"
        self.rep_status = {
            "set": "ReplicaSet",
            "members": [{"state": 1, "name": "server1",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:01", self.t_format),
                         "optime": True},
                        {"state": 2, "name": "server2",
                         "optimeDate": datetime.datetime.strptime(
                             self.date, self.t_format),
                         "optime": True}]}
        self.rep_status2 = {
            "set": "ReplicaSet",
            "members": [{"state": 1, "name": "server1",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:01", self.t_format)},
                        {"state": 2, "name": "server2",
                         "optimeDate": datetime.datetime.strptime(
                             self.date, self.t_format)}]}
        self.rep_status3 = {"set": "ReplicaSet", "members": []}
        self.rep_status4 = {
            "set": "ReplicaSet",
            "members": [{"state": 1, "name": "server1",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:01", self.t_format),
                         "optime": True}]}
        self.rep_status5 = {
            "set": "ReplicaSet",
            "members": [{"state": 1, "name": "server1",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:01", self.t_format),
                         "optime": True},
                        {"state": 2, "name": "server2",
                         "optimeDate": datetime.datetime.strptime(
                             self.date, self.t_format),
                         "optime": True},
                        {"state": 2, "name": "server3",
                         "optimeDate": datetime.datetime.strptime(
                             self.date, self.t_format),
                         "optime": True}]}
        self.optdt = datetime.datetime.strptime(self.date, "%Y-%m-%d %H:%M:%S")
        self.get_master = {"name": "master_server"}
        self.data_config = {"suppress": True, "mode": "a"}
        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.status = (True, None)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.get_master")
    def test_empty_repset(self, mock_mst, mock_process):

        """Function:  test_empty_repset

        Description:  Test with an empty replication set.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_process.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_mem_rep_lag(
                self.rep_status3, self.dtg, **self.data_config), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.get_master")
    def test_only_primary(self, mock_mst, mock_process):

        """Function:  test_only_primary

        Description:  Test with only primary present.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_process.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_mem_rep_lag(
                self.rep_status4, self.dtg, **self.data_config), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    @mock.patch("mongo_rep_admin.get_master")
    def test_no_rep_info(self, mock_mst, mock_prt, mock_process):

        """Function:  test_no_rep_info

        Description:  Test with no replication information.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_prt.return_value = True
        mock_process.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_mem_rep_lag(
                self.rep_status2, self.dtg, **self.data_config), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.get_master")
    def test_single_rep_member(self, mock_mst, mock_process):

        """Function:  test_single_rep_member

        Description:  Test with single secondary replication member.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_process.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_mem_rep_lag(
                self.rep_status, self.dtg, optdt=self.optdt,
                **self.data_config), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.data_out")
    @mock.patch("mongo_rep_admin.get_master")
    def test_multiple_rep_members(self, mock_mst, mock_process):

        """Function:  test_multiple_rep_members

        Description:  Test with multiple secondary replication members.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_process.return_value = self.status

        self.assertEqual(
            mongo_rep_admin.chk_mem_rep_lag(
                self.rep_status5, self.dtg, optdt=self.optdt,
                **self.data_config), self.status)


if __name__ == "__main__":
    unittest.main()
