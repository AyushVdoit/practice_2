from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_function,
    aws_apigateway as api
    
)
from constructs import Construct

class Practice2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        login_lambda = lambda_function.Function(self, id = 'Login_lambda', 
                                                runtime = lambda_function.Runtime.PYTHON_3_9, 
                                                handler = "login.handler",code = lambda_function.Code.from_asset("lambdacode/login")
                                                )
        login_api = api.LambdaRestApi(self,id='loginapi',rest_api_name='practice_api',handler=login_lambda)
        
        logout_lambda = lambda_function.Function(self, id = 'Logout_lambda', 
                                                runtime = lambda_function.Runtime.PYTHON_3_9, 
                                                handler = "logout.handler",code = lambda_function.Code.from_asset("lambdacode/logout")
                                                )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Practice2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
