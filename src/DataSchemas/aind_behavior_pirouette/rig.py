from typing import Literal

import aind_behavior_services.rig as rig
from pydantic import BaseModel, Field, PositiveFloat

__version__ = "0.2.0"


class CommutatorSettings(BaseModel):
    magnetometer_magnitude_threshold: float = Field(
        default=50, description="Field magnitude threshold below which samples will be discarded."
    )
    magnetometer_override_sampling: PositiveFloat = Field(
        default=2,
        description="Period of time in seconds that will be used to sample, and override, the commutator via the magnetometer correction.",
    )
    magnetometer_turn_difference_threshold: PositiveFloat = Field(
        default=1.5,
        description="The minimum absolute difference necessary to drive a commutator correction via the magnetometer.",
    )
    imu_rotation_axis: rig.Vector3 = Field(
        default=rig.Vector3(x=0, y=0, z=1), description="The axis of rotation for the IMU correction."
    )


class OnixCommutator(rig.Device):
    device_type: Literal["OnixCommutator"] = "OnixCommutator"
    port_name: str = Field(..., description="Commutator COM port name.")
    additional_settings: CommutatorSettings = Field(
        default=CommutatorSettings(), description="Additional settings for the commutator.", validate_default=True
    )


class RobocopyController(BaseModel):
    remote_path: str = Field(..., description="Remote path to copy files to.")


class AindBehaviorPirouetteRig(rig.AindBehaviorRigModel):
    version: Literal[__version__] = __version__
    camera_controller: rig.CameraController[rig.SpinnakerCamera] = Field(
        ..., description="Required camera controller to triggered cameras."
    )
    harp_white_rabbit: rig.HarpWhiteRabbit = Field(..., description="Harp white rabbit")
    harp_output_expander: rig.HarpOutputExpander = Field(..., description="Harp output expander")
    onix_commutator: OnixCommutator = Field(..., description="Onix commutator")
    robocopy_controller: RobocopyController = Field(..., description="Robocopy controller")
