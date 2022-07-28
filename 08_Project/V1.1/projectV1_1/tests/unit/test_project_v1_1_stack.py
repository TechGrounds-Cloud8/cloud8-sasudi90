import aws_cdk as core
import aws_cdk.assertions as assertions

from project_v1_1.project_v1_1_stack import ProjectV11Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in project_v1_1/project_v1_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjectV11Stack(app, "project-v1-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
