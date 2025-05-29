# Aind.Behavior.Pirouette

A repository with source code for long-term, freely moving, electrophisiology recordings in mice.

___

### Getting started 

1. Clone this repository. 
2. Clone the lifealert repository (https://github.com/AllenNeuralDynamics/lifealert).
3. Run the following deployment script to install dependencies: https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/scripts/install_dependencies.ps1.
4. In the root of the Aind.Behavior.Pirouette and lifealert, execute `uv sync` to install the dependencies denoted in the uv.lock file.
5. Regenerate the Bonsai environment in the Pirouette repo by running `setup.ps1` from the `./bonsai` directory.
6. Generate the rig.json, session.json, and task.json configuration files by running example.py found within the examples directory (update the content to reflect current experimental parameters, like device IDs).
7. Open Bonsai by running `./bonsai/Bonsai.exe`.
8. Open the desired script from the `./src` directory. 

