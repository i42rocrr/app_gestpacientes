package com.gestpacientes.app.service;

import com.gestpacientes.app.model.mysql.FarmacosPacientes;
import com.gestpacientes.app.model.mysql.Pacientes;
import com.gestpacientes.app.repository.mysql.FarmacosPacientesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class FarmacosPacientesServiceImpl implements FarmacosPacientesService {
    @Autowired
    private FarmacosPacientesRepository farmacosPacientesRepository;

    public List<FarmacosPacientes> listarTodos(){return farmacosPacientesRepository.findAll();}

    public Optional<FarmacosPacientes> buscarFarmacosPacientes(Long id){return farmacosPacientesRepository.findById(id);}

    public FarmacosPacientes guardarFarmacosPacientes(FarmacosPacientes farmacosPacientes) {return farmacosPacientesRepository.save(farmacosPacientes);}

    public void borrarFarmacosPacientes(FarmacosPacientes farmacosPacientes){farmacosPacientesRepository.delete(farmacosPacientes);}


    public FarmacosPacientes guardaListaPacientes(Long id, Pacientes paciente) {
        FarmacosPacientes farmacoPacienteBD = farmacosPacientesRepository.findById(id).orElse(null);
        List<Pacientes> PacientesList = new ArrayList<Pacientes>();
        //List<Pacientes> PacientesList;

        if (farmacoPacienteBD !=null) {
            //PacientesList = farmacoPacienteBD.getPacientesList();
            PacientesList.add(paciente);
            farmacoPacienteBD.setPacientesList(PacientesList);
        }

        farmacoPacienteBD = farmacosPacientesRepository.save(farmacoPacienteBD);
        return  farmacoPacienteBD;
    }

}
