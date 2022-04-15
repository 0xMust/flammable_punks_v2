import { useEffect, useState } from "react";
import {
  connectWallet,
  getCurrentWalletConnected, mintPunks, rescuePunk, murderPunk
} from "./utils/interact.js";


const Minter = (props) => {

  //State variables
  const [walletAddress, setWallet] = useState("");
  const [status, setStatus] = useState("");
  const [quantity, setQuantity] = useState(0);
  const [tokenId, setTokenId] = useState(0);

  function addWalletListener() {
    if (window.ethereum) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
          setWallet(accounts[0]);
          setStatus("");
        } else {
          setWallet("");
          setStatus("");
        }
      });
    } else {
      setStatus("");
    }
  };

  useEffect(async () => {
    const { address, status } = await getCurrentWalletConnected();
    setWallet(address);
    setStatus(status);

    addWalletListener();
  }, []);

  const connectWalletPressed = async () => {
    const walletResponse = await connectWallet();
    setStatus(walletResponse.status);
    setWallet(walletResponse.address);
  };

  const onMintPressed = async () => {
    const { status } = await mintPunks(quantity);
    setStatus(status);
  };

  const onRescuePressed = async () => {
    const rescueResponse = await rescuePunk(tokenId);
  };

  const onMurderPressed = async () => {
    const murderResponse = await murderPunk(tokenId);
  };

  return (
    <div className="Minter">
      <button id="walletButton" class="font-effect-fire" onClick={connectWalletPressed}>
        {walletAddress.length > 0 ? (
          "Connected: " +
          String(walletAddress).substring(0, 6) +
          "..." +
          String(walletAddress).substring(38)
        ) : (
          <span>Connect Wallet</span>
        )}
      </button>

      <h1 id="title" class="font-effect-fire">Flammable Punks V2</h1>
      <form>
        <input
          type="text"
          placeholder="Quantity (Max: 5)"
          onChange={(event) => setQuantity(event.target.value)}
        />
      </form>
      <button id="mintButton" class="font-effect-fire" onClick={onMintPressed}>
        Mint
      </button>

      <form>
        <input
          type="text"
          placeholder="Token ID"
          onChange={(event) => setTokenId(event.target.value)}
        />
      </form>
      <button id="mintButton" class="font-effect-fire" onClick={onRescuePressed}>
        Rescue
      </button>
      <form>
        <input
          type="text"
          placeholder="Token ID"
          onChange={(event) => setTokenId(event.target.value)}
        />
      </form>
      <button id="mintButton" class="font-effect-fire" onClick={onMurderPressed}>
        Murder
      </button>
    </div>
  );
};

export default Minter;
