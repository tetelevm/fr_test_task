from .default import *

if DEBUG:
    from .debug import *
else:
    from .production import *
