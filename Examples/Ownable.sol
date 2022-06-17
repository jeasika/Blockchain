// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

/*Only the owner will be able to set a new owner and 
there will be some functions where only the owner can call*/

contract Ownable {
    address public owner;
    constructor(){
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    function setOwner (address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "invalid address");
        owner = _newOwner;
    }

    function onlyOwnerCanCallThisFunc() external onlyOwner {
        //code
    }

    function anyOneCanCall() external {
        //code
    }

}