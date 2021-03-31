#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core
from pipeline_cdk.pipeline_cdk_stack import PipelineCdkStack


app = core.App()
PipelineCdkStack(app, "PipelineCdkStack",
   

   
    )

app.synth()
