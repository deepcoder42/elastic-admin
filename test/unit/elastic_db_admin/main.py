#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in elastic_db_admin.py.

    Usage:
        test/unit/elastic_db_admin/main.py

    Arguments:
        None

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
import elastic_db_admin
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_help_true -> Test with help_func returns True.
        test_help_false ->  Test with help_func returns False.
        test_require_true -> Test with arg_require returns True.
        test_require_false -> Test with arg_require returns False.
        test_xor_dict_false -> Test with arg_xor_dict returns False.
        test_xor_dict_true -> Test with arg_xor_dict returns True.
        test_con_req_or_false -> Test with arg_cond_req_or returns False.
        test_con_req_or_true -> Test with arg_cond_req_or returns True.
        test_dir_chk_crt_true -> Test with arg_dir_chk_crt returns True.
        test_dir_chk_crt_false -> Test with arg_dir_chk_crt returns False.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args = {"-c": "config_file", "-d": "config_dir", "-R": True}

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:
            mock_arg -> Mock Ref:  elastic_db_admin.arg_parser.arg_parse2
            mock_help -> Mock Ref:  elastic_db_admin.gen_libs.help_func

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:
            mock_arg -> Mock Ref:  elastic_db_admin.arg_parser
            mock_help -> Mock Ref:  elastic_db_admin.gen_libs.help_func

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.arg_parser")
    def test_require_true(self, mock_arg, mock_help):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:
            mock_arg -> Mock Ref:  elastic_db_admin.arg_parser
            mock_help -> Mock Ref:  elastic_db_admin.gen_libs.help_func

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.arg_parser")
    def test_require_false(self, mock_arg, mock_help):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:
            mock_arg -> Mock Ref:  elastic_db_admin.arg_parser
            mock_help -> Mock Ref:  elastic_db_admin.gen_libs.help_func

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.arg_parser")
    def test_dir_chk_crt_true(self, mock_arg, mock_help):

        """Function:  test_dir_chk_crt_true

        Description:  Test with arg_dir_chk_crt returns True.

        Arguments:
            mock_arg -> Mock Ref:  elastic_db_admin.arg_parser
            mock_help -> Mock Ref:  elastic_db_admin.gen_libs.help_func

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(elastic_db_admin.main())

    @mock.patch("elastic_db_admin.run_program")
    @mock.patch("elastic_db_admin.gen_libs.help_func")
    @mock.patch("elastic_db_admin.arg_parser")
    def test_dir_chk_crt_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_dir_chk_crt_false

        Description:  Test with arg_dir_chk_crt returns False.

        Arguments:
            mock_arg -> Mock Ref:  elastic_db_admin.arg_parser
            mock_help -> Mock Ref:  elastic_db_admin.gen_libs.help_func
            mock_run -> Mock Ref:  elastic_db_admin.run_program

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(elastic_db_admin.main())


if __name__ == "__main__":
    unittest.main()
