import os

from aind_behavior_services.session import AindBehaviorSessionModel

session_settings = AindBehaviorSessionModel(
    experiment="<experiment name>",
    experimenter=["<experimenter name>"],
    root_path=r"D:\Data",
    allow_dirty_repo=True,
    skip_hardware_validation=True,
    subject="<subject ID>",
    experiment_version="0.1.0",
)


def main(path_seed: str = "./local/{schema}.json"):  # set desired path for JSON generation
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)

    models = [session_settings]
    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
