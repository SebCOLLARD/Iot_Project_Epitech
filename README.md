Iot_Project_Epitech
---
*This project was realised for the Epitech 4th year Global Nomad Track module "IoT Architecture".*

---

---

This project creates a graphical user interface emulating IoT devices that communicate with a [Thingsboard](https://thingsboard.io/) server.

Authors
---
- [Sébastien Collard](https://github.com/SebCOLLARD)
- [Thomas Contini](https://github.com/Recevery)
- [Matthieu Rochette](https://github.com/MatthieuRochette)
  

Table of contents
----
- [Device Manager](#device-manager)
  - [Installation](#installation)
    - [Use pre-built binaries (Windows 10 or Ubuntu)](#use-pre-built-binaries-windows-10-or-ubuntu)
      - [Download](#download)
      - [Instructions](#instructions)
      - [Availability](#availability)
    - [Build from source](#build-from-source)
      - [Prerequisites](#prerequisites)
        - [Python 3.9+](#python-39)
        - [cx_Freeze](#cx_freeze)
      - [Commands](#commands)
    - [Use from source](#use-from-source)
  - [Setup the development environment](#setup-the-development-environment)
    - [Use a virtual environment](#use-a-virtual-environment)
      - [Windows](#windows)
        - [Powershell](#powershell)
        - [Old CMD](#old-cmd)
      - [Linux / MacOS](#linux--macos)
    - [Install dependencies](#install-dependencies)
    - [Launch the program](#launch-the-program)
  - [Configure the Device Manager](#configure-the-device-manager)
  - [Interface](#interface)
- [Thingsboard server](#thingsboard-server)
  - [Launch locally](#launch-locally)
  - [Deploy](#deploy)
  


-----------
# Device Manager
## Installation
### Use pre-built binaries (Windows 10 or Ubuntu)
#### Download
You can download pre-built binaries [from here](https://github.com/SebCOLLARD/Iot_Project_Epitech/releases).
#### Instructions
Download the ZIP file, unzip it in a folder on your PC and run the executable from inside that folder. You can also create a link to this executable in order to execute it from a remote location (like your desktop).
#### Availability
Currently, pre-built binaries are availables for Windows 10 (64 bits) and Ubuntu (64 bits).
### Build from source
If your OS or processor architecture is not supported, you can also choose to build from the source code.
#### Prerequisites
##### Python 3.9+
You can find [here](https://wiki.python.org/moin/BeginnersGuide/Download) detailed instructions about installing Python on your machine. Make sure to use Python 3.9+, because this project depends on PySide6 (Python implementation for Qt6) which requires this version. Although it might also work with older versions, there is no guarantee.
##### cx_Freeze
We use cx_Freeze for packaging the executable. This library has different dependencies depending on the OS, which you can find [here](https://cx-freeze.readthedocs.io/en/latest/installation.html#others-requirements).
#### Commands
*This tutorial is made for Debian/Ubuntu-based Linux distributions. Please adapt the steps to your own OS (use dnf instead of apt if you are on Fedora, for example).*
*You python commands may differ depending on your own Python installation.*
1. Change directories to the one corresponding to this directory:
```bash
cd ~/Downloads/Iot_Project_Epitech
```
2. Install the dependencies of the project
```bash
pip install -r ./requirements.txt
```
3. Launch the `setup.py` script
```bash
python ./setup.py build
```
4. Done! Your program is now in the newly-appeared `build` folder at the root of the repository. You can now follow the rest of the [intructions](#instructions) explained earlier in the document.
### Use from source
Finally, if you are using a system that is not supported by cx_Freeze (such as ARM architecture like the recent Apple M1 series processors), you can still try to launch it in developer mode. For that, please refer to the next parts of this document. Alternatively, you can try to find another tool that supports your architecture and is compatible with Qt6's [deployment requirements](https://doc.qt.io/qtforpython/deployment.html).
## Setup the development environment
### Use a virtual environment
```bash
python -m venv venv/
```
#### Windows
##### Powershell
```powershell
.\venv\Scripts\activate.ps1
```
##### Old CMD
```batch
.\venv\Scripts\activate.bat
```
#### Linux / MacOS
```bash
source venv/bin/activate
```
### Install dependencies
```bash
pip install -r ./requirements.txt
```
### Launch the program
```bash
python ./main.py
```
## Configure the Device Manager
There are 3 main places to configure the project:
- 1. The `./PyOneDark_settings.json` file (only for the GUI)
- 2. The `./DeviceManager/config.py` file (or a `.env` file at the root of the repo, but it's only used for development settings, as it is not copied to the executable directory by cx_Freeze) that contains all the URLs, tokens, etc.
- 3. The `./docker-compose.yml` file for the Thingsboard server's configuration.

## Interface
[](https://ibb.co/7R6hZds)

# Thingsboard server
The thingsboard server is deployed using Docker Compose.
By default, the project uses a web deployment with public dashboards, hosted [here](http://thingsboard.matthieu-rochette.fr) (the server might not be available at the moment you read those lines, presumably because the project has become quite old).

## Launch locally
Make sure docker-compose is installed (instructions [here](https://docs.docker.com/compose/install/)).

Simply run the following command:
```bash
docker-compose up
```
*You can add the `-d` flag to that command if you want to run it in background (detached), which is useful for deployment.*

**Make sure to configure the Device Manager to use the correct URL (in `./DeviceManager/config.py` or via a `./.env` file. For a local deployment, that would be `http://localhost:8080`.**
## Deploy
You can either deploy directly on your server by forwarding the port you want to use in the `./docker-compose.yml` file, or put it behind a reverse proxy (example for NGINX in `./nginx.conf`).