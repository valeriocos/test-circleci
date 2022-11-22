#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stack.a_stack import AStack

DEFAULT_ENV_VARS = {
    "STACK_NAME": "AStack",
    "ENV_NAME": "dev",
}


def _get_env_var(name):
    return os.environ.get(f"A_{name}", DEFAULT_ENV_VARS[name])


app = cdk.App()
env_name = _get_env_var("ENV_NAME")
env_config = app.node.try_get_context(_get_env_var("ENV_NAME"))

AStack(
    app,
    _get_env_var("STACK_NAME"),
    env=cdk.Environment(
        account=env_config["account"],
        region=env_config["region"],
    ),
    env_name=env_name,
)

app.synth()
