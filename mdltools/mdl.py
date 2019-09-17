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
