# Classification (U)

"""Program:  process_std.py

    Description:  Unit testing of process_std in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/process_std.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
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
        test_std_out
        test_stdout_suppress
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
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args2a = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {}
        self.args2.args_array = {"-z": True}
        self.args2a.args_array = {"-z": True, "-u": True}
        self.args3.args_array = {"-z": True, "-a": True}
        self.conn = (True, None)
        self.conn2 = (False, "Error Message")
        self.status = (True, None)
        self.status2 = (False, "process_std: Error Message")
        self.db_tbl = "db:tbl"

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_failure(self, mock_mongo):

        """Function:  test_mongo_failure

        Description:  Test with failed connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn2

        self.assertEqual(
            mongo_rep_admin.process_std(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args=self.args2, suf=self.primary), self.status2)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo_successful(self, mock_mongo):

        """Function:  test_mongo_successful

        Description:  Test with successful connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin.process_std(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args=self.args2, suf=self.primary), self.status)

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test standard out format print.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_rep_admin.process_std(
                    self.outdata, args=self.args, suf=self.primary),
                self.status)

    def test_stdout_suppress(self):

        """Function:  test_stdout_suppress

        Description:  Test with standard out suppressed.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_std(
                self.outdata, args=self.args2, suf=self.primary),
            self.status)

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo):

        """Function:  test_mongo

        Description:  Test with writing to mongo.

        Arguments:

        """

        mock_mongo.return_value = self.conn

        self.assertEqual(
            mongo_rep_admin.process_std(
                self.outdata, class_cfg="mongocfg", db_tbl=self.db_tbl,
                args=self.args2, suf=self.primary), self.status)

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
            mongo_rep_admin.process_std(
                self.outdata, ofile="Filename", args=self.args3,
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
            mongo_rep_admin.process_std(
                self.outdata, ofile="Filename", args=self.args2,
                suf=self.primary), self.status)

    def test_email_mailx(self):

        """Function:  test_email_mailx

        Description:  Test with email option using mailx.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_std(
                self.outdata, mail=self.mail, args=self.args2a,
                suf=self.primary), self.status)

    def test_email(self):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.process_std(
                self.outdata, mail=self.mail, args=self.args2a,
                suf=self.primary), self.status)


if __name__ == "__main__":
    unittest.main()
