from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from struct import *  # NOQA: E402
from .mdl import *  # NOQA: E402


def readcstr(f):
    return ''.join(iter(lambda: f.read(1).decode('ascii'), '\x00'))


offset = Struct('i')
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

            # mstudiobone_t
            bone_count = parsed[24]
            bone_offset = parsed[25]
            mdl.bones = []

            f.seek(bone_offset)
            for b in range(0, bone_count):
                data = f.read(mstudiobone_t.size)
                parsed_data = mstudiobone_t.unpack(data)
                bone = make_mstudiobone_t(parsed_data)
                mdl.bones.append(bone)

            # mstudiobonecontroller_t
            bonecontroller_count = parsed[26]
            bonecontroller_offset = parsed[27]
            mdl.bonecontrollers = []

            f.seek(bonecontroller_offset)
            for b in range(0, bonecontroller_count):
                data = f.read(mstudiobonecontroller_t.size)
                parsed_data = mstudiobonecontroller_t.unpack(data)
                bonecontroller = make_mstudiobonecontroller_t(parsed_data)
                mdl.bonecontrollers.append(bone)

            # mstudiohitboxset_t
            hitbox_count = parsed[28]
            hitbox_offset = parsed[29]

            # mstudioanimdesc_t
            localanim_count = parsed[30]
            localanim_offset = parsed[31]

            # mstudioseqdesc_t
            mdl.localseq_count = parsed[32]
            mdl.localseq_offset = parsed[33]

            mdl.activitylistversion = parsed[34]
            mdl.eventsindexed = parsed[35]

            # mstudiotexture_t
            numtextures = parsed[36]
            textureindex = parsed[37]
            mdl.textures = []

            f.seek(textureindex)
            for b in range(0, numtextures):
                data = f.read(mstudiotexture_t.size)
                parsed_data = mstudiotexture_t.unpack(data)
                bone = make_mstudiotexture_t(parsed_data)
                mdl.textures.append(bone)

            for i in range(0, len(mdl.textures)):
                f.seek(textureindex + mdl.textures[i].sznameindex + i*64)
                mdl.textures[i].pszName = readcstr(f)

            # texture directories
            numcdtextures = parsed[38]
            cdtextureindex = parsed[39]
            cdoffsets = []
            mdl.cdtextures = []

            f.seek(cdtextureindex)
            for i in range(0, numcdtextures):
                data = f.read(offset.size)
                cdoffsets.append(offset.unpack(data)[0])
            for i in cdoffsets:
                f.seek(i)
                mdl.cdtextures.append(readcstr(f))

            # skin table
            numskinref = parsed[40]
            numskinrfamilies = parsed[41]
            skinindex = parsed[42]
            skintable = []
            tablelength = numskinref * numskinrfamilies
            tableformat = 'h' * tablelength

            f.seek(skinindex)
            data = f.read(calcsize(tableformat))
            parsed_data = unpack_from(tableformat, data)

            mdl.skintable = [[0]*numskinref]*numskinrfamilies
            for i in range(0, numskinrfamilies):
                for j in range(0, numskinref):
                    mdl.skintable[i][j] = parsed_data[numskinrfamilies*i + j]

            # mstudiobodyparts_t
            bodypart_count = parsed[43]
            bodypart_offset = parsed[44]
            mdl.bodyparts = []

            f.seek(bodypart_offset)
            for b in range(0, bodypart_count):
                data = f.read(mstudiobodyparts_t.size)
                parsed_data = mstudiobodyparts_t.unpack(data)
                bodypart = make_mstudiobodyparts_t(parsed_data)
                mdl.bodyparts.append(bodypart)

            # mstudioattachment_t
            attachment_count = parsed[45]
            attachment_offset = parsed[46]

            mdl.localnode_count = parsed[47]
            mdl.localnode_index = parsed[48]
            mdl.localnode_name_index = parsed[49]

            # mstudioflexdesc_t
            mdl.flexdesc_count = parsed[50]
            mdl.flexdesc_index = parsed[51]

            # mstudioflexcontroller_t
            mdl.flexcontroller_count = parsed[52]
            mdl.flexcontroller_index = parsed[53]

            # mstudioflexrule_t
            mdl.flexrules_count = parsed[54]
            mdl.flexrules_index = parsed[55]

            # mstudioikchain_t
            mdl.ikchain_count = parsed[56]
            mdl.ikchain_index = parsed[57]

            # mstudiomouth_t
            mouths_count = parsed[58]
            mouths_index = parsed[59]

            # mstudioposeparamdesc_t
            mdl.localposeparam_count = parsed[60]
            mdl.localposeparam_index = parsed[61]

            mdl.surfaceprop_index = parsed[62]

            mdl.keyvalue_index = parsed[63]
            mdl.keyvalue_count = parsed[64]

            # mstudioiklock_t
            mdl.iklock_count = parsed[65]
            mdl.iklock_index = parsed[66]

            mdl.mass = parsed[67]
            mdl.contents = parsed[68]

            # mstudiomodelgroup_t
            mdl.includemodel_count = parsed[69]
            mdl.includemodel_index = parsed[70]

            mdl.virtualModel = parsed[71]

            # mstudioanimblock_t
            mdl.animblocks_name_index = parsed[72]
            mdl.animblocks_count = parsed[73]
            mdl.animblocks_index = parsed[74]

            mdl.animblockModel = parsed[75]

            mdl.bonetablename_index = parsed[76]

            mdl.vertex_base = parsed[77]
            mdl.offset_base = parsed[78]

            mdl.directionaldotproduct = parsed[79]
            mdl.rootLod = parsed[80]
            mdl.numAllowedRootLods = parsed[81]

            # unused = parsed[82]
            # unused = parsed[83]

            # mstudioflexcontrollerui_t
            mdl.flexcontrollerui_count = parsed[84]
            mdl.flexcontrollerui_index = parsed[85]

            studiohdr2index = parsed[86]
            # unused = parsed[87]

    return mdl


