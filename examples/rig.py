import os

from aind_behavior_pirouette import rig
from aind_behavior_services import rig as abs_rig

rig_settings = rig.AindBehaviorPirouetteRig(
    rig_name="PIROUETTE-01",
    camera_controller=abs_rig.cameras.CameraController[abs_rig.cameras.SpinnakerCamera](
        frame_rate=60,
        cameras={
            """More cameras can be added here"""
            "TopCamera": abs_rig.cameras.SpinnakerCamera(
                serial_number="23373886",
                binning=1,
                exposure=10000,
                gain=0,
                adc_bit_depth=abs_rig.cameras.SpinnakerCameraAdcBitDepth.ADC10BIT,
                video_writer=abs_rig.cameras.VideoWriterFfmpeg(frame_rate=60),
            )
        },
    ),
    harp_output_expander=abs_rig.harp.HarpOutputExpander(port_name="COM5"),
    harp_white_rabbit=abs_rig.harp.HarpWhiteRabbit(port_name="COM3"),
    onix_commutator=rig.OnixCommutator(
        port_name="COM6", additional_settings=rig.CommutatorSettings(magnetometer_turn_difference_threshold=1.5)
    ),
    robocopy_controller=rig.RobocopyController(remote_path=r"\\allen\aind\stage\chronic\data"),
    zmq_connection=abs_rig.network.ZmqConnection(connection_string="@tcp://localhost:5557"),
)


def main(path_seed: str = "./local/{schema}.json"):  # set desired path for JSON generation
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)

    models = [rig_settings]
    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
