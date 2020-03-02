import os
import unittest

from mdltools import *
from mdltools.vvd_struct import *
from mdltools.parser import *


class ParseVvdTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_vvd(self):
        with open('/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.vvd', "rb") as f:
            results = vertexFileHeader_t.parse_stream(f)
            with open('/mnt/work/source_misc/allmodels/bots/heavy/reconstructed.vvd', 'wb') as w:
                w.write(vertexFileHeader_t.build(results))
        self.assertTrue(True)

    def test_parse_vvd(self):
        vvd = VvdParse(
            '/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.vvd')
        self.assertTrue(vvd)
