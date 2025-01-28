import os

from aind_behavior_pirouette import rig, task_logic
from aind_behavior_services import rig as abs_rig
from aind_behavior_services import session as session


def mock_session():
    return session.AindBehaviorSessionModel(
        experiment="RunningTests",
        experimenter=["Carl Schoonover"],
        root_path=r"C:\Data",
        allow_dirty_repo=True,
        skip_hardware_validation=True,
        subject="TestSubject",
        experiment_version="0.0.0",
    )


def mock_task_logic():
    return task_logic.AindBehaviorPirouetteTaskLogic(task_parameters=task_logic.AindBehaviorPirouetteTaskParameters())


def mock_rig():
    return rig.AindBehaviorPirouetteRig(
        rig_name="PIROUETTE-01",
        camera_controller=abs_rig.CameraController[abs_rig.SpinnakerCamera](
            frame_rate=60,
            cameras={
                "TopCamera": abs_rig.SpinnakerCamera(
                    serial_number="23373883",
                    binning=1,
                    exposure=10000,
                    gain=0,
                    adc_bit_depth=abs_rig.SpinnakerCameraAdcBitDepth.ADC10BIT,
                    video_writer=None,  # video writer is not yet implemented via custom dsl
                )
            },
        ),
        harp_output_expander=rig.HarpOutputExpander(port_name="COM14"),
        harp_white_rabbit=abs_rig.HarpWhiteRabbit(port_name="COM15"),
        onix_commutator=rig.OnixCommutator(port_name="COM4", additional_settings=rig.CommutatorSettings()),
        robocopy_controller=rig.RobocopyController(remote_path=r"\\allen\aind\scratch\pirouette\data"),
    )


def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)

    models = [mock_rig(), mock_task_logic(), mock_session()]
    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
