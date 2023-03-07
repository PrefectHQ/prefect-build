from typing import Optional
from pydantic import BaseModel
from prefect import Flow


class DeploymentConfig(BaseModel):
    flow: Flow
    parameters: Optional[dict]
    schedule: Optional[str]
    infra_overrides: Optional[dict]
    