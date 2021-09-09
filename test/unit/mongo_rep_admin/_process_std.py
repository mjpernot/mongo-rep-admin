#!/usr/bin/python
# Classification (U)

"""Program:  _process_std.py

    Description:  Unit testing of _process_std in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/_process_std.py

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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.lag_time = lag_time
        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

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
        setUp
        test_mongo_failure
        test_mongo_successful
        test_std_out
        test_stdout_suppress
        test_mongo
        test_file_append
        test_file
        test_email

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.primary = "primary"
        self.outdata = {
            "Application": "Mongo Replication",
            "Master": "mongo1:27017",
            "RepSet": "spock",
            "AsOf": "2020-07-13 11:51:21",
            "Slaves": [{"LagTime": 0,
                        "SyncTo": "2020-07-13 10:51:19",
                        "Name": "mongo2:27017"},
                       {"LagTime": 10,
                        "SyncTo": "2020-07-13 10:51:09",
                        "Name": "mongo3:27017"}]}
        self.args_array = {}
        self.args_array2 = {"-z": True}
        self.args_array3 = {"-z": True, "-a": True}
        self.conn = (True, None)
        self.conn2 = (False, "Error Message")
        self.status = (True, None)
        self.status2 = (False, "_process_std: Error Message")
        self.db_tbl = "db:tbl"

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_failure(self, mock_mongo):

        """Function:  test_mongo_failure

        Description:  Test with failed connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn2

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args_array=self.args_array2, suf=self.primary), self.status2)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_successful(self, mock_mongo):

        """Function:  test_mongo_successful

        Description:  Test with successful connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args_array=self.args_array2, suf=self.primary), self.status)

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test standard out format print.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin._process_std(
                    self.outdata, args_array=self.args_array,
                    suf=self.primary), self.status)

    def test_stdout_suppress(self):

        """Function:  test_stdout_suppress

        Description:  Test with standard out suppressed.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, args_array=self.args_array2, suf=self.primary),
            self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo):

        """Function:  test_mongo

        Description:  Test with writing to mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args_array=self.args_array2, suf=self.primary), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.openfile",
                mock.Mock(return_value="File_Handler"))
    @mock.patch("mongo_rep_admin.gen_libs.write_file2",
                mock.Mock(return_value=True))
    def test_file_append(self):

        """Function:  test_file_append

        Description:  Test with writing to file in append mode.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, ofile="Filename", args_array=self.args_array3,
                suf=self.primary), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.openfile",
                mock.Mock(return_value="File_Handler"))
    @mock.patch("mongo_rep_admin.gen_libs.write_file2",
                mock.Mock(return_value=True))
    def test_file(self):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, ofile="Filename", args_array=self.args_array2,
                suf=self.primary), self.status)

    def test_email(self):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_std(
                self.outdata, mail=self.mail, args_array=self.args_array2,
                suf=self.primary), self.status)


if __name__ == "__main__":
    unittest.main()
