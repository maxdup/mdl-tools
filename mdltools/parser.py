from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import dict
from builtins import int
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: E402

from .mdl import *  # NOQA: E402
from .vvd import *  # NOQA: E402
from .vtx import *  # NOQA: E402
from .phy import *  # NOQA: E402

from .mdl_struct import *  # NOQA: E402
from .vvd_struct import *  # NOQA: E402
from .vtx_struct import *  # NOQA: E402
from .phy_struct import *  # NOQA: E402


def MdlParse(filename):
    mdl = Mdl()
    with open(filename, "rb") as f:
        try:
            results = studiohdr_t.parse_stream(f)
            # print(results)
        except Exception as e:
            print(e)
    return mdl


def VvdParse(filename):
    vvd = Vvd()
    with open(filename, "rb") as f:
        try:
            results = vertexFileHeader_t.parse_stream(f)
            # print(results)
        except Exception as e:
            print(e)
    return vvd


def PhyParse(filename):
    phy = Phy()
    with open(filename, "rb") as f:
        try:
            results = phyheader_t.parse_stream(f)
            # print(results)
        except Exception as e:
            print(e)
    return phy


def VtxParse(filename):
    vtx = Vtx()
    with open(filename, "rb") as f:
        try:
            results = vtxheader_t.parse_stream(f)
            # print(results)
        except Exception as e:
            print(e)
    return vtx
