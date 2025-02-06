from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("System", show=False):
    
    with Cluster("Cluster Docker Swarm"):
        ELB("lb") >> EC2("web") >> RDS("userdb")