from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from .common_struct import *  # NOQA: #402
from construct import *  # NOQA: #402

Vertex_t = Struct(
    'boneWeightIndex' / Int8ul[3],
    'numBones' / Int8ul,

    'origMeshVertID' / Int16ul,

    'boneID' / Int8sl[3]
)

BoneStateChangeHeader_t = Struct(
    'hardwareID' / Int32sl,
    'newBoneID' / Int32sl,
)

StripHeader_t = Struct(
    'numIndices' / Int32sl,
    'indexOffset' / Int32sl,

    'numVerts' / Int32sl,
    'vertOffset' / Int32sl,

    'numBones' / Int16sl,

    'flags' / Int8ul,

    'numBoneStateChanges' / Int32sl,
    'boneStateChangeOffset' / Int32sl,

    'selfOffset' / Computed(this._index*27 +
                            this._.selfOffset + this._.stripOffset),

    'BoneStateChanges' / Pointer(this.selfOffset + this.boneStateChangeOffset,
                                 BoneStateChangeHeader_t[this.numBoneStateChanges])
)

StripGroupHeader_t = Struct(
    'numVerts' / Int32sl,
    'vertOffset' / Int32sl,

    'numIndices' / Int32sl,
    'indexOffset' / Int32sl,

    'numStrips' / Int32sl,
    'stripOffset' / Int32sl,

    'flags' / Int8ul,

    'selfOffset' / Computed(this._index*25 +
                            this._.selfOffset + this._.stripGroupHeaderOffset),

    'Verts' / Pointer(this.selfOffset + this.vertOffset,
                      Vertex_t[this.numVerts]),
    'indices' / Pointer(this.selfOffset + this.indexOffset,
                        Int16sl[this.numIndices]),
    'Strips' / Pointer(this.selfOffset + this.stripOffset,
                       StripHeader_t[this.numStrips]),
)

MeshHeader_t = Struct(
    'numStripGroups' / Int32sl,
    'stripGroupHeaderOffset' / Int32sl,
    'flags' / Int8ul,

    'selfOffset' / Computed(this._index*9 +
                            this._.selfOffset + this._.meshOffset),
    'GroupHeaders' / Pointer(this.selfOffset + this.stripGroupHeaderOffset,
                             StripGroupHeader_t[this.numStripGroups])
)

ModelLODHeader_t = Struct(
    'numMeshes' / Int32sl,
    'meshOffset' / Int32sl,
    'switchPoint' / Float32l,

    'selfOffset' / Computed(this._index*12 +
                            this._.selfOffset + this._.lodOffset),
    'meshes' / Pointer(this.selfOffset + this.meshOffset,
                       MeshHeader_t[this.numMeshes])
)

ModelHeader_t = Struct(
    'numLODs' / Int32sl,
    'lodOffset' / Int32sl,

    'selfOffset' / Computed(this._index*8 +
                            this._.selfOffset + this._.modelOffset),
    'lodHeaders' / Pointer(this.selfOffset + this.lodOffset,
                           ModelLODHeader_t[this.numLODs])
)

BodyPartHeader_t = Struct(
    'numModels' / Int32sl,
    'modelOffset' / Int32sl,

    'selfOffset' / Computed(this._index*8 + this._.bodyPartOffset),
    'models' / Pointer(this.selfOffset + this.modelOffset,
                       ModelHeader_t[this.numModels])
)

MaterialReplacementHeader_t = Struct(
    'materialID' / Int16sl,
    'replacementMaterialNameOffset' / Int32sl,
)

MaterialReplacementListHeader_t = Struct(
    'numReplacements' / Int32sl,
    'replacementOffset' / Int32sl,
    # not fully implemented, cannot find candidate to test against
)

vtxheader_t = Struct(
    'version' / Const(7, Int32sl),
    'vertCacheSize' / Int32sl,
    'maxBonesPerStrip' / Int16ul,
    'maxBonesPerTri' / Int16ul,
    'maxBonesPerVert' / Int32sl,

    'checksum' / Int32sl,
    'numLODs' / Int32sl,

    'materialReplacementListOffset' / Int32sl,

    'materialReplacements' / Pointer(this.materialReplacementListOffset,
                                     MaterialReplacementListHeader_t[this.numLODs]),

    'numBodyParts' / Int32sl,
    'bodyPartOffset' / Int32sl,

    'bodyParts' / Pointer(this.bodyPartOffset,
                          BodyPartHeader_t[this.numBodyParts]),

)
