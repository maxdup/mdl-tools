from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from .common_struct import *  # NOQA: #402
from construct import *  # NOQA: #402

mstudioboneweight_t = Struct(
    'weight' / Float32l[MAX_NUM_BONES_PER_VERT],
    'bone' / Byte[MAX_NUM_BONES_PER_VERT],
    'numbones' / Byte,
)

mstudiovertex_t = Struct(
    'm_BoneWeights' / mstudioboneweight_t,
    'm_vecPosition' / Vector,
    'm_vecNormal' / Vector,
    'm_vecTexCoord' / Vector2D
)

vertexFileFixup_t = Struct(
    'lod' / Int32sl,
    'sourceVertexID' / Int32sl,
    'numVertexes' / Int32sl
)

vertexFileHeader_t = Struct(
    'id' / Const(b'IDSV'),
    'version' / Const(4, Int32sl),
    'checksum' / Int32sl,

    'numLODs' / Int32sl,
    'numLODVertexes' / Int32sl[MAX_NUM_LODS],

    'numFixups' / Int32sl,
    'fixupTableStart' / Int32sl,

    'vertexDataStart' / Int32sl,
    'tangentDataStart' / Int32sl,

    'numvertexes' /
    Computed(lambda this: sum(this.numLODVertexes[:1])),

    'fixups' / Pointer(this.fixupTableStart, vertexFileFixup_t[this.numFixups]),

    'vertexData' / Pointer(this.vertexDataStart,
                           mstudiovertex_t[this.numvertexes]),
    'tangentData' / Pointer(this.tangentDataStart, Vector4D[this.numvertexes]),
)
