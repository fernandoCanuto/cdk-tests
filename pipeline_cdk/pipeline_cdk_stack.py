from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk import aws_s3 as s3


class PipelineCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # The code that defines your stack goes here
