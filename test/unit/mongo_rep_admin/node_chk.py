#!/usr/bin/python
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
        create_subject -> Stub method holder for Mail.create_subject.
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

    def send_mail(self):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.
        adm_cmd -> Stub holder for mongo_class.Server.adm_cmd method.

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
        setUp -> Initialize testing environment.
        test_mail_no_subj -> Test with mail and no subject set.
        test_mail_fail -> Test with mail and failure.
        test_flatten_fail -> Test with flatten JSON and failure.
        test_suppression_fail -> Test with standard suppression and failure.
        test_message_fail -> Test with message failure check.
        test_state_fail -> Test with state failure check.
        test_health_fail -> Test with health failure check.
        test_good -> Test with good status return on all checks.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args_array = {}
        self.args_array2 = {"-z": True}
        self.args_array3 = {"-f": True}
        self.status = (True, None)

    def test_mail_no_subj(self):

        """Function:  test_mail_no_subj

        Description:  Test with mail and no subject set.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8
        self.mail.subj = None

        self.assertEqual(mongo_rep_admin.node_chk(
            self.server, self.args_array2, mail=self.mail), self.status)

    def test_mail_fail(self):

        """Function:  test_mail_fail

        Description:  Test with mail and failure.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8

        self.assertEqual(mongo_rep_admin.node_chk(
            self.server, self.args_array2, mail=self.mail), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_flatten_fail(self):

        """Function:  test_flatten_fail

        Description:  Test with flatten JSON and failure.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args_array3), self.status)

    def test_suppression_fail(self):

        """Function:  test_suppression_fail

        Description:  Test with standard suppression and failure.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args_array2), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_message_fail(self):

        """Function:  test_message_fail

        Description:  Test with message failure check.

        Arguments:

        """

        self.server.status["members"][0]["infoMessage"] = "Error Message Here"

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args_array), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_state_fail(self):

        """Function:  test_state_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.server.status["members"][0]["state"] = 8

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args_array), self.status)

    @mock.patch("mongo_rep_admin.gen_libs.display_data",
                mock.Mock(return_value=True))
    def test_health_fail(self):

        """Function:  test_health_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.server.status["members"][0]["health"] = 0.0

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args_array), self.status)

    def test_good(self):

        """Function:  test_good

        Description:  Test with good status return on all checks.

        Arguments:

        """

        self.assertEqual(
            mongo_rep_admin.node_chk(
                self.server, self.args_array), self.status)


if __name__ == "__main__":
    unittest.main()
