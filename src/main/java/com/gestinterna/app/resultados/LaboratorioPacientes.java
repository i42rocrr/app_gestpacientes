package com.gestinterna.app.resultados;

import com.gestinterna.app.model.mysql.Pacientes;
import com.gestinterna.app.model.postgresql.Laboratorios;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class LaboratorioPacientes {
    Laboratorios laboratorio;
    List<Pacientes> listaPacientes;
}
