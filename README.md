# Empty Recycle Bin Script

This Python script automatically empties the Recycle Bin on Windows after a specified interval (e.g., once a week). The script uses the Windows Shell API to delete the contents of the Recycle Bin without confirmation or any UI prompts.

## Features

- Empties the Recycle Bin without any user interaction.
- Uses the `ctypes` module to interact with Windows system functions.
- Can be scheduled to run automatically using Windows Task Scheduler.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. **Clone the repository** (or download the script directly):
   ```bash
   git clone https://github.com/kiganyamburu/empty-recycle-bin.git
   cd empty-recycle-bin
