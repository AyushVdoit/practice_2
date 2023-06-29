import aws_cdk as core
import aws_cdk.assertions as assertions

from practice_2.practice_2_stack import Practice2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in practice_2/practice_2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Practice2Stack(app, "practice-2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
