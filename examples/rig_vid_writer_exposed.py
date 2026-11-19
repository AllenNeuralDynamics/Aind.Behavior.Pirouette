import os

from aind_behavior_services import rig as abs_rig

from aind_behavior_pirouette import rig

FRAME_RATE = 60

# Same filter and encoder settings as the current JSON output.
# Matroska output: no moov atom to lose, so a file that is cut off stays readable.
OUTPUT_ARGUMENTS = (
    '-vf "scale=out_range=full,setparams=range=full:colorspace=bt709:color_primaries=bt709:color_trc=linear" '
    "-c:v h264_nvenc -pix_fmt yuv420p -color_range full -colorspace bt709 "
    "-color_trc linear -tune hq -preset p3 -rc vbr -cq 18 -b:v 0M "
    '-metadata author="Allen Institute for Neural Dynamics" '
    "-maxrate 700M -bufsize 350M "
    "-f matroska -write_crc32 0"
)
INPUT_ARGUMENTS = "-colorspace bt709 -color_primaries bt709 -color_range full -color_trc linear"

# # Optional: fragmented MP4, so a file that is not closed cleanly stays playable.
# # Off by default. Check that your downstream tools read it before turning it on.
# FRAGMENTED_MP4 = False
# if FRAGMENTED_MP4:
#     OUTPUT_ARGUMENTS += " -movflags +frag_keyframe+empty_moov+default_base_moof"


def make_video_writer() -> abs_rig.cameras.VideoWriterFfmpeg:
    # A new instance per camera, so the two cameras never share one object.
    return abs_rig.cameras.VideoWriterFfmpeg(
        frame_rate=FRAME_RATE,
        container_extension="mp4",
        output_arguments=OUTPUT_ARGUMENTS,
        input_arguments=INPUT_ARGUMENTS,
    )


rig_settings = rig.AindBehaviorPirouetteRig(
    rig_name="Chronic.5",
    camera_controller=abs_rig.cameras.CameraController[abs_rig.cameras.SpinnakerCamera](
        frame_rate=FRAME_RATE,
        cameras={
            "TopCamera": abs_rig.cameras.SpinnakerCamera(
                serial_number="25502910",
                binning=1,
                exposure=5000,
                gain=10,
                adc_bit_depth=abs_rig.cameras.SpinnakerCameraAdcBitDepth.ADC10BIT,
                video_writer=make_video_writer(),
            ),
            "PortCamera": abs_rig.cameras.SpinnakerCamera(
                serial_number="26034883",
                binning=1,
                exposure=5000,
                gain=10,
                adc_bit_depth=abs_rig.cameras.SpinnakerCameraAdcBitDepth.ADC10BIT,
                video_writer=make_video_writer(),
            ),
        },
    ),
    harp_output_expander=abs_rig.harp.HarpOutputExpander(port_name="COM6"),
    harp_white_rabbit=abs_rig.harp.HarpWhiteRabbit(port_name="COM5"),
    onix_commutator=rig.OnixCommutator(
        port_name="COM4", additional_settings=rig.CommutatorSettings(magnetometer_turn_difference_threshold=1.5)
    ),
    robocopy_controller=rig.RobocopyController(remote_path=r"\\allen\aind\stage\chronic\data"),
)


def main(path_seed: str = "./local/{schema}.json"):  # set desired path for JSON generation
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)

    models = [rig_settings]
    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()