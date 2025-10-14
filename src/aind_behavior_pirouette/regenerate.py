from pathlib import Path
from typing import Union

import pydantic
from aind_behavior_services.session import AindBehaviorSessionModel
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
    model = pydantic.RootModel[Union[tuple(models)]]

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
