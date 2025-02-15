import os
import unittest
from isatools.convert import sampletab2isatab
from isatools.tests import utils
import tempfile
import shutil

SLOW_TESTS = int(os.getenv('SLOW_TESTS', '0'))


def setUpModule():
    if not os.path.exists(utils.DATA_DIR):
        raise FileNotFoundError("Could not fine test data directory in {0}. Ensure you have cloned the ISAdatasets "
                                "repository using "
                                "git clone -b tests --single-branch git@github.com:ISA-tools/ISAdatasets {0}"
                                .format(utils.DATA_DIR))


class TestSampleTab2IsaTab(unittest.TestCase):

    def setUp(self):
        self._tab_dir = utils.TAB_DATA_DIR
        self._sampletab_dir = utils.SAMPLETAB_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_sampletab2isatab_test_1(self):
        with open(os.path.join(self._sampletab_dir, "test1.txt")) as sampletab_fp:
            sampletab2isatab.convert(source_sampletab_fp=sampletab_fp, target_dir=self._tmp_dir)

    def test_sampletab2isatab_test_2(self):
        with open(os.path.join(self._sampletab_dir, "test2.txt")) as sampletab_fp:
            sampletab2isatab.convert(source_sampletab_fp=sampletab_fp, target_dir=self._tmp_dir)

    @unittest.skipIf(not SLOW_TESTS, "slow")
    def test_sampletab2isatab_GSB_3(self):
        with open(os.path.join(self._sampletab_dir, "GSB-3.txt")) as sampletab_fp:
            sampletab2isatab.convert(source_sampletab_fp=sampletab_fp, target_dir=self._tmp_dir)

    @unittest.skipIf(not SLOW_TESTS, "slow")
    def test_sampletab2isatab_GSB_537(self):
        with open(os.path.join(self._sampletab_dir, "GSB-537.txt")) as sampletab_fp:
            sampletab2isatab.convert(source_sampletab_fp=sampletab_fp, target_dir=self._tmp_dir)

    @unittest.skip("slow")
    def test_sampletab2isatab_GSB_718(self):
        with open(os.path.join(self._sampletab_dir, "GSB-718.txt")) as sampletab_fp:
            sampletab2isatab.convert(source_sampletab_fp=sampletab_fp, target_dir=self._tmp_dir)
