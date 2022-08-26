
from aws_cdk import(
    aws_elasticloadbalancingv2 as elbv2,
    Duration,
    aws_certificatemanager as acm, 
)

arn="arn:aws:acm:eu-central-1:517734281713:certificate/dc0d1172-7af9-489f-9d16-ab17a7cc20b5"

from constructs import Construct

class elb_construct(Construct):

    def __init__(self, scope: Construct, id: str, vpc, asg, **kwargs) -> None:
        super().__init__(scope, id)

        self.alb=elbv2.ApplicationLoadBalancer(self, "LB",
            vpc=vpc,
            internet_facing=True,
        )

        self.alb.add_redirect()

        arn="arn:aws:acm:eu-central-1:517734281713:certificate/dc0d1172-7af9-489f-9d16-ab17a7cc20b5"
        self.certificate=acm.Certificate.from_certificate_arn(self, "Certificate", arn)

        self.listener=self.alb.add_listener("Listener", 
        certificates=[self.certificate],
            port=443,
            open=True,
            ssl_policy=elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
        )

        self.listener.add_targets("target",
            port=80,
            targets=[asg],
            health_check=elbv2.HealthCheck(
                path="/",
                enabled=True,
                port="80",
            ),
            stickiness_cookie_duration=Duration.seconds(120),
            stickiness_cookie_name="StickyCookie",
        )

        self.listener.add_action("/static",
            priority=5,
            conditions=[elbv2.ListenerCondition.path_patterns(["/static"])],
            action=elbv2.ListenerAction.fixed_response(200,
                content_type="text/html",
                message_body="<h1>I DO work.</h1>"),
        )

        
    