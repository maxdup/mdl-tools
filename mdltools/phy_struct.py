from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from builtins import int
from future import standard_library
standard_library.install_aliases()

from .common_struct import *  # NOQA: #402
from construct import *  # NOQA: #402

compactsurfaceheader_t = Struct(

    'size' / Int32sl,
    'vphysicsID' / Bytes(4),  # VPHY
    'version' / Int16sl,
    'modelType' / Int16sl,
    'surfaceSize' / Int32sl,
    'dragAxisAreas' / Vector,
    'axisMapSize' / Int32sl
)

legacysurfaceheader_t = Struct(
    'mass_center' / Float32l[3],
    'rotation_inertia' / Float32l[3],
    'upper_limit_radius' / Float32l,
    'max_deviation' / Int32sl,
    'byte_size' / Int32sl,
    'dummy' / Int32sl[3],  # IVPS
)

ragdollconstraintdesc = Struct(
    'parent_index' / Int32sl,
    'child_index' / Int32sl,
    'xmin' / Float32l,
    'xmax' / Float32l,
    'xfriction' / Float32l,
    'ymin' / Float32l,
    'ymax' / Float32l,
    'yfriction' / Float32l,
    'zmin' / Float32l,
    'zmax' / Float32l,
    'zfriction' / Float32l,
)

triangleface_t = Struct(
    'id' / Int8ul,
    'dummy1' / Bytes(3),
    'v1' / Int8ul,
    'dummy2' / Bytes(3),
    'v2' / Int8ul,
    'dummy3' / Bytes(3),
    'v3' / Int8ul,
    'dummy4' / Bytes(3),
)

trianglefaceheader_t = Struct(
    'm_offsetTovertices' / Int32sl,
    'dummy' / Int32sl[2],
    'm_countFaces' / Int32sl,
    'size' / Computed(this.m_countFaces * 16 + 16),

    'triangle_faces' / triangleface_t[this.m_countFaces],

    'max_vid' / Computed(lambda ctx: (max([max(f.v1, f.v2, f.v3)
                                           for f in ctx.triangle_faces]))),
)

unknown_recursive = Struct(
    'size' / Int32sl,
    'dummy1' / Int32sl,
    'dummy2' / Float32l,
    'dummy3' / Float32l,
    'dummy4' / Float32l,
    'dummy5' / Float32l,
    'dummy6' / Float32l,
    'childs' / If(this.size > 0, RepeatUntil(lambda x, lst, ctx:
                                             sum(max(u.size, 28) for u in lst)
                                             >= max(ctx.size, 28) - 28,
                                             LazyBound(lambda: unknown_recursive)))
)

phyblock = Struct(
    'compact' / compactsurfaceheader_t,
    'legacy' / legacysurfaceheader_t,
    'triangle_headers' /
    RepeatUntil(lambda x, lst, ctx: x.m_offsetTovertices ==
                x.size, trianglefaceheader_t),

    'vector_count' /
    Computed(lambda ctx: max(h.max_vid for h in ctx.triangle_headers)),

    'vectors' / RepeatUntil(lambda x, lst, ctx: len(lst)
                            > max(h.max_vid for h in ctx.triangle_headers), Vector4D),

    'childs' / RepeatUntil(lambda x, lst, ctx: x.size == 0, unknown_recursive)
)

phyheader_t = Struct(

    'size' / Int32sl,
    'id' / Int32sl,
    'solidCount' / Int32sl,
    'checkSum' / Int32sl,

    'blocks' / phyblock[this.solidCount],
    'string' / CString('ascii')
)
