package com.gestpacientes.app.controller;

import com.gestpacientes.app.model.mysql.FarmacosPacientes;
import com.gestpacientes.app.model.mysql.Pacientes;
import com.gestpacientes.app.service.FarmacosPacientesService;
import com.gestpacientes.app.service.PacientesService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;


@Controller
public class PacientesController {
    @Autowired
    private PacientesService pacientesService;
    @Autowired
    private FarmacosPacientesService farmacosPacientesService;

    private Pacientes paciente;

/////////////////////////////////////////////////////////////////////////////////////
    @GetMapping("/pacientes/alta")
    public String mostrarFormularioDeNuevoPaciente(Model model){

        paciente= new Pacientes();

        model.addAttribute("paciente",paciente);

        return "NuevoPacienteForm";
    }

    @PostMapping("/pacientes/alta/guardar")
    public String guardarNuevoPaciente(@ModelAttribute Pacientes pacienteModel) {

        pacienteModel.setNombre(pacienteModel.getNombre().toUpperCase().trim());
        pacienteModel.setEmail (pacienteModel.getEmail().toUpperCase().trim());


        pacientesService.guardarPacientes(pacienteModel);
        paciente = pacientesService.asignarValores(pacienteModel.getId(),pacienteModel);


        return "redirect:/pacientes/farmacos";
    }
///////////////////////////////////////////////////////////////////////////////////

    @GetMapping("/pacientes/farmacos")
    public String mostrarFormularioDeNuevosFarmacos(Model model){



        model.addAttribute("paciente",paciente);
        model.addAttribute("farmacosList", paciente.getFarmacosPacientesList());
        model.addAttribute("nuevoFarmaco",new FarmacosPacientes());


        return "AdherirFarmacosPacientesForm";
    }

    @PostMapping("/pacientes/farmacos/guardar")
    public String guardarNuevoFarmaco(@ModelAttribute FarmacosPacientes farmacosPacientesModel) {
        FarmacosPacientes farmacosPaciente;
        List<FarmacosPacientes> farmacosPacientesList = new ArrayList<FarmacosPacientes>();

        farmacosPacientesModel.setNombre (farmacosPacientesModel.getNombre().toUpperCase().trim());

        farmacosPaciente  = farmacosPacientesService.guardarFarmacosPacientes(farmacosPacientesModel);
        farmacosPacientesService.guardaListaPacientes(farmacosPaciente.getId(), paciente);
        pacientesService.guardaListaFarmacos(paciente.getId(), farmacosPaciente);


        if (paciente.getFarmacosPacientesList() != null) {
            farmacosPacientesList = paciente.getFarmacosPacientesList();
        }
        farmacosPacientesList.add(farmacosPaciente);
        paciente.setFarmacosPacientesList(farmacosPacientesList);


        return "redirect:/pacientes/farmacos";
    }
/////////////////////////////////////////////////////////////////////////////////////////////////////////

    @GetMapping("/pacientes/listartodos")
    public String listarPacientes(Model model){
        List<Pacientes> pacientesList = pacientesService.listarTodos();

        model.addAttribute("pacientesList",pacientesList);


        return "ListadoCompletoPacientes";
    }


    @GetMapping("/pacientes/borrar/{id}")
    public String borrarPaciente(@PathVariable Long id){
        Optional<Pacientes> buscarPacienteBD = pacientesService.buscarPacientes(id);
        if (buscarPacienteBD.isPresent()) {
            Pacientes pacienteBD = buscarPacienteBD.get();

            List<FarmacosPacientes> farmacosPacienteList = pacienteBD.getFarmacosPacientesList();
            if (farmacosPacienteList.isEmpty()==false) {
                for (int i = 0; i < farmacosPacienteList.size(); i++) {
                    farmacosPacientesService.borrarFarmacosPacientes(farmacosPacienteList.get(i));
                }
            }
            pacientesService.borrarPacientes(pacienteBD);
        }

        return "redirect:/pacientes/listartodos";
    }

}
