// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract Payable {

    //This address will be able to send ether
    address payable public owner;

    constructor () {
        owner = payable(msg.sender);
    }

    function deposit() external payable {}

    function getBalance() external view returns (uint) {
        return address(this).balance;
    }
}