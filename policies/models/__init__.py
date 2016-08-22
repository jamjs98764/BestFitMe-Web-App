import glob
import os

from django.db import models

# A hack to access all modules in the models/ directory
_models_dir = os.path.dirname(__file__) or "."

for f in glob.glob("%s/*.py" % _models_dir):
    basename = os.path.basename(f)
    app_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    if basename == "__init__.py":
        continue

    module_name = basename[:-3]
    exec("from %s.models import %s" % (app_name, module_name))

    for name, value in eval(module_name).__dict__.items():
        if issubclass(type(value), models.Model):
            exec("%s = %s.%s" % (name, module_name, name))
