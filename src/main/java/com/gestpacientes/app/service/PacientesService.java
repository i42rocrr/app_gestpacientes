package com.gestpacientes.app.service;

import com.gestpacientes.app.model.FarmacosPacientes;
import com.gestpacientes.app.model.Pacientes;
import java.util.List;
import java.util.Optional;

public interface PacientesService {

    public List<Pacientes> listarTodos();

    public Optional<Pacientes> buscarPacientes(Long id);

    public Pacientes guardarPacientes(Pacientes paciente);

    public void borrarPacientes(Pacientes paciente);



    public Pacientes asignarValores (Long id,  Pacientes paciente);
    public Pacientes guardaListaFarmacos(Long id, FarmacosPacientes farmacosPaciente);

}
