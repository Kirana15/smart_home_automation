# smart_home_automation
controlling lights at home through voice input
# Home Automation using Python + ESP8266 (HTTP)

This is a smart home automation project where Python sends HTTP requests to an ESP8266 to control home appliances like lights and fans.

## Features
- Voice control using speech recognition
- ESP32 receives HTTP requests and switches devices

## How it works
- Python sends HTTP requests to ESp8266
- ESP8266 reads commands and controls connected devices
- No internet required — works over local Wi-Fi

## Folder Structure
- /python/ → Python scripts
- /Arduino/ → ESP8266 code (.ino)
- README.md → This file

## Requirements
- Python: requests, speech recognition
- Arduino: ESP8266, Wi-Fi library

## Arduino (ESP8266) Setup

This project uses an ESP8266 microcontroller to receive HTTP requests and control devices.

### Libraries Used:
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

## Demo
[Watch Video](https://your-demo-link)

## Author
Kirana BV
