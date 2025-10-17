# aind-behavior-pirouette

![CI](https://github.com/AllenNeuralDynamics/Aind.Behavior.Pirouette/actions/workflows/pirouette-cicd.yml/badge.svg)
<!-- [![PyPI - Version](https://img.shields.io/pypi/v/aind-behavior-pirouette)](https://pypi.org/project/aind-behavior-pirouette/) -->
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

A repository with source code for long-term, freely moving, electrophysiology recordings in mice.

---

## 🔧 Prerequisites

[Pre-requisites for running the project can be found here](https://allenneuraldynamics.github.io/Aind.Behavior.Services/articles/requirements.html).

---

## 🚀 Deployment

For convenience, once third-party dependencies are installed, `Bonsai` and `python` virtual environments can be bootstrapped by running:

```powershell
./scripts/deploy.ps1
```

from the root of the repository.

## ⚙️ Generating settings files

The Pirouette platform is instantiated by a set of two settings files that strictly follow a DSL schema. These files are:

- `rig.json`
- `session.json`

Examples on how to generate these files can be found in the `./Examples` directory of the repository. Once generated, these are the the only required inputs to run the Bonsai workflow in `./src/main.bonsai`.

The workflow can thus be executed using the [Bonsai CLI](https://bonsai-rx.org/docs/articles/cli.html):

```powershell
"./bonsai/bonsai.exe" "./src/main.bonsai" -p SessionPath=<path-to-session.json> -p RigPath=<path-to-rig.json>
```

## [> ] CLI tools

The platform exposes a few CLI tools to facilitate various tasks. Tools are available via:

```powershell
uv run pirouette <subcommand>
```

for a list of all sub commands available:

```powershell
uv run pirouette -h
```

## 🔄 Regenerating schemas

DSL schemas can be modified in `./src/aind_behavior_pirouette/rig.py`.
Once modified, changes to the DSL must be propagated to `json-schema` and `csharp` API. This can be done by running:

```powershell
uv run pirouette regenerate
```
