package com.gestinterna.app.resultados;

import com.gestinterna.app.model.mysql.Pacientes;
import com.gestinterna.app.model.postgresql.Laboratorios;

import java.util.List;

public interface ResultadosPy {
    List<Pacientes> buscaPacientes(Laboratorios laboratorio, List<Pacientes> todosPacientes);
}
