from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("System", show=False):
    with Cluster("internet"):
        obsidian_sync = EC2("Obsidian Sync")
        obsidian_repo = EC2("Obsidian Repo")

    with Cluster("local"):
        co_author = EC2("Co-Author")
        local_copy_vault = EC2("Local Copy Vault")
        
        co_author >> local_copy_vault

        local_copy_vault >> obsidian_sync
        local_copy_vault >> obsidian_repo


    with Cluster("vps"):
        traefik = EC2("Traefik")
        obsidian_api = EC2("Obsidian API (Nest)")
        flash = EC2("Flash (Python)")
        front = EC2("Front (Vue + Caddy)")
        api = EC2("API (Spring Boot)")
        mongodb = RDS("MongoDB")

        obsidian_api >> api
        flash >> api
        mongodb >> api

        api >> front
        front >> traefik

        obsidian_api >> obsidian_repo
