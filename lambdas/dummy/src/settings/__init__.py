import os

settings_module = os.environ.get("SETTINGS_MODULE", "dev")

if settings_module == "dev":
    from .dev import *  # noqa
elif settings_module == "test":
    from .test import *  # noqa
elif settings_module == "preprod":
    from .preprod import *  # noqa
elif settings_module == "prod":
    from .prod import *  # noqa
