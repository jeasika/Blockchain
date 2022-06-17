// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "./safemath.sol";

contract ServiciosTecnicos {

    using SafeMath for uint256;
    
    address owner;
    uint nextId;

    struct Tecnico {
        uint id;
        uint contadorServicios; //dar confiabilidad de su historial
        address payable tecnicoAddress;
        string categoria;
        string location;
    }

    Tecnico[] public tecnicos;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    function findIndex(uint _id) internal view returns (uint) {
        for (uint i = 0; i < tecnicos.length; i++) {
            if(tecnicos[i].id == _id){
                return i;
            }
        }
        revert('Tecnico not found');
    }

    /*Funciones que solo puede realizar el owner */
    function createTecnico(uint _contadorServicios, address payable _tecnicoAddress, string memory _categoria, string memory _location) external onlyOwner {
        tecnicos.push(Tecnico(nextId, _contadorServicios, _tecnicoAddress, _categoria, _location));
        nextId++;
    }

    function deleteTecnico(uint _id) external onlyOwner {
        uint index = findIndex(_id);
        delete tecnicos[index];
    }


    /*Funciones que puede realizar cualquier usuario*/
    function readTecnico(uint _id) public view returns (uint, uint, address payable, string memory, string memory) {
        uint index = findIndex(_id);
        return (tecnicos[index].id, tecnicos[index].contadorServicios, tecnicos[index].tecnicoAddress, tecnicos[index].categoria, tecnicos[index].location);
    }

    function addService() external payable {
        //por categoria elegir el personal
        //emitir un evento
        //function que lleve a pagar por el servicio
        //suma del contador del tecnico
    }

}