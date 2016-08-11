from .base import *


try:
    if DEBUG:
        from .local import *
    else:
        from .production import *

except:
    pass
