from __future__ import annotations

from typing import Literal

from aind_behavior_services.task_logic import AindBehaviorTaskLogicModel, TaskParameters
from pydantic import Field

__version__ = "0.0.0"


class AindBehaviorPirouetteTaskParameters(TaskParameters):
    pass


class AindBehaviorPirouetteTaskLogic(AindBehaviorTaskLogicModel):
    version: Literal[__version__] = __version__
    name: Literal["AindBehaviorPirouette"] = Field(
        default="AindBehaviorPirouette", description="Name of the task logic", frozen=True
    )
    task_parameters: AindBehaviorPirouetteTaskParameters = Field(..., description="Parameters of the task logic")
