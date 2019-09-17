from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()


class Mdl(object):
    """Contains all the data from a Mdl file such as
    entities and other editor informations."""

    def __init__(self):
        """Creates an empty instance of Mdl."""

        self.id = None
        self.version = None
        self.checksum = None
        self.name = None
        self.dataLength = None

        self.eyeposition = None
        self.illumposition = None
        self.hull_min = None
        self.hull_max = None
        self.view_bbmin = None
        self.view_bbmax = None

        self.flags = None


class Mdl_mstudiobone_t(object):
    """The Mdl mstudiobone_t struct."""

    def __init__(self):
        self.sznameindex = None
        self.parent = None
        self.bonecontroller = [None, None, None, None, None, None]

        self.pos = (None, None, None)
        self.quat = (None, None, None, None)
        self.rot = (None, None, None)

        self.posscale = (None, None, None)
        self.rotscale = (None, None, None)

        self.poseToBone = ((None, None, None, None),
                           (None, None, None, None),
                           (None, None, None, None))
        self.qAlignment = (None, None, None, None)
        self.flags = None
        self.proctype = None
        self.procindex = None

        self.physicsbone = None
        self.surfacepropidx = None
        self.unused = [None, None, None, None, None, None, None, None]


class Mdl_mstudiobonecontroller(object):
    """The Mdl mstudiobonecontroller_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudiohitboxset_t(object):
    """The Mdl mstudiohitboxset_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioMouth_t(object):
    """The Mdl mstudioMouth_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_studioloddata_t(object):
    """The Mdl studioloddata_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioanimdesc_t(object):
    """The Mdl mstudioanimdesc_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioseqdesc_t(object):
    """The Mdl mstudioseqdesc_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioposeparamdesc_t(object):
    """The Mdl mstudioposeparamdesc_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioflexdesc_t(object):
    """The Mdl mstudioflexdesc_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioflexrule_t(object):
    """The Mdl mstudioflexrule_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudiotexture_t(object):
    """The Mdl mstudiotexture_t struct."""

    def __init__(self):
        self.placeholder = None
        self.sznameindex = None
        self.pszname = ''
        self.flags = None
        self.used = None
        self.unused1 = None
        self.material = None
        self.clientmaterial = None
        self.unused = None


class Mdl_mstudioattachment_t(object):
    """The Mdl mstudioattachment_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudioiklock_t(object):
    """The Mdl mstudioiklock_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudiomodelgroup_t(object):
    """The Mdl mstudiomodelgroup_t struct."""

    def __init__(self):
        self.placeholder = None


class Mdl_mstudiobodyparts_t(object):
    """The Mdl mstudiobodyparts_t struct."""

    def __init__(self):
        self.sznameindex = None
        self.nummodels = None
        self.base = None
        self.modelindex = None
