package com.gestinterna.app.pythonConf;

import com.gestinterna.app.model.mysql.Pacientes;
import com.gestinterna.app.model.postgresql.Laboratorios;

import java.util.List;

public interface listado_LaboratorioPacientes {
    List<Pacientes> buscaPacientes(Laboratorios laboratorio, Iterable<Pacientes> pacientes);

}
