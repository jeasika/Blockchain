// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol"; //Se usa la libreria de OpenZeppelin.

//
contract Token is ERC20{ //El contract es especificado que sea token ERC20.


    address public admin;
    constructor(uint256 initialSupply) ERC20 ("Business Token", "BTN"){ //Se crea el token que va utilizar el dueño
        _mint(msg.sender, initialSupply); //Initial supply va ser la cantidad de tokens que sean creados.
        admin = msg.sender;
    }

    function mint(address to, uint amount) external{ //Mint permite aumentar la oferta total del token.
        require(msg.sender == admin, "only admin"); //Admin solo tiene permiso de hacer esto.
        _mint(to, amount);
    }

    function burn (uint amount) external{ //Permite destruir permamentemente un token.
        _burn(msg.sender, amount);

    }


}