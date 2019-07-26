#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_rep_admin.py.

    Usage:
        test/unit/mongo_rep_admin/run_program.py

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


def prt_rep_stat(self, repset, args_array):

    """Function:  prt_rep_stat

    Description:  Stub holder for mongo_rep_admin.prt_rep_stat function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    return True


class Coll(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.Coll.connect method.
        coll_cnt -> Stub holder for mongo_class.Coll.coll_cnt method.
        coll_find1 -> Stub holder for mongo_class.Coll.coll_find1 method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.coll_cnt = 1

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True

    def coll_cnt(self):

        """Method:  coll_cnt

        Description:  Stub holder for mongo_class.Coll.coll_cnt method.

        Arguments:

        """

        return self.coll_cnt

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return {"_id": "RepSetName"}


class RepSet(object):

    """Class:  RepSet

    Description:  Class stub holder for mongo_class.RepSet class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.RepSet.connect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.passwd = "pwd"
        self.host = "host"
        self.port = 27017
        self.auth = "auth"
        self.conf_file = "conffile"

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.RepSet.connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_replication -> Test with replication setup.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = {"name": "name", "user": "user", "passwd": "pwd",
                       "host": "host", "port": 27017, "auth": "auth",
                       "conf_file": "conffile"}

        self.repset = RepSet()
        self.coll = Coll()
        self.args_array = {"-T": True}
        self.func_dict = {"-P": fetch_priority, "-T": prt_rep_stat}

    @mock.patch("mongo_rep_admin.mongo_class.RepSet")
    @mock.patch("mongo_rep_admin.cmds_gen.disconnect")
    @mock.patch("mongo_rep_admin.mongo_class.Coll")
    def test_replication(self, mock_coll, mock_cmd, mock_repset):

        """Function:  test_replication

        Description:  Test with replication setup.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_cmd.return_value = True
        mock_repset.return_value = self.repset

        self.assertFalse(mongo_rep_admin.run_program(self.args_array,
                                                     self.func_dict))


if __name__ == "__main__":
    unittest.main()
