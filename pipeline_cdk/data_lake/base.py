from enum import Enum
from aws_cdk import core
from aws_cdk import aws_s3 as s3
from pipeline_cdk.environment import Environment


class DataLakeLayer(Enum):
    RAW = 'raw'
    PROCESSED = 'processed'
    AGGREGATED = 'aggregated'


class BaseDataLakeBucket(s3.Bucket):
    def __init__(self, scope: core.Construct, deploy_env: Environment, layer: DataLakeLayer, **kwargs):
        self.layer = layer
        self.deploy_env = deploy_env
        self.obj_name = f's3-canuto-{self.deploy_env.value}-data-lake-{self.layer.value}'
        super().__init__(
            scope,
            id = self.obj_name,
            bucket_name = self.obj_name,
            block_public_access = self.default_block_public_access,
            encryption = self.default_encryption,
            versioned = False,
            **kwargs
        )
    
    @property
    def default_block_public_access(self):
        return s3.BlockPublicAccess(
                ignore_public_acls=True,
                block_public_acls=True,
                block_public_policy=True,
                restrict_public_buckets=True
        )

    @property
    def default_encryption(self):
        return s3.BucketEncryption.S3_MANAGED

    def set_default_lifecycle_rules(self):
        