# Classification (U)

"""Program:  process_json.py

    Description:  Unit testing of process_json in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/process_json.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Mail():

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

    def send_mail(self, use_mailx=False):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:
            (input) use_mailx -> True|False - To use mailx command.

        """

        status = True

        if use_mailx:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mongo_failure
        test_mongo_successful
        test_json_flatten
        test_json_stdout_suppress
        test_json_stdout
        test_mongo
        test_file_append
        test_file
        test_email_mailx
        test_email

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
        self.args = ArgParser()
        self.argsa = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args.args_array = {"-z": True}
        self.argsa.args_array = {"-z": True, "-u": True}
        self.args2.args_array = {}
        self.args3.args_array = {"-z": True, "-a": True}
        self.args4.args_array = {"-z": True, "-f": True}
        self.conn = (True, None)
        self.conn2 = (False, "Error Message")
        self.status = (True, None)
        self.status2 = (False, "process_json: Error Message")
        self.db_tbl = "db:tbl"

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_failure(self, mock_mongo):

        """Function:  test_mongo_failure

        Description:  Test with failed connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn2

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args=self.args), self.status2)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_successful(self, mock_mongo):

        """Function:  test_mongo_successful

        Description:  Test with successful connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args=self.args), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_json_flatten(self):

        """Function:  test_json_flatten

        Description:  Test with JSON format flatten.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, args=self.args4), self.status)

    def test_json_stdout_suppress(self):

        """Function:  test_json_stdout_suppress

        Description:  Test with JSON format to standard out suppression.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, args=self.args), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_json_stdout(self):

        """Function:  test_json_stdout

        Description:  Test with JSON format to standard out.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, args=self.args2), self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo):

        """Function:  test_mongo

        Description:  Test with writing to mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args=self.args), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file_append(self):

        """Function:  test_file_append

        Description:  Test with writing to file in append mode.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, ofile="Filename", args=self.args3), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_file(self):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, ofile="Filename", args=self.args), self.status)

    def test_email_mailx(self):

        """Function:  test_email_mailx

        Description:  Test with email option using mailx.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, mail=self.mail, args=self.argsa), self.status)

    def test_email(self):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_json(
                self.outdata, mail=self.mail, args=self.args), self.status)


if __name__ == "__main__":
    unittest.main()
