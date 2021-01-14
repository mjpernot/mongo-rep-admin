#!/usr/bin/python
# Classification (U)

"""Program:  process_json.py

    Description:  Unit testing of _process_json in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/process_json.py

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
        setUp -> Initialize testing environment.
        test_mongo_failure -> Test with failed connection to Mongo.
        test_mongo_successful -> Test with successful connection to Mongo.
        test_json_flatten -> Test with JSON format to standard out suppression.
        test_json_stdout_suppress -> Test with JSON format std out suppression.
        test_json_stdout -> Test with JSON format to standard out.
        test_mongo -> Test with writing to mongo.
        test_file_append -> Test with writing to file in append mode.
        test_file -> Test with writing to file.
        test_email -> Test with email option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.outdata = {
            "Application": "Mongo Replication",
            "RepSet": "RepSetName",
            "Master": "MasterRepName",
            "AsOf": datetime.datetime.strftime(datetime.datetime.now(),
                                               "%Y-%m-%d %H:%M:%S"),
            "Slaves": ["slave1", "slave2"]}
        self.args_array = {"-z": True}
        self.args_array2 = {}
        self.args_array3 = {"-z": True, "-a": True}
        self.args_array4 = {"-z": True, "-f": True}
        self.conn = (True, None)
        self.conn2 = (False, "Error Message")
        self.status = (True, None)
        self.status2 = (False, "_process_json: Error Message")
        self.db_tbl = "db:tbl"

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_failure(self, mock_mongo):

        """Function:  test_mongo_failure

        Description:  Test with failed connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn2

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args_array=self.args_array), self.status2)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_successful(self, mock_mongo):

        """Function:  test_mongo_successful

        Description:  Test with successful connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args_array=self.args_array), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_json_flatten(self):

        """Function:  test_json_flatten

        Description:  Test with JSON format flatten.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, args_array=self.args_array4),
            self.status)

    def test_json_stdout_suppress(self):

        """Function:  test_json_stdout_suppress

        Description:  Test with JSON format to standard out suppression.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, args_array=self.args_array), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_json_stdout(self):

        """Function:  test_json_stdout

        Description:  Test with JSON format to standard out.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, args_array=self.args_array2), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo):

        """Function:  test_mongo

        Description:  Test with writing to mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args_array=self.args_array), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file_append(self):

        """Function:  test_file_append

        Description:  Test with writing to file in append mode.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, ofile="Filename", args_array=self.args_array3),
            self.status)

    @mock.patch("mongo_rep_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file(self):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, ofile="Filename", args_array=self.args_array),
            self.status)

    def test_email(self):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin._process_json(
                self.outdata, mail=self.mail, args_array=self.args_array),
            self.status)


if __name__ == "__main__":
    unittest.main()
