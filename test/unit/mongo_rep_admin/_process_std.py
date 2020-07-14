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
        test_std_out -> Test standard out format print.
        test_stdout_suppress -> Test with standard out suppressed.
        # test_json_stdout -> Test with JSON format to standard out.
        # test_mongo -> Test with writing to mongo.
        # test_file_append -> Test with writing to file in append mode.
        # test_file -> Test with writing to file.
        # test_email -> Test with email option.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.primary = "primary"
        self.outdata = {
            "application": "Mongo Replication",
            "master": "mongo1:27017",
            "repSet": "spock",
            "asOf": "2020-07-13 11:51:21",
            "slaves": [{"lagTime": 0,
                        "syncTo": "2020-07-13 10:51:19",
                        "name": "mongo2:27017"},
                       {"lagTime": 10,
                        "syncTo": "2020-07-13 10:51:09",
                        "name": "mongo3:27017"}]}
        self.args_array = {}
        self.args_array2 = {"-z": True}
        #self.args_array3 = {"-z": True, "-a": True}
        #self.args_array4 = {"-z": True, "-f": True}

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test standard out format print.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_rep_admin._process_std(
                self.outdata, args_array=self.args_array, suf=self.primary))

    def test_stdout_suppress(self):

        """Function:  test_stdout_suppress

        Description:  Test with standard out suppressed.

        Arguments:

        """

        self.assertFalse(mongo_rep_admin._process_std(
            self.outdata, args_array=self.args_array2, suf=self.primary))

    @unittest.skip("not yet implemented")
    @mock.patch("mongo_rep_admin.gen_libs.display_data")
    def test_json_stdout(self, mock_prt):

        """Function:  test_json_stdout

        Description:  Test with JSON format to standard out.

        Arguments:

        """

        self.assertFalse(mongo_rep_admin._process_std(
            self.outdata, args_array=self.args_array2))

    @mock.patch("mongo_rep_admin.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo):

        """Function:  test_mongo

        Description:  Test with writing to mongo.

        Arguments:

        """

        mock_mongo.return_value = True

        self.assertFalse(mongo_rep_admin._process_std(
            self.outdata, class_cfg="mongocfg", db_tbl="db:tbl",
            args_array=self.args_array2))

    @unittest.skip("not yet implemented")
    @mock.patch("mongo_rep_admin.gen_libs.write_file")
    def test_file_append(self, mock_file):

        """Function:  test_file_append

        Description:  Test with writing to file in append mode.

        Arguments:

        """

        mock_file.return_value = True

        self.assertFalse(mongo_rep_admin._process_std(
            self.outdata, ofile="Filename", args_array=self.args_array3))

    @unittest.skip("not yet implemented")
    @mock.patch("mongo_rep_admin.gen_libs.write_file")
    def test_file(self, mock_file):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertFalse(mongo_rep_admin._process_std(
            self.outdata, ofile="Filename", args_array=self.args_array))

    @unittest.skip("not yet implemented")
    def test_email(self):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        self.assertFalse(mongo_rep_admin._process_std(
            self.outdata, mail=self.mail, args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
