from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import int
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: E402
from .mdl import *  # NOQA: E402


def readcstr(f):
    return ''.join(iter(lambda: f.read(1).decode('ascii'), '\x00'))


mstudiobbox_t = Struct(
    'bone' / Int32sl,
    'group' / Int32sl,
    'bbmin' / Float32l[3],
    'bbmax' / Float32l[3],
    'szhitboxnameindex' / Int32sl,
    'unused' / Int32sl[8],
)

mstudiohitboxset_t = Struct(
    'sznameindex' / Int32sl,
    'numhitboxes' / Int32sl,
    'hitboxindex' / Int32sl,

    # 'hitboxes' / Pointer(this.hitboxindex,
    #                     mstudiobbox_t[this.numhitboxes]),
)
'''
mstudiovertex_t = Struct(
    mstudioboneweight_t m_BoneWeights;
    Vector              m_vecPosition;
    Vector              m_vecNormal;
    Vector2D            m_vecTexCoord;
    mstudiovertex_t() {}
)
'''

mstudiocdtexture_t = Struct(
    'nameoffset' / Int32sl,

    'name' / Pointer(this.nameoffset, CString('ascii'))
)


mstudiotexture_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'flags' / Int32sl,
    'used' / Int32sl,
    'unused1' / Int32sl,
    'unused' / Int32sl[12],

    'name' / Pointer(this.sznameindex + this._.textureindex +
                     (this.i*64), CString('ascii'))
)

mstudiomodel_t = Struct(

)

mstudiobodyparts_t = Struct(
    'sznameindex' / Int32sl,
    'nummodels' / Int32sl,
    'base' / Int32sl,
    'modelindex' / Int32sl,
    'name' / Pointer(this.sznameindex + this._.bodypartindex, CString('ascii'))
)

mstudiomouth_t = Struct(
    'bone' / Int32sl,
    'forward' / Float32l[3],
    'flexdesc' / Int32sl,
)

mstudioposeparamdesc_t = Struct(
    'sznameindex' / Int32sl,
    'flags' / Int32sl,
    'start' / Float32l,
    'end' / Float32l,
    'loop' / Float32l,
)

mstudiomovement_t = Struct(
    'endframe' / Int32sl,
    'motionflags' / Int32sl,
    'v0' / Float32l,
    'v1' / Float32l,
    'angle' / Float32l,
    'vector' / Float32l[3],
    'position' / Float32l[3],
)

mstudioseqdesc_t = Struct(
    'baseptr' / Int32sl,
    'szlabelindex' / Int32sl,
    'szactivitynameindex' / Int32sl,
    'flags' / Int32sl,
    'activity' / Int32sl,
    'actweight' / Int32sl,
    'numevents' / Int32sl,
    'eventindex' / Int32sl,
    'bbmin' / Float32l[3],
    'bbmax' / Float32l[3],
    'numblends' / Int32sl,
    'animindexindex' / Int32sl,
    'movementindex' / Int32sl,
    'groupsize' / Int32sl[2],
    'paramindex' / Int32sl[2],
    'paramstart' / Float32l[2],
    'paramend' / Float32l[2],
    'paramparent' / Int32sl,
    'fadeintime' / Float32l[2],
    'fadeouttime' / Float32l[2],
    'localentrynode' / Int32sl,
    'localexitnode' / Int32sl,
    'nodeflags' / Int32sl,
    'entryphase' / Float32l,
    'exitphase' / Float32l,
    'lastframe' / Float32l,
    'nextseq' / Int32sl,
    'pose' / Int32sl,
    'numikrules' / Int32sl,
    'numautolayers' / Int32sl,
    'autolayerindex' / Int32sl,
    'weightlistindex' / Int32sl,
    'posekeyindex' / Int32sl,
    'numiklocks' / Int32sl,
    'iklockindex' / Int32sl,
    'keyvalueindex' / Int32sl,
    'keyvaluesize' / Int32sl,
    'cycleposeindex' / Int32sl,
    'unused' / Int32sl[7],
)

mstudiobone_t = Struct(
    'sznameindex' / Int32sl,
    'parent' / Int32sl,
    'bonecontroller' / Int32sl[6],
    'pos' / Float32l[3],
    'quat' / Float32l[4],
    'rot' / Float32l[3],
    'posscale' / Float32l[3],
    'rotscale' / Float32l[3],
    'poseToBone' / Float32l[12],
    'qAlignment' / Float32l[4],
    'flags' / Int32sl,
    'proctype' / Int32sl,
    'procindex' / Int32sl,
    'surfacepropidx' / Int32sl,
    'contents' / Int32sl,
    'unused' / Int32sl[8],
)

mstudiolinearbone_t = Struct(
    'numbones' / Int32sl,
    'flagsindex' / Int32sl,
    'parentindex' / Int32sl,
    'posindex' / Int32sl,
    'quatindex' / Int32sl,
    'rotindex' / Int32sl,
    'posetoboneindex' / Int32sl,
    'posscaleindex' / Int32sl,
    'rotscaleindex' / Int32sl,
    'qalignmentindex' / Int32sl,
    'unused' / Int32sl[6],
)

