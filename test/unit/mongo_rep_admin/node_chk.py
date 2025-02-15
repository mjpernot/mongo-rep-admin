# Classification (U)

"""Program:  node_chk.py

    Description:  Unit testing of node_chk in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/node_chk.py

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
        create_subject
        add_2_msg
        send_mail

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.lag_time = lag_time
        self.subj = "Test subject line"
        self.data = None

    def create_subject(self, subj):

        """Method:  create_subject

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.subj = subj

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

        self.repset = "RepsetName"
        self.cmd = None
        self.status = {"members":
                       [{"name": "MemberName", "health": 1.0, "state": 1,
                         "stateStr": None, "infoMessage": None}]}

    def adm_cmd(self, cmd):

        """Method:  adm_cmd

        Description:  Stub holder for mongo_class.Server.adm_cmd method.

        Arguments:
            (input) cmd -> Command.

        """

        self.cmd = cmd

        return self.status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mail_no_subj_mailx
        test_mail_no_subj
        test_mail_fail_mailx
        test_mail_fail
        test_flatten_fail
        test_suppression_fail
        test_message_fail
        test_state_fail
        test_health_fail
        test_good

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args2a = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {}
        self.args2.args_array = {"-z": True}
        self.args2a.args_array = {"-z": True, "-u": True}
        self.args3.args_array = {"-f": True}
        self.status = (True, None)

    def test_mail_no_subj_mailx(self):

        """Function:  test_mail_no_subj_mailx

        Description:  Test with mail and no subject set using mailx.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8
        self.mail.subj = None

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args2a, mail=self.mail), self.status)

    def test_mail_no_subj(self):

        """Function:  test_mail_no_subj

        Description:  Test with mail and no subject set.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8
        self.mail.subj = None

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args2, mail=self.mail), self.status)

    def test_mail_fail_mailx(self):

        """Function:  test_mail_fail_mailx

        Description:  Test with mail and failure using mailx.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args2a, mail=self.mail), self.status)

    def test_mail_fail(self):

        """Function:  test_mail_fail

        Description:  Test with mail and failure.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args2, mail=self.mail), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_flatten_fail(self):

        """Function:  test_flatten_fail

        Description:  Test with flatten JSON and failure.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(self.server, self.args3), self.status)

    def test_suppression_fail(self):

        """Function:  test_suppression_fail

        Description:  Test with standard suppression and failure.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(self.server, self.args2), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_message_fail(self):

        """Function:  test_message_fail

        Description:  Test with message failure check.

        Arguments:

        """

        self.server.status["members"][0]["infoMessage"] = "Error Message Here"

        self.assertEqual(
            mongo_rep_admin.node_chk(self.server, self.args), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_state_fail(self):

        """Function:  test_state_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8

        self.assertEqual(
            mongo_rep_admin.node_chk(self.server, self.args), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_health_fail(self):

        """Function:  test_health_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(self.server, self.args), self.status)

    def test_good(self):

        """Function:  test_good

        Description:  Test with good status return on all checks.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.node_chk(self.server, self.args), self.status)


if __name__ == "__main__":
    unittest.main()