mstudiobone_t = Struct('<ii6i3f4f3f3f3f12f4f3iiii8i')


def make_mstudiobone_t(data):
    instance = Mdl_mstudiobone_t()

    instance.sznameindex = data[0]
    instance.parent = data[1]
    instance.bonecontroller = list(data[2:8])

    instance.pos = tuple(data[8:11])
    instance.quat = tuple(data[11:15])
    instance.rot = tuple(data[15:18])

    instance.posscale = tuple(data[18:21])
    instance.rotscale = tuple(data[21:24])

    instance.poseToBone = (tuple(data[24:28]),
                           tuple(data[28:32]),
                           tuple(data[32:36]))
    instance.qAlignment = tuple(data[36:40])
    instance.flags = data[41]
    instance.proctype = data[42]
    instance.procindex = data[43]

    instance.physicsbone = data[44]
    instance.surfacepropidx = data[45]
    instance.unused = list(data[46:54])
    return instance


mstudiobonecontroller_t = Struct('iiffiii')


def make_mstudiobonecontroller_t(data):
    instance = Mdl_mstudiobonecontroller_t()
    # int                 bone
    # int                 type
    # float               start
    # float               end
    # int                 rest
    # int                 inputfield
    # int                 unused[8]
    return instance


mstudiohitboxset_t = Struct('iii')


def make_mstudiohitboxset_t(data):
    instance = Mdl_mstudiohitboxset_t()
    # int                 sznameindex;
    # int                 numhitboxes;
    # int                 hitboxindex;
    return instance


def make_mstudiomouth_t(data):
    instance = Mdl_mstudiomouth_t()
    # int                 bone;
    # Vector              forward;
    # int                 flexdesc;

    return instance


mstudiobodyparts_t = Struct('iiii')


def make_mstudiobodyparts_t(data):
    instance = Mdl_mstudiobodyparts_t()
    instance.sznameindex = data[0]
    instance.nummodels = data[1]
    instance.base = data[2]
    instance.modelindex = data[3]
    return instance


def make_mstudioanimdesc_t(data):
    instance = Mdl_mstudioanimdesc_t()
    # int                 baseptr;
    # int                 sznameindex
    # float               fps
    # int                 flags
    # int                 numframes
    # int                 nummovements
    # int                 movementindex
    # int                 unused1[6]
    # int                 animblock
    # int                 animindex
    # mstudioanim_t * pAnimBlock(int block, int index) const
    # mstudioanim_t * pAnim(int * piFrame, float & flStall) const
    # mstudioanim_t *pAnim( int *piFrame ) const; // returns pointer to data and new frame index

    # int                 numikrules;
    # int                 ikruleindex;    // non-zero when IK data is stored in the mdl
    # int                 animblockikruleindex; // non-zero when IK data is stored in animblock file
    # mstudioikrule_t *pIKRule( int i ) const;

    # int                 numlocalhierarchy;
    # int                 localhierarchyindex;
    # mstudiolocalhierarchy_t *pHierarchy( int i ) const;

    # int                 sectionindex;
    # int                 sectionframes;

    # short               zeroframespan;  // frames per span
    # short               zeroframecount; // number of spans
    # int                 zeroframeindex;
    # byte                * pZeroFrameData()

    # mutable float       zeroframestalltime
    return instance


