# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/main.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_help_false
        test_arg_req_true
        test_arg_req_false
        test_arg_cond_false
        test_arg_cond_true
        test_arg_dir_true
        test_arg_dir_false
        test_arg_file_true
        test_arg_file_false

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "CfgFile", "-d": "CfgDir", "-C": True}

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.arg_parser.arg_require")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_help_false(self, mock_arg, mock_help, mock_req):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.arg_parser.arg_require")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_arg_req_true(self, mock_arg, mock_help, mock_req):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.arg_parser.arg_cond_req")
    @mock.patch("mongo_rep_admin.arg_parser.arg_require")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_arg_req_false(self, mock_arg, mock_help, mock_req, mock_cond):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.arg_parser.arg_cond_req")
    @mock.patch("mongo_rep_admin.arg_parser.arg_require")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_arg_cond_false(self, mock_arg, mock_help, mock_req, mock_cond):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.arg_parser.arg_dir_chk_crt")
    @mock.patch("mongo_rep_admin.arg_parser.arg_file_chk")
    @mock.patch("mongo_rep_admin.arg_parser.arg_require")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_arg_cond_true(self, mock_arg, mock_help, mock_req, mock_cond,
                           mock_dir):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = True
        mock_dir.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.arg_parser.arg_dir_chk_crt")
    @mock.patch("mongo_rep_admin.arg_parser.arg_file_chk")
    @mock.patch("mongo_rep_admin.arg_parser.arg_require")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser.arg_parse2")
    def test_arg_dir_true(self, mock_arg, mock_help, mock_req, mock_cond,
                          mock_dir):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = True
        mock_dir.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser")
    def test_arg_file_true(self, mock_arg, mock_help):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.run_program")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.arg_parser")
    def test_arg_file_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_file_chk.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_rep_admin.main())


if __name__ == "__main__":
    unittest.main()
