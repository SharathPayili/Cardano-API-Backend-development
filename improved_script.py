import koios_api

# Function to retrieve all epochs with error handling
def fetch_epochs():
    try:
        epochs = koios_api.get_epoch_info()
        epoch_list = [e["epoch_no"] for e in epochs]
        return epoch_list
    except Exception as e:
        print(f"Error fetching epochs: {e}")
        return []

# Function to retrieve the latest blocks with additional block details
def fetch_latest_blocks(n=2):
    try:
        blocks = koios_api.get_blocks(n)
        blocks_list = [{"hash": b["hash"], "slot_no": b["slot_no"], "block_no": b["block_no"]} for b in blocks]
        return blocks_list
    except Exception as e:
        print(f"Error fetching blocks: {e}")
        return []

# Function to retrieve transactions for a specific block and filter them by certain criteria
def fetch_txs_for_block(block_hash):
    try:
        txs = koios_api.get_block_txs(block_hash)
        # Example: Filter transactions based on certain criteria, e.g., length of the hash
        tx_list = [tx['tx_hash'] for tx in txs if len(tx['tx_hash']) > 60]
        return tx_list
    except Exception as e:
        print(f"Error fetching transactions: {e}")
        return []

# Function to fetch and process detailed transaction information
def fetch_and_process_tx_info(tx_list):
    for t in tx_list:
        try:
            tx_info = koios_api.get_tx_info(t)
            # Process the transaction info, e.g., extract certain fields
            print({
                "tx_hash": tx_info.get("tx_hash"),
                "fee": tx_info.get("fee"),
                "inputs_count": len(tx_info.get("inputs", [])),
                "outputs_count": len(tx_info.get("outputs", [])),
            })
        except Exception as e:
            print(f"Error fetching transaction info: {e}")

# Main execution
if __name__ == "__main__":
    # Fetch epochs and print the total number
    epoch_list = fetch_epochs()
    print("The number of epochs: ", len(epoch_list))

    # Fetch latest blocks and print details
    blocks_list = fetch_latest_blocks(2)
    print("Latest blocks:", blocks_list)

    # Fetch transactions for a specific block and print them
    block_hash = "8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6"
    tx_list = fetch_txs_for_block(block_hash)
    print("Transactions in block:", tx_list)

    # Fetch and process detailed information for each transaction
    fetch_and_process_tx_info(tx_list)
