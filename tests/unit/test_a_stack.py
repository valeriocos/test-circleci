import aws_cdk as cdk
import pytest
from aws_cdk import assertions as assertions

from stack.a_stack import (
    DUMMY_FUNCTION_TAG,
)
from stack.a_stack import AStack as Stack


@pytest.fixture(scope="session")
def stack():
    app = cdk.App()
    test_env = cdk.Environment(region="us-east-1")
    return Stack(app, "a-service", env=test_env)


@pytest.fixture(scope="session")
def template(stack):
    return assertions.Template.from_stack(stack)


def test_stack_create_dummy_lambda(template):
    template.resource_count_is("AWS::Lambda::Function", 1)

    template.find_resources(
        "AWS::Lambda::Function",
        {"Properties": {"Tags": [{"Key": "Function", "Value": DUMMY_FUNCTION_TAG}]}},
    )
