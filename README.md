Iot_Project_Epitech
---
*This project was realised for the Epitech 4th year Global Nomad Track module "IoT Architecture".*

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
    - [Lights](#lights)
    - [Temperature](#temperature)
    - [Fluids](#fluids)
- [Thingsboard server](#thingsboard-server)
  - [Launch locally](#launch-locally)
  - [Deploy](#deploy)
  - [Configure the Thingsboard server from scratch](#configure-the-thingsboard-server-from-scratch)
  - [Login to the Thingsboard server](#login-to-the-thingsboard-server)
    - [System Administrator](#system-administrator)
    - [Tenant Administrator](#tenant-administrator)
    - [Customer User](#customer-user)
- [Thinksboard Intern Rules](#thinksboard-intern-rules)
  - [Humidity Alarm](#humidity-alarm)
  - [Temperature Critcal Alarm](#temperature-critcal-alarm)
  - [Temperature Critcal Alarm Cold](#temeperature-major-alamr-cold)
  - [Temperature Critcal Alarm Hot](#temeperature-major-alamr-hot)
  - [Delta Temperature](#delta-temperature)
  - [Alarm Specific Temperature](#alarm-specific-temperature)
- [Example Telemtry Data](#example-telemtry-data)
  - [Temperature Data](#temperature-data)
  - [Light Data](#light-data)
  - [Fluid Data](#fluid-data)


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
The interface is compose of 3 tabs:
- lights,
- temperature,
- fluids.
### Lights
![Lights interface](https://i.ibb.co/3MLKj9g/lights.png)
The light dashboard in the GUI is a web view of the Thingsboard light dashboard.
The dashboard controls the 3 light sensors:
- Switch On/Off (controls only the electricity passed through the light)
- Intensity controller
- Color temperature controller
### Temperature
![Temperature interface](https://i.ibb.co/N79Y55s/Screenshot-5.png)
The temperature dashboard in the GUI is a web view of the Thingsboard Temperature dashboard and is a representation of each data sent by each sensor.
The temperature and humidity data are both represented in a gauge and in a graph showing the variation.
The 3 markers on the chart correspond to each sensor. You can click on any of these markers to view the details of the sensor data.
### Fluids
![Fluids interface](https://i.ibb.co/tJ1LW4W/Screenshot-6.png)
The fluids lets you control 3 fluid sensors:
- an ink color sensor,
- a flow sensor (in milliliters per second),
- a fluid substance (=kind) sensor.

This page does not implement the Thingsboard telemetry dashboard for these sensors directly, so there are two ways of accessing it:
- opening the dashboard directly in a web browser thanks to this [link](http://thingsboard.matthieu-rochette.fr/dashboard/a3618da0-4fe4-11ec-96b5-35454323bc15?publicId=e942da30-4dd8-11ec-a7fc-35454323bc15),
- or going to one of the other two pages of the GUI ([Lights](#lights) or [Temperature](#temperature)) and change the dashboard displayed thanks to the menu in the top-right corner of the webview.


---
# Thingsboard server
The thingsboard server is deployed using Docker Compose.
By default, the project uses a web deployment with public dashboards, hosted **[here](http://thingsboard.matthieu-rochette.fr)** (the server might not be available at the moment you read those lines, presumably because the project has become quite old).

## Launch locally
Make sure docker-compose is installed (instructions [here](https://docs.docker.com/compose/install/)).

*Warning: the locally deployed instance will be empty. The configurations, devices etc. available on the publically deployed server will not be available by default.*
Simply run the following command:
```bash
docker-compose up
```
*You can add the `-d` flag to that command if you want to run it in background (detached), which is useful for deployment.*

**Make sure to configure the Device Manager to use the correct URL (in `./DeviceManager/config.py` or via a `./.env` file. For a local deployment, that would be `http://localhost:8080`.**
## Deploy
You can either deploy directly on your server by forwarding the port you want to use in the `./docker-compose.yml` file, or put it behind a reverse proxy (example for NGINX in `./nginx.conf`).

## Configure the Thingsboard server from scratch
If you configure your own Thingsboard instance, you can use the files in `./Thingsboard/` to import dashboards and rules from this project.
However, you will have to manually create the devices (a total of 9: 3 lights, 3 temperature sensors, 3 fluid sensors (1 of each kind)) and configure the GUI manually with the correct access tokens (cf. [this section](#configure-the-device-manager)).

## Login to the Thingsboard server
To access the Thingsboard instance, there are multiple users, with each their own credentials.
### System Administrator
Email: `sysadmin@thingsboard.org`
Password: `sysadmin`
### Tenant Administrator
Email: `tenant@thingsboard.org`
Password: `tenant`
### Customer User
Email: `customer@thingsboard.org`
Password: `customer`

# Thingsboard Intern Rules
Internily to Thingsboard we create rules to verifying the data.
When the data is not corresponding it's create an alarm via the rules.
Depending on the alarm type the alarm severity change.

### Humidity Alarm
The humidity alarm verify if the humidity is above 90%.
If its true we create an alarm.

### Temperature Critcal Alarm
This rule create an alarm when the temperature is invalid.
Invalid temperature is when the temperature is below -10°C and above 35°C.

### Temeperature Major Alamr Cold
When the temperature is between -10°C and -5°C we create an alarm.

### Temeperature Major Alamr Hot
When the temperature is between 30°C and 35°C we create an alarm.

### Delta Temperature
Calculate the delta between the temperature of 10 minutes ago and last temperature.
When the result of the delta is above 20°C an alarm is created.

### Alarm Specific Temperature
When the temperature equal to 0 an alarm is created.

# Example Telemtry Data
All telemetry data is send to thingsboard in JSON format.

### Temperature Data
```json
{
  "temperature": 26.87,
  "humidity": 58
}
```
### Light Data
```json
{
  "state": 1,
  "led": 0,
  "intensity": 67.18,
  "color_temp": 3256
}
```
### Fluid Data
```json
{
  "color": "cyan",
  "substance": "water",
  "flow_in_ml_per_s": 11.98
}
```
