// contracts/build_erc20_token.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/ERC20.sol";

contract SHITToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Doge Shit", "SHIT") {
        _mint(msg.sender, initialSupply);
    }
}