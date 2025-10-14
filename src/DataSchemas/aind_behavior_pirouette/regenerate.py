import inspect
from pathlib import Path

from aind_behavior_services import AindBehaviorSessionModel
from aind_behavior_services.utils import (
    convert_pydantic_to_bonsai,
    pascal_to_snake_case,
    snake_to_pascal_case,
)

import aind_behavior_pirouette.rig

SCHEMA_ROOT = Path.cwd().parent
EXTENSIONS_ROOT = Path.cwd().parent.parent.joinpath("Extensions")
NAMESPACE_PREFIX = "AindBehaviorPirouetteDataSchema"


def main():
    models = [
        aind_behavior_pirouette.rig.AindBehaviorPirouetteRig,
        AindBehaviorSessionModel,
    ]

    for model in models:
        module_name = inspect.getmodule(model).__name__
        module_name = module_name.split(".")[-1]
        schema_name = f"{pascal_to_snake_case(model.__name__)}"
        namespace = f"{NAMESPACE_PREFIX}.{snake_to_pascal_case(module_name)}"

        print((schema_name, namespace))
        convert_pydantic_to_bonsai(
            model=model,
            model_name=schema_name,
            json_schema_output_dir=SCHEMA_ROOT,
            cs_output_dir=EXTENSIONS_ROOT,
            cs_namespace=namespace,
            json_schema_export_kwargs=dict(
                remove_root=False
            ),  # needs to be false otherwise session model json isn't generated correctly
        )


if __name__ == "__main__":
    main()
