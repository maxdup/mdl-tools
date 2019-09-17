from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import open
from future import standard_library
standard_library.install_aliases()

from struct import *  # NOQA: E402
from .mdl import *  # NOQA: E402


studiohdr_t = Struct('<iii64si3f3f3f3f3f3fi43if11icccc5i')


def MdlParse(filename):
    mdl = Mdl()
    with open(filename, "rb") as f:
        data = f.read(studiohdr_t.size)
        parsed = studiohdr_t.unpack(data)
    if data:
        mdl.id = parsed[0]
        mdl.version = parsed[1]
        mdl.checksum = parsed[2]
        mdl.name = parsed[3]
        mdl.dataLength = parsed[4]

        mdl.eyeposition = (parsed[5], parsed[6], parsed[7])
        mdl.illumposition = (parsed[8], parsed[9], parsed[10])

        mdl.hull_min = (parsed[11], parsed[12], parsed[13])
        mdl.hull_max = (parsed[14], parsed[15], parsed[16])

        mdl.view_bbmin = (parsed[17], parsed[18], parsed[19])
        mdl.view_bbmax = (parsed[20], parsed[21], parsed[22])

        mdl.flags = parsed[23]

        mdl.bone_count = parsed[24]
        mdl.bone_offset = parsed[25]

        mdl.bonecontroller_count = parsed[26]
        mdl.bonecontroller_offset = parsed[27]

        mdl.hitbox_count = parsed[28]
        mdl.hitbox_offset = parsed[29]

        mdl.localanim_count = parsed[30]
        mdl.localanim_offset = parsed[31]

        mdl.localseq_count = parsed[32]
        mdl.localseq_offset = parsed[33]

        mdl.activitylistversion = parsed[34]
        mdl.eventsindexed = parsed[35]

        mdl.texture_count = parsed[36]
        mdl.texture_offset = parsed[37]

        mdl.texturedir_count = parsed[38]
        mdl.texturedir_offset = parsed[39]

        mdl.skinreference_count = parsed[40]
        mdl.skinrfamily_count = parsed[41]
        mdl.skinreference_index = parsed[42]

        mdl.bodypart_count = parsed[43]
        mdl.bodypart_offset = parsed[44]

        mdl.attachment_count = parsed[45]
        mdl.attachment_offset = parsed[46]

        mdl.localnode_count = parsed[47]
        mdl.localnode_index = parsed[48]
        mdl.localnode_name_index = parsed[49]

        mdl.flexdesc_count = parsed[50]
        mdl.flexdesc_index = parsed[51]

        mdl.flexcontroller_count = parsed[52]
        mdl.flexcontroller_index = parsed[53]

        mdl.flexrules_count = parsed[54]
        mdl.flexrules_index = parsed[55]

        mdl.ikchain_count = parsed[56]
        mdl.ikchain_index = parsed[57]

        mdl.mouths_count = parsed[58]
        mdl.mouths_index = parsed[59]

        mdl.localposeparam_count = parsed[60]
        mdl.localposeparam_index = parsed[61]

        mdl.surfaceprop_index = parsed[62]

        mdl.keyvalue_index = parsed[63]
        mdl.keyvalue_count = parsed[64]
        mdl.iklock_count = parsed[65]
        mdl.iklock_index = parsed[66]

        mdl.mass = parsed[67]
        mdl.contents = parsed[68]

        mdl.includemodel_count = parsed[69]
        mdl.includemodel_index = parsed[70]

        mdl.virtualModel = parsed[71]

        mdl.animblocks_name_index = parsed[72]
        mdl.animblocks_count = parsed[73]
        mdl.animblocks_index = parsed[74]

        mdl.animblockModel = parsed[75]

        mdl.bonetablename_index = parsed[76]

        mdl.vertex_base = parsed[77]
        mdl.offset_base = parsed[78]

    return mdl
