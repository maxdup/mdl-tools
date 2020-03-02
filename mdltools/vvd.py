from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
class Vvd(object):
    """Contains all the vertex data from a Vvd file."""

    def __init__(self):
        """Creates an empty instance of Vvd."""

        self.id = None
