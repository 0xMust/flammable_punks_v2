//require('dotenv').config();
const alchemyKey = process.env.REACT_APP_ALCHEMY_KEY;
const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
const web3 = createAlchemyWeb3(alchemyKey);

const contractABI = require('../contract-abi.json');
const contractAddress = process.env.CONTRACT_ADDRESS;

// Mint PUNKS
export const mintPunks = async (quantity) => {
    if ((quantity <= 0) || (quantity > 5) || (quantity % 1 != 0)) {
        return {
            success: false,
            status: "Please enter the number of punks you want to rescue (up to 5).",
        }
    }


    window.contract = await new web3.eth.Contract(contractABI, contractAddress);

    //set up your Ethereum transaction
    const transactionParameters = {
        from: window.ethereum.selectedAddress, // must match user's active address.
        'data': window.contract.methods.mintPunks(quantity).encodeABI() //make call to NFT smart contract 
    };

    //sign transaction via Metamask
    try {
        const txHash =
            await window.contract.methods.mintPunks(quantity).send(
                transactionParameters
            )
            ;

        return {
            success: true,
            status: "Transaction succesful ✅"
        }
    } catch (error) {
        return {
            success: false,
            status: "😥 Something went wrong: " + error.message
        }
    }
};

// RESCUE PUNKS
export const rescuePunk = async (tokenId) => {

    window.contract = await new web3.eth.Contract(contractABI, contractAddress);

    //set up your Ethereum transaction
    const transactionParameters = {
        from: window.ethereum.selectedAddress, // must match user's active address.
        'data': window.contract.methods.rescuePunk(tokenId).encodeABI() //make call to NFT smart contract 
    };

    //sign transaction via Metamask
    try {
        const txHash =
            await window.contract.methods.rescuePunk(tokenId).send(
                transactionParameters
            )
            ;

        return {
            success: true,
            status: "Transaction succesful ✅"
        }
    } catch (error) {
        return {
            success: false,
            status: "😥 Something went wrong: " + error.message
        }
    }
};


// MURDER PUNKS
export const murderPunk = async (tokenId) => {

    window.contract = await new web3.eth.Contract(contractABI, contractAddress);

    //set up your Ethereum transaction
    const transactionParameters = {
        from: window.ethereum.selectedAddress, // must match user's active address.
        'data': window.contract.methods.murderPunk(tokenId).encodeABI() //make call to NFT smart contract 
    };

    //sign transaction via Metamask
    try {
        const txHash =
            await window.contract.methods.murderPunk(tokenId).send(
                transactionParameters
            )
            ;

        return {
            success: true,
            status: "Transaction succesful ✅"
        }
    } catch (error) {
        return {
            success: false,
            status: "😥 Something went wrong: " + error.message
        }
    }
};

export const connectWallet = async () => {
    if (window.ethereum) {
        try {
            const addressArray = await window.ethereum.request({
                method: "eth_requestAccounts",
            });
            const obj = {
                status: "",
                address: addressArray[0],
            };
            return obj;
        } catch (err) {
            return {
                address: "",
                status: "😥 " + err.message,
            };
        }
    } else {
        return {
            address: "",
            status: "",
        };
    }
};



export const getCurrentWalletConnected = async () => {
    if (window.ethereum) {
        try {
            const addressArray = await window.ethereum.request({
                method: "eth_accounts",
            });
            if (addressArray.length > 0) {
                return {
                    address: addressArray[0],
                    status: "",
                };
            } else {
                return {
                    address: "",
                    status: "",
                };
            }
        } catch (err) {
            return {
                address: "",
                status: "😥 " + err.message,
            };
        }
    } else {
        return {
            address: "",
            status: "",
        };
    }
};

