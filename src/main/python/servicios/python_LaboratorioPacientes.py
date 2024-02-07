import site
import sys
import os
import numpy as np
import java
from typing import List

Pacientes = java.type("com.gestinterna.app.model.mysql.Pacientes")
Laboratorios = java.type("com.gestinterna.app.model.postgresql.Laboratorios")
class ResultadosPyImpl:
    @staticmethod
    def buscaPacientes(laboratorio: Laboratorios, todosPacientes: List[Pacientes]) -> List[Pacientes]:
        print("Entra en python")

        return list(todosPacientes)

