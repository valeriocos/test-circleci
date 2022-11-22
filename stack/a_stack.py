from aws_cdk import Stack, Tags
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda
from constructs import Construct


EXCLUDED_PATTERNS = [".venv", "__pycache__", "Dockerfile", ".dockerignore", "tests"]
DUMMY_FUNCTION_TAG = "DUMMY"



class AStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, env_name: str = "dev", **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.env_name = env_name

        self.create_dummy_lambda(env_name)

    def create_dummy_lambda(self, env_name: str) -> aws_lambda.Function:
        dummy_role = iam.Role(
            self,
            "DummyLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            inline_policies={
                "network_interfaces": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "ec2:DescribeNetworkInterfaces",
                                "ec2:CreateNetworkInterface",
                                "ec2:DeleteNetworkInterface",
                                "ec2:DescribeInstances",
                                "ec2:AttachNetworkInterface",
                            ],
                            resources=["*"],
                        )
                    ]
                ),
            },
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                )
            ],
        )

        dummy_lambda_fn = aws_lambda.Function(
            self,
            "DummyLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.from_asset(
                "./lambdas/dummy", exclude=EXCLUDED_PATTERNS
            ),
            role=dummy_role,
            handler="src.app.handler",
            environment={
                "SETTINGS_MODULE": env_name,
            },
        )

        Tags.of(dummy_lambda_fn).add("Function", DUMMY_FUNCTION_TAG)

        return dummy_lambda_fn
