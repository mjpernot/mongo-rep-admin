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
import mock

# Local
sys.path.append(os.getcwd())
import mongo_rep_admin                          # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_cond_req
        arg_dir_chk
        arg_file_chk
        arg_require
        arg_valid_val
        arg_parse2

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}
        self.opt_val = None
        self.multi_val = None
        self.do_parse = None
        self.file_perm_chk = None
        self.file_crt = None
        self.arg_file_chk2 = True
        self.opt_valid_val = None
        self.arg_valid_val2 = True
        self.opt_req = None
        self.opt_req2 = True
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.argparse2 = True

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_file_chk(self, file_perm_chk, file_crt):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk
        self.file_crt = file_crt

        return self.arg_file_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def arg_valid_val(self, opt_valid_val):

        """Method:  arg_valid_val

        Description:  Method stub holder for gen_class.ArgParser.arg_valid_val.

        Arguments:

        """

        self.opt_valid_val = opt_valid_val

        return self.arg_valid_val2

    def arg_parse2(self):

        """Method:  arg_parse2

        Description:  Method stub holder for gen_class.ArgParser.arg_parse2.

        Arguments:

        """

        return self.argparse2


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_arg_parse2_false
        test_arg_parse2_true
        test_help_true
        test_help_false
        test_arg_req_false
        test_arg_req_true
        test_arg_cond_false
        test_arg_cond_true
        test_arg_dir_false
        test_arg_dir_true
        test_arg_file_false
        test_arg_file_true
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {"-c": "CfgFile", "-d": "CfgDir", "-C": True}

    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_parse2_false(self, mock_arg):

        """Function:  test_arg_parse2_false

        Description:  Test arg_parse2 returns false.

        Arguments:

        """

        self.args.argparse2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_parse2_true(self, mock_arg, mock_help):

        """Function:  test_arg_parse2_true

        Description:  Test arg_parse2 returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_cond_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_cond_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_dir_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_file_false(self, mock_arg, mock_help):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.run_program")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_arg_file_true(self, mock_arg, mock_help, mock_run):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_rep_admin.main())

    @mock.patch("mongo_rep_admin.run_program")
    @mock.patch("mongo_rep_admin.gen_libs.help_func")
    @mock.patch("mongo_rep_admin.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_run):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_rep_admin.main())


if __name__ == "__main__":
    unittest.main()
