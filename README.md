# Incident Response & Diagnostic Bundler

A lightweight, robust CLI toolkit designed to gather system health signals, redact sensitive information, and bundle support artifacts for faster, safer incident resolution.

## Features

- **Gather System Signals:** Automatically captures process snapshots, memory usage, and disk health (`psutil`).
- **Targeted Log Tailing:** Reads from a custom `config.yml` to extract exactly what support needs.
- **Automated Safeguards:** Uses regex-based redaction to mask sensitive data (IPs, API keys, Emails) before files ever leave the machine.
- **Secure Bundling:** Packages all artifacts into a shareable, timestamped `.tar.gz` archive.
- **Standardized Handoffs:** Generates clean, formatted Post-Incident Reports via interactive prompts.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/venkatasivanaga/incident-runbook-toolkit.git](https://github.com/venkatasivanaga/incident-runbook-toolkit.git)
   cd incident-runbook-toolkit

   ```

2. Set up a Python virtual environment:

```Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```Bash
pip install -r requirements.txt
```

## ⚙️ Configuration
You can optionally pass a YAML configuration file to the toolkit to tell it exactly which logs to tail and which config files to grab.
Create a `config.yml` file anywhere on your system:

```yaml
logs:
  - path: "/var/log/nginx/error.log" # Or C:\logs\app.log on Windows
    lines: 500
  - path: "/var/log/syslog"
    lines: 100
artifacts:
  - "/etc/nginx/nginx.conf"
```

# Incident Response & Diagnostic Bundler 🛠️

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight, robust Command Line Interface (CLI) toolkit designed to gather system health signals, redact sensitive information, and bundle support artifacts for faster, safer incident resolution. 

This tool was built to replace ad-hoc diagnostic scripts with a repeatable, audit-friendly workflow that standardizes engineering handoffs.

## 📑 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [Testing](#-testing)
- [License & Author](#-license--author)

---

## ✨ Features

- **Health Signal Gathering:** Automatically captures process snapshots, memory usage, and disk health using `psutil`.
- **Targeted Log Tailing:** Reads from a customizable `config.yml` to extract exact log lines and configuration files needed by support teams.
- **Automated Safeguards (Redaction):** Uses a regex-based redaction engine to automatically mask sensitive data (IP addresses, API keys, Emails) before files ever leave the host machine.
- **Secure Bundling:** Packages all sanitized artifacts into a shareable, timestamped `.tar.gz` archive for consistent case handling.
- **Standardized Handoffs:** Generates clean, formatted Post-Incident Reports (Markdown or JSON) via interactive CLI prompts to reduce missed details.

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/incident-runbook-toolkit.git
   cd incident-runbook-toolkit
   ```

2. **Set up a Python virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

You can optionally pass a YAML configuration file to the toolkit to tell it exactly which logs to tail and which config files to grab. 

Create a `config.yml` file anywhere on your system:

```yaml
logs:
  - path: "/var/log/nginx/error.log" # Or C:\logs\app.log on Windows
    lines: 500
  - path: "/var/log/syslog"
    lines: 100
artifacts:
  - "/etc/nginx/nginx.conf"
```

---

## 💻 Usage Guide

The toolkit operates via four primary commands. Use the `--help` flag on any command for more details.

### 1. Gather Diagnostics
Collects system diagnostics and copies files specified in your config. Applies redaction automatically to ensure audit-friendly reporting.
```bash
python -m toolkit.cli gather --config config.yml
```
*(Note: To bypass the redaction safeguard, use the `--no-redact` flag).*

### 2. Manual Redaction
If you manually placed files into the `.staging/` directory, you can trigger the regex-based redaction engine independently.
```bash
python -m toolkit.cli redact
```

### 3. Bundle Artifacts
Compresses the sanitized staging area into a timestamped `.tar.gz` file for easy sharing with support and DevOps teams.
```bash
python -m toolkit.cli bundle
```
*(Note: This automatically cleans up the `.staging/` directory unless you pass the `--keep` flag).*

### 4. Generate Post-Incident Report
Launches an interactive prompt to capture timeline, impact, suspected cause, and corrective actions, outputting a standardized Post-Mortem document.
```bash
python -m toolkit.cli report --format markdown
```
*(Supports `--format json` for automated API integrations).*

---

## 🧪 Testing

This project uses `pytest` for unit testing, ensuring the integrity of the redaction engine, bundling logic, and CLI commands.

To run the test suite locally:
```bash
pytest -v
```

---

## 📝 License & Author

**Author:** Venkata Siva Reddy Naga  
**License:** MIT License

*Designed for rapid incident response, support readiness, and robust system diagnostics.*