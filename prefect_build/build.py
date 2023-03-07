import yaml
from prefect.deployments import Deployment
from prefect import Flow

def parse_yaml(file_path: str):
    with open(file_path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError() as exc:
            print(exc)


def build_deployment(flow:Flow, name:str, ):
    deployment = Deployment.build_from_flow(
        flow=log_flow,
        name="log-simple",
        parameters={"name": "Marvin"},
        infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
        work_queue_name="test",
    )

def build_from_file():
    