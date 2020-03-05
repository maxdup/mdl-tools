import os
import unittest

from mdltools import *
from mdltools.phy_struct import *
from mdltools.parser import *


class ParsePhyTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_phy(self):
        with open('/mnt/work/source_misc/allmodels/props_forest/rock003.phy', "rb") as f:
            results = phyheader_t.parse_stream(f)
            print(results)
            with open('/mnt/work/source_misc/allmodels/props_forest/rock003_re.phy', 'wb') as w:
                w.write(phyheader_t.build(results))
        with open('/mnt/work/source_misc/allmodels/props_forest/dove.phy', "rb") as f:
            results = phyheader_t.parse_stream(f)
            print(results)
            with open('/mnt/work/source_misc/allmodels/props_forest/dove_re.phy', 'wb') as w:
                w.write(phyheader_t.build(results))
        with open('/mnt/work/source_misc/allmodels/props_forest/cliff_wall_10.phy', "rb") as f:
            results = phyheader_t.parse_stream(f)
            print(results)
            with open('/mnt/work/source_misc/allmodels/props_forest/cliff_wall_10_re.phy', 'wb') as w:
                w.write(phyheader_t.build(results))
        self.assertTrue(True)

    def test_parse_phy(self):
        phy = PhyParse(
            '/mnt/work/source_misc/allmodels/bots/heavy/bot_heavy.phy')
        self.assertTrue(phy)
