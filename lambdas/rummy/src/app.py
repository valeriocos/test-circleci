import os


def handler(event, context):
    return prepare_message()


def prepare_message():
    return {"body": "Hello, CDK! You are in {}".format(os.environ["SETTINGS_MODULE"])}


def another_message():
    return {"body": "Hello again, CDK! You are in {}".format(os.environ["SETTINGS_MODULE"])}


def stalking_message():
    return {"body": "Hello once more, CDK! You are in {}".format(os.environ["SETTINGS_MODULE"])}
