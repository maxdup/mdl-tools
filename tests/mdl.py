import os
import unittest

from mdltools import *
from mdltools.mdl_struct import *
from mdltools.parser import *


class ParseMdlTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_mdl(self):
        with open('/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.mdl', "rb") as f:
            results = studiohdr_t.parse_stream(f)
            with open('/mnt/work/source_misc/allmodels/bots/heavy/reconstructed.mdl', 'wb') as w:
                w.write(studiohdr_t.build(results))
        self.assertTrue(True)

    def test_parse_mdl(self):
        mdl = MdlParse(
            '/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.mdl')
        self.assertTrue(mdl)
