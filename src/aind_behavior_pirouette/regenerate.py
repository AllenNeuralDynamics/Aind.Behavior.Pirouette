from pathlib import Path

from aind_behavior_services import AindBehaviorSessionModel
from aind_behavior_services.utils import BonsaiSgenSerializers, convert_pydantic_to_bonsai

import aind_behavior_pirouette.rig

SCHEMA_ROOT = Path("./src/DataSchemas/")
EXTENSIONS_ROOT = Path("./src/Extensions/")
NAMESPACE_PREFIX = "AindBehaviorPirouetteDataSchema"


def main():
    models = [
        aind_behavior_pirouette.rig.AindBehaviorPirouetteRig,
        AindBehaviorSessionModel,
    ]

    for model in models:
        module_name = "aind_behavior_pirouette"
        module_name = module_name.split(".")[-1]

    convert_pydantic_to_bonsai(
        model,
        model_name="aind_behavior_pirouette",
        root_element="Root",
        cs_namespace=NAMESPACE_PREFIX,
        json_schema_output_dir=SCHEMA_ROOT,
        cs_output_dir=EXTENSIONS_ROOT,
        cs_serializer=[BonsaiSgenSerializers.JSON],
    )


if __name__ == "__main__":
    main()
