# Classification (U)

"""Program:  prt_rep_stat.py

    Description:  Unit testing of prt_rep_stat in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/prt_rep_stat.py

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


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.repset = "RepsetName"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_prt_rep_stat

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args.args_array = {"-T": "TimeLag"}
        self.status = (True, None)

    @mock.patch("mongo_rep_admin.chk_rep_stat")
    def test_prt_rep_stat(self, mock_stat):

        """Function:  test_prt_rep_stat

        Description:  Test prt_rep_stat function.

        Arguments:

        """

        mock_stat.return_value = True

        self.assertEqual(
            mongo_rep_admin.prt_rep_stat(
                self.server, self.args), self.status)


if __name__ == "__main__":
    unittest.main()
