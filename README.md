# Berachain Auto Faucet Claimer


![Logo](https://github.com/maxspxtr/Berachain-Auto-Faucet-Claimer/blob/main/berachain.jpg?raw=true)

Berachain Auto Faucet Claimer is a Python-based automation tool designed to streamline the process of claiming faucet rewards from the Berachain network. By automating regular claims, This bot ensures that your specified wallet address receives periodic faucet rewards without the need for manual interaction. This tool is built for users who want hands-free management of faucet claims, particularly those interested in maintaining steady Berachain liquidity.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scheduler Setup](#scheduler-setup)
- [Contributing](#contributing)
- [License](#license)


## Installation

1. **Clone the Repository:**
   ```bash
      git clone https://github.com/maxspxtr/BerachainAutoFaucetClaimer.git
   cd BerachainAutoFaucetClaimer


2. **Install Dependencies:**

- Requires Python 3.6 or higher. 
- You will need to install the `requests` library. This can be done easily with pip:

   ```bash  
      pip install -r requirements.txt
   ```

## Usage

1. **Set Your Wallet Address**:
   -Open `config.py` and set your wallet address.
   ```python
   WALLET_ADDRESS = "0xYourWalletAddress"
   
2.  **Run the Script:**
     ```bash
      python faucet_claim.py
    ```

## Scheduler Setup

For Continuous Operation:
- Windows: Use Task Scheduler to run the script at intervals.
- Linux/macOS: Set up a cron job for periodic claims.

**Example (Windows Task Scheduler)**
Open Task Scheduler, create a new task.
Set the task to run `python faucet_claim.py` at an 8-hour, 10-minute interval.
Choose “Run whether user is logged on or not” to keep it running in the background.


**Example (Linux/macOS Cron Job)**
1. Open the crontab editor:
   ```bash
   crontab -e
   ```
2. Add the following line to run the script every 8 hours and 10 minutes:

   ```bash
   */490 * * * * /usr/bin/python3 /path/to/BerachainAutoFaucetClaimer/faucet_claim.py
   ```

# Contributing

We welcome contributions to **Berachain Auto Faucet Claimer**! To contribute:

To contribute:

1. Fork the Project
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
