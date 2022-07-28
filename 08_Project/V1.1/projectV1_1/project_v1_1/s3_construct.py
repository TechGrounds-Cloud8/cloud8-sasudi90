from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
)

from constructs import Construct

class S3_construct(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id)

        self.pdsbucket=s3.Bucket(self, "pdsbucketau",
            bucket_name="pdsbucketau",
            removal_policy=RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            auto_delete_objects=True,
        )

        self.deploy=s3deploy.BucketDeployment(self, "postdeploy",
            sources=[s3deploy.Source.asset('./postdeploymentscripts')],
            destination_bucket=self.pdsbucket,
        )

