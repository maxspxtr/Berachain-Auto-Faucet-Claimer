import time
import requests
from datetime import datetime

# URL of the faucet
faucet_url = "https://bartio.faucet.berachain.com/"
# Address to claim for
address = "0xYourWalletAddress"

# Function to claim from the faucet
def claim_faucet():
    try:
        # Send POST request to the faucet endpoint (assuming it's a POST request)
        response = requests.post(faucet_url, json={"address": address})
        
        # Check if the claim was successful
        if response.status_code == 200:
            print(f"[{datetime.now()}] Successfully claimed from faucet for address: {address}")
        else:
            print(f"[{datetime.now()}] Failed to claim from faucet. Status code: {response.status_code}")
            print("Response:", response.text)
    
    except Exception as e:
        print(f"[{datetime.now()}] An error occurred: {str(e)}")

# Scheduler to run the task every 8 hours and 10 minutes
def schedule_faucet_claim():
    while True:
        claim_faucet()
        # Sleep for 8 hours and 10 minutes (8 hours * 3600 seconds + 10 minutes * 60 seconds)
        time.sleep(8 * 3600 + 10 * 60)

# Start the scheduler
if __name__ == "__main__":
    schedule_faucet_claim()
