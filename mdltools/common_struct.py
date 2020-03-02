from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: E402
from .constants import *  # NOQA: E402


def readcstr(f):
    return ''.join(iter(lambda: f.read(1).decode('ascii'), '\x00'))


Vector = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)
Vector2D = Struct('x' / Float32l, 'y' / Float32l)
Vector4D = Struct('x' / Float32l, 'y' / Float32l,
                  'z' / Float32l, 'w' / Float32l)
RadianEuler = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)
Quaternion = Struct('x' / Float32l, 'y' / Float32l,
                    'z' / Float32l, 'w' / Float32l)
matrix3x4_t = Sequence(Float32l[4], Float32l[4], Float32l[4])
