from solcx import compile_standard, install_solc
from web3 import Web3
import json

install_solc('0.8.5')
with open("Asset_provenance.sol", "r") as file:
    contract_code = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Asset_provenance.sol": {"content": contract_code}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "metadata",
                        "evm.bytecode",
                        "evm.sourceMap"
                    ]
                },
            }
        }
    },
    solc_version="0.8.5"
)

abi = compiled_sol['contracts']['Asset_provenance.sol']['AssetProvenance']['abi']
# ✅ Save the ABI to a JSON file
with open("abi.json", "w") as abi_file:
    json.dump(abi, abi_file)

bytecode = compiled_sol['contracts']['Asset_provenance.sol']['AssetProvenance']['evm']['bytecode']['object']

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
chain_id = 1337
private_key = "0xe94ce2c4a6c05512012f0b5f482ce281a7afc34a860cdfdb1e1227369a3cc06c"
account = w3.eth.account.from_key(private_key)
my_address = account.address

AssetProvenance = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(my_address)
transaction = AssetProvenance.constructor().build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce,
    "gas": 3000000,
    "gasPrice": w3.to_wei("20", "gwei"),
})
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt['contractAddress']
print(f"Contract Address: {contract_address}")

contract_instance = w3.eth.contract(address=contract_address, abi=abi)

