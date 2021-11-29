# 1. Iot_Project_Epitech
This project was realised for the Epitech 4th year Global Nomad Track module "IoT Architecture".
#### 1.0.0.1. Authors
- [Sébastien Collard](https://github.com/SebCOLLARD)
- [Thomas Contini](https://github.com/Recevery)
- [Matthieu Rochette](https://github.com/MatthieuRochette)
  
----
- [1. Iot_Project_Epitech](#1-iot_project_epitech)
      - [1.0.0.1. Authors](#1001-authors)
- [2. Installation](#2-installation)
  - [2.1. Use pre-built binaries (Windows 10 or Ubuntu)](#21-use-pre-built-binaries-windows-10-or-ubuntu)
    - [2.1.1. Download](#211-download)
    - [2.1.2. Instructions](#212-instructions)
    - [2.1.3. Availability](#213-availability)
  - [2.2. Build from source](#22-build-from-source)
    - [2.2.1. Prerequisites](#221-prerequisites)
      - [2.2.1.1. Python 3.9+](#2211-python-39)
      - [2.2.1.2. cx_Freeze](#2212-cx_freeze)
    - [2.2.2. Commands](#222-commands)
  - [2.3. Use from source](#23-use-from-source)
- [3. Setup the development environment](#3-setup-the-development-environment)
  - [3.1. Use a virtual environment](#31-use-a-virtual-environment)
    - [3.1.1. Windows](#311-windows)
      - [3.1.1.1. Powershell](#3111-powershell)
      - [3.1.1.2. Old CMD](#3112-old-cmd)
    - [3.1.2. Linux / MacOS](#312-linux--macos)
  - [3.2. Install dependencies](#32-install-dependencies)
  - [3.3. Launch the program](#33-launch-the-program)
  - [Configure the project](#configure-the-project)
  
-----------
# 2. Installation
## 2.1. Use pre-built binaries (Windows 10 or Ubuntu)
### 2.1.1. Download
You can download pre-built binaries [from here](https://github.com/SebCOLLARD/Iot_Project_Epitech/releases).
### 2.1.2. Instructions
Download the ZIP file, unzip it in a folder on your PC and run the executable from inside that folder. You can also create a link to this executable in order to execute it from a remote location (like your desktop).
### 2.1.3. Availability
Currently, pre-built binaries are availables for Windows 10 (64 bits) and Ubuntu (64 bits).
## 2.2. Build from source
If your OS or processor architecture is not supported, you can also choose to build from the source code.
### 2.2.1. Prerequisites
#### 2.2.1.1. Python 3.9+
You can find [here](https://wiki.python.org/moin/BeginnersGuide/Download) detailed instructions about installing Python on your machine. Make sure to use Python 3.9+, because this project depends on PySide6 (Python implementation for Qt6) which requires this version. Although it might also work with older versions, there is no guarantee.
#### 2.2.1.2. cx_Freeze
We use cx_Freeze for packaging the executable. This library has different dependencies depending on the OS, which you can find [here](https://cx-freeze.readthedocs.io/en/latest/installation.html#others-requirements).
### 2.2.2. Commands
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
## 2.3. Use from source
Finally, if you are using a system that is not supported by cx_Freeze (such as ARM architecture like the recent Apple M1 series processors), you can still try to launch it in developer mode. For that, please refer to the next parts of this document. Alternatively, you can try to find another tool that supports your architecture and is compatible with Qt6's [deployment requirements](https://doc.qt.io/qtforpython/deployment.html).
# 3. Setup the development environment
## 3.1. Use a virtual environment
```bash
python -m venv venv/
```
### 3.1.1. Windows
#### 3.1.1.1. Powershell
```powershell
.\venv\Scripts\activate.ps1
```
#### 3.1.1.2. Old CMD
```batch
.\venv\Scripts\activate.bat
```
### 3.1.2. Linux / MacOS
```bash
source venv/bin/activate
```
## 3.2. Install dependencies
```bash
pip install -r ./requirements.txt
```
## 3.3. Launch the program
```bash
python ./main.py
```
## Configure the project
There are 3 main places to configure the project:
- 1. The `./PyOneDark_settings.json` file (only for the GUI)
- 2. The `./DeviceManager/config.py` file (or a `.env` file at the root of the repo, but it's only used for development settings, as it is not copied to the executable directory by cx_Freeze) that contains all the URLs, tokens, etc.
- 3. The `./docker-compose.yml` file for the Thingsboard server's configuration.