from __future__ import absolute_import
import logging
import _version


__version__ = _version.__version__
__version_info__ = _version.__version_info__

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
