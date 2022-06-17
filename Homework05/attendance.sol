/*************
By: Jeasika López
    A00821873
Contrato para tomar asistencia
**************/

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract ProofOfAttendance {
    
    address owner;
  
    struct Student {
        string matricula;
        address addreStudent;
    }

    Student[] Students;

    //Evento para saber si asistio el estudiante
    event studentsRegistered(string mat, address addressStudent);

    mapping(address => bool[16]) attendance;

    //Funcion para registrar un estudiante por medio de un numero id, su address y su matricula
    function RegisterStudent(uint sNum, address sId, string sMatricula)  public {
        Student student = Student(sMatricula, sId);
        Students[sNum] = student;
        emit studentsRegistered(sMatricula, sId);
    }

    //Funcion para eliminar un estudiante por medio de su numero id en la lista
    function DeleteStudent(uint sNum) public {
      delete students[sNum];
    }

    //Funcion para registrar la asistencia del estudiante por medio de su address, matricula, el dia y si assitio o no por un booleano
    function RegisterAttendance(address sId, string sMatricula, uint day, bool attended) view public {
        //Pasar lista por medio del id
        for (uint i=0; i<Students.length; i++) {
            if (Students[i].addreStudent == address sId){
                attendance(sId)[day] = attended;
            }    
        }   
    }

}