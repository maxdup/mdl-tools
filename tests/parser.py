import os
import unittest

from mdltools import *


class ParseTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_parse(self):
        # mdl = MdlParse(
        #    '/mnt/work/source_misc/allmodels/props_forest/rock004.mdl')
        mdl = MdlParse(
            '/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.mdl')
        self.assertTrue(mdl)
