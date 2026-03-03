# Automated Network Alert System

This project automates the management and monitoring of Cisco IOS-XE devices using Python.

## Overview

The solution leverages SSH automation to manage network devices, perform configuration backups, monitor interface health, and send real-time alerts to a communication platform.

---

## Key Features

### 1. Automated Configuration Backups
- Connects to Cisco IOS-XE devices using SSH
- Pulls `running-config`
- Saves configurations with timestamps
- Stores backups securely on AWS infrastructure

### 2. Real-Time Health Monitoring
- Audits interface status
- Detects down or unstable interfaces
- Enables proactive network troubleshooting

### 3. Discord Alert Integration
- Sends instant alerts via Discord Webhooks
- Notifies administrators of device or interface issues
- Provides lightweight observability without complex monitoring stacks

---

## Tools & Technologies

- **Python** – Core automation scripting
- **Netmiko** – SSH-based network automation
- **AWS CloudShell / EC2** – Cloud execution and storage
- **Discord API (Webhooks)** – Alerting and notifications

---

## Use Case

This project demonstrates practical network automation skills, cloud integration, and real-time alerting—bridging traditional network engineering with modern DevOps practices.

<img width="771" height="533" alt="Screenshot 2026-03-02 at 10 33 41 PM" src="https://github.com/user-attachments/assets/d8a609bb-62e3-4527-af0e-4908cd11d507" />
