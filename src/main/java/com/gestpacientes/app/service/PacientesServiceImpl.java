package com.gestpacientes.app.service;

import com.gestpacientes.app.model.mysql.FarmacosPacientes;
import com.gestpacientes.app.model.mysql.Pacientes;
import com.gestpacientes.app.repository.mysql.PacientesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class PacientesServiceImpl implements PacientesService {
    @Autowired
    private PacientesRepository pacientesRepository;

    @Override
    public List<Pacientes> listarTodos() {
        return pacientesRepository.findAll();
    }

    @Override
    public Optional<Pacientes> buscarPacientes(Long id) {
        return pacientesRepository.findById(id);
    }

    @Override
    public Pacientes guardarPacientes(Pacientes paciente) {
        return  pacientesRepository.save(paciente);
    }

    @Override
    public void borrarPacientes(Pacientes paciente) {
        pacientesRepository.delete(paciente);
    }


    public Pacientes asignarValores (Long id,  Pacientes paciente) {
        Pacientes pacienteBD = pacientesRepository.findById(id).orElse(null);

        if (pacienteBD !=null) {
            pacienteBD.setNombre(paciente.getNombre());
            pacienteBD.setEmail(paciente.getEmail());


            pacienteBD.setFarmacosPacientesList(paciente.getFarmacosPacientesList());
        }

        return pacienteBD;
    }

    public Pacientes guardaListaFarmacos(Long id, FarmacosPacientes farmacosPaciente) {
        Pacientes pacienteBD = pacientesRepository.findById(id).orElse(null);
        List<FarmacosPacientes> farmacosPacientesList = new ArrayList<FarmacosPacientes>();

        if (pacienteBD !=null) {
            farmacosPacientesList = pacienteBD.getFarmacosPacientesList();
            farmacosPacientesList.add(farmacosPaciente);

            pacienteBD.setFarmacosPacientesList(farmacosPacientesList);
        }
        return pacientesRepository.save(pacienteBD);
    }


}
