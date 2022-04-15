// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.10;

import {DSTestPlus} from "solmate/test/DSTestPlus.t.sol";
import "../FlammablePunksV2.sol";

interface CheatCodes {
    function expectRevert(bytes calldata expectedError) external;

    function assume(bool) external;
}

contract ContractTest is DSTestPlus {
    FlammablePunksV2 myContract;
    CheatCodes cheats = CheatCodes(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);

    function setUp() public {
        myContract = new FlammablePunksV2();
    }

    function testMint(uint256 quantity) public {
        quantity = bound(quantity, 1, 5);
        myContract.mintPunks(quantity);
    }

    function testMintTooMany(uint256 quantity) public {
        quantity = bound(quantity, 6, 10000);
        cheats.expectRevert("You can only mint 5 punks at a time.");
        myContract.mintPunks(quantity);
    }

    function testMintZero() public {
        cheats.expectRevert("You must mint more than 0 punks");
        myContract.mintPunks(0);
    }

    function testRescuePunk(uint256 quantity, uint256 tokenId) public {
        quantity = bound(quantity, 1, 5);
        tokenId = bound(tokenId, 0, quantity - 1);
        myContract.mintPunks(quantity);
        myContract.rescuePunk(tokenId);
        assertTrue(true);
    }

    function testMurderPunk(uint256 quantity, uint256 tokenId) public {
        quantity = bound(quantity, 1, 5);
        tokenId = bound(tokenId, 0, quantity - 1);
        myContract.mintPunks(quantity);
        myContract.murderPunk(tokenId);
        assertTrue(true);
    }

    function testRescueUnownedPunk(uint256 quantity, uint256 tokenId) public {
        quantity = bound(quantity, 1, 5);
        tokenId = bound(tokenId, 0, quantity - 1);
        myContract.mintPunks(quantity);
        myContract.safeTransferFrom(
            address(this),
            0x42FF331884882726573A6880409138E38dA78C3F,
            tokenId
        );
        cheats.expectRevert(
            "Token not in wallet. To rescue a punk you must own it first."
        );
        myContract.rescuePunk(tokenId);
        assertTrue(true);
    }

    function testMurderUnownedPunk(uint256 quantity, uint256 tokenId) public {
        quantity = bound(quantity, 1, 5);
        tokenId = bound(tokenId, 0, quantity - 1);
        myContract.mintPunks(quantity);
        myContract.safeTransferFrom(
            address(this),
            0x42FF331884882726573A6880409138E38dA78C3F,
            tokenId
        );
        cheats.expectRevert(
            "Token not in wallet. To murder a punk you must own it first."
        );
        myContract.murderPunk(tokenId);
        assertTrue(true);
    }

    function testRescueAlivePunk(uint256 quantity, uint256 tokenId) public {
        quantity = bound(quantity, 1, 5);
        tokenId = bound(tokenId, 0, quantity - 1);
        myContract.mintPunks(quantity);
        myContract.rescuePunk(tokenId);
        cheats.expectRevert(
            "You are too kind, this punk has already been rescued."
        );
        myContract.rescuePunk(tokenId);
        assertTrue(true);
    }

    function testMurderDeadPunk(uint256 quantity, uint256 tokenId) public {
        quantity = bound(quantity, 1, 5);
        tokenId = bound(tokenId, 0, quantity - 1);
        myContract.mintPunks(quantity);
        myContract.murderPunk(tokenId);
        cheats.expectRevert("Please have mercy, this punk is already dead.");
        myContract.murderPunk(tokenId);
        assertTrue(true);
    }

    function testNotEnoughLeft() public {
        uint256 counter = 0;
        while (counter < 9995) {
            myContract.mintPunks(5);
            counter = counter + 5;
        }
        myContract.mintPunks(3);
        cheats.expectRevert("There aren't that many punks left to be saved.");
        myContract.mintPunks(5);
    }

    function testSoldOut() public {
        uint256 counter = 0;
        while (counter < 10000) {
            myContract.mintPunks(5);
            counter = counter + 5;
        }
        cheats.expectRevert("All punks have been rescued!");
        myContract.mintPunks(1);
    }

    function onERC721Received(
        address,
        address,
        uint256,
        bytes calldata
    ) external pure returns (bytes4) {
        return
            bytes4(
                keccak256("onERC721Received(address,address,uint256,bytes)")
            );
    }
    /*
  solved reference: https://docs.klaytn.com/smart-contract/sample-contracts/erc-721/1-erc721#3-safetransferfrom-and-transferfrom
  */
}
