import koios_api

# Total number of epochs on Cardano blockchain

epoch_list = [ e["epoch_no"] for e in koios_api.get_epoch_info()]

print("The number of epochs : ")
print(len(epoch_list))

# Get a List of 2 latest blocks in descending order

blocks_list = [ b["hash"] for b in koios_api.get_blocks(2) ]

# Get the list of transactions for a specific block
# Using list comprehension and API method to extract list of transaction hashes
tx_list = [tx['tx_hash'] for tx in koios_api.get_block_txs("8e33bb588feff6414469779d724923064688615535280f8982c9981410cd06f6")]

print(tx_list)

# Detailed information on each transaction

for t in tx_list:
    # Calling API method to get transaction data
    print(koios_api.get_tx_info(t))