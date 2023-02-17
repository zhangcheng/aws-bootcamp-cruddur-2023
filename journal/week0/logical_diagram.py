from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ElasticContainerServiceContainer
from diagrams.aws.database import RDS, Dynamodb
from diagrams.programming.flowchart import Inspection, InternalStorage
from diagrams.aws.integration import Appsync
from diagrams.aws.network import Route53
from diagrams.aws.network import ALB
from diagrams.aws.security import Cognito
from diagrams.onprem.client import Client


with Diagram("Cruddur Logical Diagram", show=False):
    client = Client("Client")

    with Cluster("AWS Cloud"):
        dns = Route53("DNS")
        cognito = Cognito("Authentication")

        rds = RDS("RDS")
        ddb = Dynamodb("Dynamodb")
        app_sync = Appsync("Appsync")

        cache_integration_point = Inspection("")

        with Cluster("Virtual Private Cloud"):
            alb = ALB("Load Balancer")

            with Cluster("ECS Cluster Container"):
                front_end = ElasticContainerServiceContainer("Front-end")
                back_end = ElasticContainerServiceContainer("Back-end")


    with Cluster("3rd Party Services"):
        cache = InternalStorage("Momento")

    client >> dns
    client >> cognito

    dns >> alb
    alb >> front_end
    alb >> back_end
    front_end >> Edge(dir="both") << back_end
    cognito >> back_end

    app_sync >> front_end
    app_sync >> rds
    app_sync >> ddb
    rds >> Edge(dir="both") << back_end
    ddb << cache_integration_point >> back_end
    cache >> Edge(style="dotted") >> cache_integration_point
