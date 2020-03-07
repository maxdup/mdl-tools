import os
import unittest

from mdltools import *
from mdltools.vtx_struct import *
from mdltools.parser import *


class ParseVtxTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_vtx(self):
        with open('/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.sw.vtx', "rb") as f:
            # with open('/mnt/work/source_misc/allmodels/props_forest/rock004.sw.vtx', "rb") as f:
            results = vtxheader_t.parse_stream(f)
            print(results)
            with open('/mnt/work/source_misc/allmodels/bots/heavy/reconstructed.sw.vtx', 'wb') as w:
                # with open('/mnt/work/source_misc/allmodels/props_forest/reconstructed.sw.vtx', 'wb') as w:
                w.write(vtxheader_t.build(results))
        self.assertTrue(True)

    def test_parse_vvd(self):
        vtx = VtxParse(
            '/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.sw.vtx')
        self.assertTrue(vtx)
