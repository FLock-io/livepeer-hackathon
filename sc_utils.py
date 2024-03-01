from web3 import Web3

# Connect to the Ethereum node.
web3 = Web3(Web3.HTTPProvider("https://www.your-ethereum-node.com/"))

# Ensure successful connection
if not web3.is_connected():
    print("Failed to connect to Ethereum network!")
else:
    print("Connected to Ethereum network")

# Contract address and ABI (replace these placeholders with actual values)
contract_address = "0xYourContractAddress"
contract_abi = [
    # Contract ABI
]

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


# Call the vote function of the contract, specifying the account from which the transaction is sent
def vote(video_uuid: str, from_address: str):
    # You need to unlock the account or use a signed transaction to send the transaction
    # This is just an example of a call, in practice, you need to handle transaction signing and sending
    tx_hash = contract.functions.vote(video_uuid).transact({"from": from_address})
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Transaction receipt: {receipt}")


# Call the getVotes function of the contract
def get_votes(video_uuid: str) -> int:
    total_votes = contract.functions.getVotes(video_uuid).call()
    print(f"Total votes for video {video_uuid}: {total_votes}")
    return total_votes