mstudiobonecontroller_t = Struct(
    'bone' / Int32sl,
    'type' / Int32sl,
    'start' / Float32l,
    'end' / Float32l,
    'rest' / Int32sl,
    'inputfield' / Int32sl,
    'unused' / Int32sl[8],
)

mstudioflexdesc_t = Struct(
    'szFACSindex' / Int32sl,
)

mstudioflexcontroller_t = Struct(
    'sztypeindex' / Int32sl,
    'sznameindex' / Int32sl,
    'localToGlobal' / Int32sl,
    'min' / Float32l,
    'max' / Float32l,
)

mstudioflexcontrollerui_t = Struct(

    'sznameindex' / Int32sl,
    'szindex0' / Int32sl,
    'szindex1' / Int32sl,
    'szindex2' / Int32sl,
    'remaptype' / Int8ul,
    'stereo' / Flag,
    'unused' / Int8ub[2],
)

mstudioflexrule_t = Struct(
    'flex' / Int32sl,
    'numops' / Int32sl,
    'opindex' / Int32sl,
)

mstudiobbox_t = Struct(
    'bone' / Int32sl,
    'group' / Int32sl,
    'bbmin' / Float32l[3],
    'bbmax' / Float32l[3],
    'szhitboxnameindex' / Int32sl,
    'unused' / Int32sl[8],
)

mstudioevent_t = Struct(
    'cycle' / Float32l,
    'event' / Int32sl,
    'type' / Int32sl,
    'options[64]' / PaddedString(64, "ascii"),
    'szeventindex' / Int32sl,
)

mstudioattachment_t = Struct(
    'sznameindex' / Int32sl,
    'flags' / Int32ul,
    'localbone' / Int32sl,
    'local' / Float32l[12],
    'unused' / Int32sl[8],
)
mstudioikchain_t = Struct(
    'sznameindex' / Int32sl,
    'linktype' / Int32sl,
    'numlinks' / Int32sl,
    'linkindex' / Int32sl,
)

mstudioiklock_t = Struct(
    'chain' / Int32sl,
    'flPosWeight' / Float32l,
    'flLocalQWeight' / Float32l,
    'flags' / Int32sl,
    'unused' / Int32sl[4],
)

mstudioikrule_t = Struct(
    'index' / Int32sl,
    'type' / Int32sl,
    'chain' / Int32sl,
    'bone' / Int32sl,
    'slot' / Int32sl,
    'height' / Float32l,
    'radius' / Float32l,
    'floor' / Float32l,
    'pos' / Float32l[3],
    'q' / Float32l[4],
    'compressedikerrorindex' / Int32sl,
    'unused2' / Int32sl,
    'iStart' / Int32sl,
    'ikerrorindex' / Int32sl,
    'start' / Float32l,
    'peak' / Float32l,
    'tail' / Float32l,
    'end' / Float32l,
    'unused3' / Float32l,
    'contact' / Float32l,
    'drop' / Float32l,
    'top' / Float32l,
    'unused6' / Int32sl,
    'unused7' / Int32sl,
    'unused8' / Int32sl,
    'szattachmentindex' / Int32sl,
    'unused' / Int32sl[7],
)

mstudiolocalhierarchy_t = Struct(
    'iBone' / Int32sl,
    'iNewParent' / Int32sl,
    'start' / Float32l,
    'peak' / Float32l,
    'tail' / Float32l,
    'end' / Float32l,
    'iStart' / Int32sl,
    'localanimindex' / Int32sl,
    'unused' / Int32sl[4],
)

mstudioanimblock_t = Struct(
    'datastart' / Int32sl,
    'dataend' / Int32sl,
)
mstudioanimsections_t = Struct(
    'animblock' / Int32sl,
    'animindex' / Int32sl,
)

mstudioanimdesc_t = Struct(
    'baseptr' / Int32sl,
    'sznameindex' / Int32sl,
    'fps' / Float32l,
    'flags' / Int32sl,
    'numframes' / Int32sl,
    'nummovements' / Int32sl,
    'movementindex' / Int32sl,
    'unused1' / Int32sl[6],
    'animblock' / Int32sl,
    'animindex' / Int32sl,
    'numikrules' / Int32sl,
    'ikruleindex' / Int32sl,
    'animblockikruleindex' / Int32sl,
    'numlocalhierarchy' / Int32sl,
    'localhierarchyindex' / Int32sl,
    'sectionindex' / Int32sl,
    'sectionframes' / Int32sl,
    'zeroframespan' / Int16sl,
    'zeroframecount' / Int16sl,
    'zeroframeindex' / Int32sl,
)

mstudioautolayer_t = Struct(
    'iSequence' / Int16sl,
    'iPose' / Int16sl,
    'flags' / Int32sl,
    'start' / Float32l,
    'peak' / Float32l,
    'tail' / Float32l,
    'end' / Float32l,
)

