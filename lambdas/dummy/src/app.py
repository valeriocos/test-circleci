import os


def handler(event, context):
    return prepare_message()


def prepare_message():
    return {"body": "Hello, CDK! You are in {}".format(os.environ["SETTINGS_MODULE"])}
