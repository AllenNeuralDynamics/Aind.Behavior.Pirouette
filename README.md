# Aind.Behavior.Pirouette

Authors: Bruno Cruz, Brandon Pratt, and Carl Schoonover

Last Updated: 05/15/2025

A repository with source code and instructions for long-term, electrophisiology recordings in behaving mice

---
## Content
### 1. Getting started 
### 2. Pirouette Bonsai workflow
### 3. Lifealert 
### 4. Neural activity visualization
---
### 1. Getting started 
1. If using a new computer, contact IT to set up the "svc_aind_chronic" service account, which is the account that all Pirouette systems use.
2. Clone this repository using git clone (may need to generate an ssh key and link it with your GitHub account -- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
3. Clone the lifealert repository (https://github.com/AllenNeuralDynamics/lifealert).
4. Install FFMPEG (https://www.wikihow.com/Install-FFmpeg-on-Windows).
5. Install UV package manager (https://docs.astral.sh/uv/).
6. In the root of the Aind.Behavior.Pirouette and lifealert, execute `uv sync` to install the dependencies denoted in the uv.lock file.
7. Regenerate the Bonsai environment in the Pirouette repo by running `setup.ps1` from the `./bonsai` directory.
8. Generate the rig.json, session.json, and task.json configuration files by running example.py found within the examples directory (update the content to reflect current experimental parameters, like device IDs).
---
### 2. Pirouette Bonsai workflow
1.Open Git Bash, navigate to the Aind.Behavior.Pirouette remote directory, and luanch visual studio.

<img src="https://github.com/user-attachments/assets/5a7f9441-c6d2-4c14-8cb9-c3303e97611e" width="600">

2.Activate the virtual environments by executing `source .venv/Scripts/activate`.

<img src="https://github.com/user-attachments/assets/7dce5ce1-c64f-4ba2-bdc4-c9fc3cbd56ec" width="600">

3.Open Bonsai by running `./Bonsai.exe` within the bonsai directory.

<img src="https://github.com/user-attachments/assets/5bc1bf8e-a49a-4077-ac94-ea70eb1c1bfb" width="600">

4.Open the desired Pirouette script from the `./src` directory ("WrappedPirouette.bonsai" as of 5/15/2025).

<img src="https://github.com/user-attachments/assets/56c56e8d-2e13-40f8-a00c-e6d33f334e4d" width="600">

5.Load the Neuropixels 2.0 probe configuration file using the GUI that appears after double clicking on the "Headstage Neuropixel V2e" operator, which is located `pirouette/hardware/onix`. Also, make sure that the "Channel Presets" is set to "AllShanks0_95"(bottom sites on each shank). Note that the Probe Interface file (needed for SpikeInterface and compression) can be saved in the way that the image shows.

<img src="https://github.com/user-attachments/assets/fcf3011b-8dea-499d-b394-9c06df305576" width="600">
<img src="https://github.com/user-attachments/assets/c74938f6-3196-4742-be1d-0dee4f397000" width="600">

6.Check that the read block size in the StartAcquistion operator is set to 1048576 bytes.
7.Test the workflow before plugging in a mouse by instead plugging in the broken probe into the headstage, and launching the Bonsai workflow by pressing the start button. Check that the commutator rotates in the same direction as the probe.

<img src="https://github.com/user-attachments/assets/80d15458-45ee-46fb-9383-4ff0f4c95408" width="600">

8.Before proceeding, launch lifealert (see section below). 

9.Plug the probe implanted in the mouse's brain into the headstage.

10.While holding the mouse, press "Start" (green arrow) to launch the workflow and turn on commutation. Confirm that the commutator is working.

11.Begin the experiment by placing the mouse in the behavior box.

---
### 3. Lifealert
1.Open Git Bash, navigate to the lifealert remote directory, and luanch visual studio.
2.Activate the virtual environments by executing `source .venv/Scripts/activate`.
3.Lauch the alert system by running `uv run .\src\lifealert\listner.py`. Once the Pirouette Bonsai workflow is started, a "heart beat" will be detected, which will be displayed in the command terminal where listener.py was run. 

<img src="https://github.com/user-attachments/assets/e27c959c-ba8a-4b1e-ae97-769a64c126b3" width="600">

4.If an error occurs in Bonsai that stops the workflow, the error message and lack of heart beats (in 60 s intervals) will be displayed in the terminal. Note that the error and missing heart beats will be sent to the "Chronic Alerts" teams channel and as emails using PowerAutomate. 

---
### 4. Neural activity visualization
Visualiztion of neural activity is done on the surgery computer in Lab 343. The directories of interest are located on the desktop and called "LOAD BONSAI-ONIX STREAM IN SPIKEGLX" and "LOAD BONSAI-ONIX STREAM IN OPENEHPYS". Below are instructions for the recommended way of visualizing data in SpikeGLX, but at the root of both directories is an "instructions.txt" file that can be used for visualizing data collected using Bonsai and Onix. 

1.Copy .bin file that was collected using the Onix system to: \test-day7-Tuesday-May-13-g0\test-day7-Tuesday-May-13_g0_imec0 (Ignore the date, it doesn't matter for visualization).

2.Rename the .bin file to test-day7-Tuesday-May-13-g0_t0.imec0.ap.bin (if there was a previous file with that name, append something relevant to that file, like "_OLD".

3.The fileSizeBytes parameter within the .meta file needs to be updated to the number of bytes the .bin file is, which can be found by looking at the files properties. 

4.Open SpikeGLX, File -->New Acquistion.

5.If slot 40 isn't already available, click Configure Slots and add 40 (i.e. the simulation slot).

6.In the probe table, enable slot 40, Port 1, Dock 1, and disable everything else.

7.Click "Detect" and then "Run".

8.Plot with the following settings: 300-INF filtering, <Tn> enabled, Glb Dmx, and BinMax enabled.

9.The recording neural activity can now be played from beginning to end.

10.OPTIONAL: the file can be also opened in SpikeGLX by File --> Open File Viewer. Select the .bin file, and plot with the following settings: 300-INF filtering, <Tn> enabled, Glb Dmx, and BinMax "Faster".
