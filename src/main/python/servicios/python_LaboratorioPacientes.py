import site
import sys
import os
import numpy as np
import java
from typing import List


Pacientes = java.type("com.gestinterna.app.model.mysql.Pacientes")
Laboratorios = java.type("com.gestinterna.app.model.postgresql.Laboratorios")


class python_LaboratorioPacientes:
    @staticmethod
    def buscaPacientes(laboratorio: Laboratorios, pacientes: List[Pacientes]) -> List[Pacientes]:
        farmacos_laboratorio = np.array(list(map(lambda skill: 1, laboratorio.farmacosLaboratoriosList())))

        farmacos_pacientes = {
            paciente: generaArray(paciente.getfarmacosPacientesList(), laboratorio.farmacosLaboratoriosList())
            for paciente in pacientes
        }

        distances = {
            paciente: np.linalg.norm(farmacos_laboratorio - listadoFarmacos)
            for paciente, listadoFarmacos in paciente_vectors.items()
        }

        listaOrdenada = dict(sorted(distances.items(), key=lambda distance: distance[1]))

        return list(listaOrdenada.keys())

def generaArray(farmacosPaciente, farmacosBuscados):
    return np.array(list(map(lambda farmaco: int(farmaco in farmacosPaciente), farmacosBuscados)))