def make_mstudioseqdesc_t(data):
    instance = Mdl_mstudioseqdesc_t()

    # int                 baseptr;
    # int                 szlabelindex;
    # int                 szactivitynameindex;
    # int                 flags;      // looping/non-looping flags
    # int                 activity;   // initialized at loadtime to game DLL values
    # int                 actweight;
    # int                 numevents;
    # int                 eventindex;
    # Vector              bbmin;      // per sequence bounding box
    # Vector              bbmax;
    # int                 numblends;
    # int                 animindexindex;

    # int                 movementindex;  // [blend] float array for blended movement
    # int                 groupsize[2];
    # int                 paramindex[2];  // X, Y, Z, XR, YR, ZR
    # float               paramstart[2];  // local (0..1) starting value
    # float               paramend[2];    // local (0..1) ending value
    # int                 paramparent;

    # float               fade# intime;     // ideal cross fate in time (0.2 default)
    # float               fadeouttime;    // ideal cross fade out time (0.2 default)

    # int                 localentrynode;     // transition node at entry
    # int                 localexitnode;      // transition node at exit
    # int                 nodeflags;      // transition rules

    # float               entryphase;     // used to match entry gait
    # float               exitphase;      // used to match exit gait

    # float               lastframe;      // frame that should generation EndOfSequence

    # int                 nextseq;        // auto advancing sequences
    # int                 pose;           // index of delta animation between end and nextseq

    # int                 numikrules;
    # int                 numautolayers;
    # int                 autolayerindex;
    # int                 weightlistindex;

    # int                 posekeyindex;
    # float               *pPoseKey( int iParam, int iAnim ) const { return (float *)(((byte *)this) + posekeyindex) + iParam * groupsize[0] + iAnim; }
    # float               poseKey( int iParam, int iAnim ) const { return *(pPoseKey( iParam, iAnim )); }

    # int                 numiklocks;
    # int                 iklockindex;
    # int                 keyvalueindex;
    # int                 keyvaluesize;
    # int                 cycleposeindex;     // index of pose parameter to use as cycle index

    # int                 unused[7];

    return instance


mstudioposeparamdesc_t = Struct('iifff')


def make_mstudioposeparamdesc_t(data):
    instance = Mdl_mstudioposeparamdesc_t()
    # int                 sznameindex;
    # int                 flags;  // ????
    # float               start;  // starting value
    # float               end;    // ending value
    # float               loop;   // looping range, 0 for no looping, 360 for rotations, etc.
    return instance


mstudioflexdesc_t = Struct('i')


def make_mstudioflexdesc_t(data):
    instance = Mdl_mstudioflexdesc_t()
    # int                 szFACSindex
    return instance


mstudioflexcontroller_t = Struct('iiiff')


def make_mstudioflexcontroller_t(data):
    instance = Mdl_mstudioflexcontroller_t()
    # int                 sztypeindex;
    # int                 sznameindex;

    # mutable int         localToGlobal;  // remapped at load time to master list
    # float               min;
    # float               max;
    return instance


mstudioflexrule_t = Struct('3i')


def make_mstudioflexrule_t(data):
    instance = Mdl_mstudioflexrule_t()
    # int                 flex;
    # int                 numops;
    # int                 opindex;
    return instance


mstudioikchain_t = Struct('4i')


def make_mstudioikchain_t(data):

    instance = Mdl_mstudioikchain_t()
    # int             sznameindex;
    # int             linktype;
    # int             numlinks;
    # int             linkindex;
    return instance


mstudiotexture_t = Struct('iiiiii10i')


def make_mstudiotexture_t(data):

    instance = Mdl_mstudiotexture_t()

    instance.sznameindex = data[0]
    instance.flags = data[1]
    instance.used = data[2]
    instance.unused1 = data[3]
    instance.material = data[4]
    instance.clientmaterial = data[5]
    instance.unused = data[-10:]

    return instance


def make_mstudioattachment_t(data):

    instance = Mdl_mstudioattachment_t()
    # int                 sznameindex;
    # unsigned int        flags;
    # int                 localbone;
    # matrix3x4_t         local; // attachment point
    # int                 unused[8];
    return instance


def make_mstudioiklock_t(data):
    instance = Mdl_mstudioiklock_t()
    # int         chain;
    # float       flPosWeight;
    # float       flLocalQWeight;
    # int         flags;

    # int         unused[4];
    return instance


def make_mstudiomodelgroup_t(data):
    instance = Mdl_mstudiomodelgroup_t()
    # int                 szlabelindex;   // textual name
    # int                 sznameindex;    // file name
    return instance
