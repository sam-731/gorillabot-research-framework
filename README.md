# GorillaBot Research Framework

A defensive cybersecurity research framework for analyzing
Mirai-based DDoS infrastructures inspired by the GorillaBot paper.

## Features

- Safe C2 protocol emulation
- Netflow analysis
- DDoS traffic classification
- YARA/Suricata detections
- Attack visualization dashboards
- IoT honeypot integration
- Malware evolution tracking

## Research Background

This repository is inspired by the paper:

"From Mirai to Gorilla: Deep Dive into a Long-Lasting DDoS-for-Hire Botnet"

The project focuses ONLY on:
- defensive research
- traffic analysis
- malware reverse engineering
- detection engineering

No offensive tooling is included.

## Architecture

```text
Passive Sensors
      |
      v
Flow Collection ---> Detection Engine ---> Dashboard
      |
      v
Protocol Emulator ---> Attack Classification
