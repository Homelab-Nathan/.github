from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.network import Traefik, Caddy
from diagrams.onprem.vcs import Github, Git
from diagrams.programming.language import Go, Python
from diagrams.programming.framework import Vue, Spring
from diagrams.onprem.database import Mongodb

def _get_custom(name: str, url: str, icon_path: str) :
    urlretrieve(url, icon_path)
    return Custom(name, icon_path)

def get_nest(name: str):
    return _get_custom(name, "http://docs.nestjs.com/assets/logo-small-gradient.svg", "icons/nest.png")


if __name__ == "__main__":
    with Diagram("System", show=False):
        with Cluster("Internet"):
            obsidian_sync = EC2("Obsidian Sync")
            obsidian_repo = Github("Vault Obsidian")

        with Cluster("Local"):
            co_author = Go("Co-Author")
            local_copy_vault = Git("Local Copy Vault Obsidian")
            
            co_author >> local_copy_vault

            local_copy_vault >> obsidian_sync
            local_copy_vault >> obsidian_repo


        with Cluster("VPS (Docker Swarm)"):
            traefik = Traefik("Reverse proxy")
            obsidian_api = EC2("Obsidian API")
            flash = Python("Flash")

            with Cluster("front"):
                front = Vue("Front")
                front_server = Caddy("Front server")

                front >> front_server

            api = Spring("API (Spring Boot)")
            mongodb = Mongodb("MongoDB")

            obsidian_api >> api
            flash >> api
            mongodb >> api

            api >> front
            front_server >> traefik

            obsidian_api >> obsidian_repo
