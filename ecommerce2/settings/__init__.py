from .base import *

try:
    if DJANGO_ENV == "production":
        from .production import *
    else:
        from .local import *

except:
    pass
