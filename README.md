# Asset Provenance dApp 🔗

This is a decentralized web application (dApp) built using **Solidity**, **Flask**, and **Web3.py** that manages the lifecycle of electronic assets. It allows users to register a device, transfer ownership, and log service history, with all actions recorded immutably on the Ethereum blockchain.

## 📌 Features

- ✅ Register a device with model and warranty period  
- 🔄 Transfer ownership securely on-chain  
- 🛠️ Add service events to device history  
- 🔍 View registered device details  
- 📚 Track full service history  

## 🧠 Smart Contract (Solidity)

The smart contract includes:
- `registerDevice`: Adds a device to the blockchain  
- `transferOwnership`: Lets current owner transfer the device  
- `addServiceEvent`: Records maintenance events  
- `getDevice`: Retrieves device data  
- `getServiceEvent`: Retrieves individual service events  

## 🛠 Technologies Used

- **Solidity** – for smart contract logic  
- **Ganache** – local Ethereum blockchain  
- **Web3.py** – for Python and Ethereum interaction  
- **Flask** – for backend and routing  
- **HTML/CSS (Jinja2 templates)** – for frontend  
- **MetaMask** – for managing blockchain wallet  

## 🔄 Workflow

1. User registers device using serial number and warranty
2. Owner can transfer ownership to another address
3. Service centers can log maintenance history
4. Users can view asset history and metadata

## 🌐 Deployment

- Local testing with Ganache
- Can be migrated to Sepolia/Testnet using Infura and MetaMask

## 📸 Screenshots

_Add screenshots of your running Flask frontend or contract deployment here_

## 📚 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/manali-dhamale/Asset_provenance.git
   cd Asset_provenance
