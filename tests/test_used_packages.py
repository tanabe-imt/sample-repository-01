import sys
from unittest import TestCase

import numpy as np
import openpyxl


class UsedPackagesTests(TestCase):
    def test_python_version_01(self):
        self.assertTrue(sys.version.startswith("3.9.12"))

    def test_numpy_version_01(self):
        self.assertEqual(np.__version__, "1.21.6")

    def test_openpyxl_version_01(self):
        self.assertEqual(openpyxl.__version__, "3.0.9")
