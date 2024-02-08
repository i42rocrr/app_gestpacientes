package com.gestpacientes.app.service;

import com.gestpacientes.app.model.FarmacosPacientes;
import com.gestpacientes.app.model.Pacientes;
import java.util.List;
import java.util.Optional;

public interface FarmacosPacientesService {
    public List<FarmacosPacientes> listarTodos();

    public Optional<FarmacosPacientes> buscarFarmacosPacientes(Long id);

    public FarmacosPacientes guardarFarmacosPacientes(FarmacosPacientes farmacosPacientes);

    public void borrarFarmacosPacientes(FarmacosPacientes farmacosPacientes);

    public FarmacosPacientes guardaListaPacientes(Long id, Pacientes paciente);
}