studiohdr2_t = Struct(
    'numsrcbonetransform' / Int32sl,
    'srcbonetransformindex' / Int32sl,
    'illumpositionattachmentindex' / Int32sl,
    'flMaxEyeDeflection' / Float32l,
    'linearboneindex' / Int32sl,
    'sznameindex' / Int32sl,
    'm_nBoneFlexDriverCount' / Int32sl,
    'm_nBoneFlexDriverIndex' / Int32sl,
)
studiohdr_t = Struct(
    'id' / Int32sl,
    'version' / Int32sl,
    'checksum' / Int32sl,
    'name' / PaddedString(64, "ascii"),
    'dataLength' / Int32sl,
    'eyeposition' / Float32l[3],
    'illumposition' / Float32l[3],
    'hull_min' / Float32l[3],
    'hull_max' / Float32l[3],
    'view_bbmin' / Float32l[3],
    'view_bbmax' / Float32l[3],
    'flags' / Int32sl,

    'numbones' / Int32sl,
    'boneindex' / Int32sl,

    'RemapSeqBone' / Int32sl,  # todo?
    'RemapAnimBone' / Int32sl,  # todo?

    'numbonecontrollers' / Int32sl,  # doesn't look right
    'bonecontrollerindex' / Int32sl,  # doesn't look right
    'numhitboxsets' / Int32sl,
    'hitboxsetindex' / Int32sl,

    'numlocalanim' / Int32sl,
    'localanimindex' / Int32sl,
    'numlocalseq' / Int32sl,
    'localseqindex' / Int32sl,

    'numtextures' / Int32sl,
    'textureindex' / Int32sl,
    'numcdtextures' / Int32sl,
    'cdtextureindex' / Int32sl,
    'numskinref' / Int32sl,
    'numskinfamilies' / Int32sl,
    'skinindex' / Int32sl,
    'numbodyparts' / Int32sl,
    'bodypartindex' / Int32sl,
    'numlocalattachments' / Int32sl,
    'localattachmentindex' / Int32sl,
    'numlocalnodes' / Int32sl,
    'localnodeindex' / Int32sl,
    'localnodenameindex' / Int32sl,
    'numflexdesc' / Int32sl,
    'flexdescindex' / Int32sl,
    'numflexcontrollers' / Int32sl,
    'flexcontrollerindex' / Int32sl,
    'numflexrules' / Int32sl,
    'flexruleindex' / Int32sl,
    'numikchains' / Int32sl,
    'ikchainindex' / Int32sl,
    'nummouths' / Int32sl,
    'mouthindex' / Int32sl,
    'numlocalposeparameters' / Int32sl,
    'localposeparamindex' / Int32sl,
    'surfacepropindex' / Int32sl,
    'keyvalueindex' / Int32sl,
    'keyvaluesize' / Int32sl,
    'numlocalikautoplaylocks' / Int32sl,
    'localikautoplaylockindex' / Int32sl,
    'mass' / Float32l,
    'contents' / Int32sl,
    'numincludemodels' / Int32sl,
    'includemodelindex' / Int32sl,
    'szanimblocknameindex' / Int32sl,
    'numanimblocks' / Int32sl,
    'animblockindex' / Int32sl,
    'bonetablebynameindex' / Int32sl,
    'pVertexBase' / Int32sl,
    'pIndexBase' / Int32sl,
    'constdirectionallightdot' / Byte,
    'rootLOD' / Byte,
    'numAllowedRootLODs' / Byte,
    'unused1' / Byte,
    'unused4' / Int32sl,
    'numflexcontrollerui' / Int32sl,
    'flexcontrolleruiindex' / Int32sl,
    'flVertAnimFixedPointScale' / Float32l,
    'unused3' / Int32sl,
    'test1' / Int32sl,
    'test2' / Int32sl,
    'studiohdr2index' / Int32sl,
    'unused2' / Int32sl,

    'studiohdr2_t' / Pointer(this.studiohdr2index, studiohdr2_t),
    'textures' / Pointer(this.textureindex,
                         mstudiotexture_t[this.numtextures]),
    'cdtextures' / Pointer(this.cdtextureindex,
                           mstudiocdtexture_t[this.numcdtextures]),
    'bodyparts' / Pointer(this.bodypartindex,
                          mstudiobodyparts_t[this.numbodyparts]),
    'bones' / Pointer(this.boneindex, mstudiobone_t[this.numbones]),

    'bonecontrollers' / Pointer(this.bonecontrollerindex,
                                mstudiobonecontroller_t[this.numbonecontrollers]),
    'hitboxsets' / Pointer(this.hitboxsetindex,
                           mstudiohitboxset_t[this.numhitboxsets]),

)


def MdlParse(filename):
    mdl = Mdl()
    with open(filename, "rb") as f:
        results = studiohdr_t.parse_stream(f)
        print(results)
        print(studiohdr_t.sizeof())
    return mdl
