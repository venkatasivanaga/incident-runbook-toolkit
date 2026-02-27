# Incident Response & Diagnostic Bundler

A lightweight CLI toolkit designed to gather system health signals, redact sensitive information, and bundle support artifacts for faster incident resolution.

## Features
- **Gather:** Captures process snapshots, disk/memory health, and tails log files.
- **Redact:** Automatically masks sensitive data (IPs, API keys) before bundling.
- **Bundle:** Packages artifacts into a shareable, timestamped `.tar.gz` archive.
- **Report:** Generates standardized post-incident reports.