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
import datetime

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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__ -> Class initialization.
        add_2_msg -> Stub method holder for Mail.add_2_msg.
        send_mail -> Stub method holder for Mail.send_mail.

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        pass

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        return True

    def send_mail(self):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_json_stdout_suppress -> Test with JSON format std out suppression.
        test_json_stdout -> Test with JSON format to standard out.
        test_no_rep_info -> Test with no replication information.
        test_mongo -> Test with writing to mongo.
        test_file -> Test with writing to file.
        test_email -> Test with email option.
        test_json -> Test with JSON format.
        test_std_out -> Test with standard out.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.t_format = "%Y-%m-%d %H:%M:%S"
        self.mail = Mail()
        self.rep_status = {
            "set": "ReplicaSet",
            "members": [{"state": 1, "name": "server1",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:01", self.t_format),
                         "optime": True},
                        {"state": 2, "name": "server2",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:02", self.t_format),
                         "optime": True}]}
        self.rep_status2 = {
            "set": "ReplicaSet",
            "members": [{"state": 1, "name": "server1",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:01", self.t_format)},
                        {"state": 2, "name": "server2",
                         "optimeDate": datetime.datetime.strptime(
                             "2019-07-26 11:13:02", self.t_format)}]}
        self.get_master = {"name": "master_server"}
        self.args_array = {"-z": True}
        self.args_array2 = {}

    @mock.patch("mongo_rep_admin.gen_libs.display_data")
    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_json_stdout_suppress(self, mock_mst, mock_lag, mock_prt):

        """Function:  test_json_stdout_suppress

        Description:  Test with JSON format to standard out suppression.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True
        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status, json=True, args_array=self.args_array))

    @mock.patch("mongo_rep_admin.gen_libs.display_data")
    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_json_stdout(self, mock_mst, mock_lag, mock_prt):

        """Function:  test_json_stdout

        Description:  Test with JSON format to standard out.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True
        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status, json=True, args_array=self.args_array2))

    @mock.patch("mongo_rep_admin.gen_libs.prt_msg")
    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_no_rep_info(self, mock_mst, mock_lag, mock_prt):

        """Function:  test_no_rep_info

        Description:  Test with no replication information.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True
        mock_prt.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status2, json=True, args_array=self.args_array))

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_mongo(self, mock_mst, mock_lag, mock_mongo):

        """Function:  test_mongo

        Description:  Test with writing to mongo.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True
        mock_mongo.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status, json=True, class_cfg="mongocfg", db_tbl="db:tbl",
            args_array=self.args_array))

    @mock.patch("mongo_rep_admin.gen_libs.write_file")
    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_file(self, mock_mst, mock_lag, mock_file):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True
        mock_file.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status, json=True, ofile="Filename",
            args_array=self.args_array))

    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_email(self, mock_mst, mock_lag):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status, json=True, mail=self.mail,
            args_array=self.args_array))

    @mock.patch("mongo_rep_admin.fetch_rep_lag")
    @mock.patch("mongo_rep_admin.get_master")
    def test_json(self, mock_mst, mock_lag):

        """Function:  test_json

        Description:  Test with JSON format.

        Arguments:

        """

        mock_mst.return_value = self.get_master
        mock_lag.return_value = True

        self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
            self.rep_status, json=True, args_array=self.args_array))

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
            self.assertFalse(mongo_rep_admin.chk_mem_rep_lag(
                self.rep_status))


if __name__ == "__main__":
    unittest.main()
