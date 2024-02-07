package com.gestinterna.app.controller;

import com.gestinterna.app.model.mysql.Pacientes;
import com.gestinterna.app.resultados.LaboratorioPacientes;
import com.gestinterna.app.resultados.ResultadosPy;
import com.gestinterna.app.service.mysql.PacientesService;
import com.gestinterna.app.service.postgresql.LaboratoriosService;
import com.gestinterna.app.service.postgresql.LaboratoriosServiceImpl;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;

import org.graalvm.polyglot.Value;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;

import java.util.ArrayList;
import java.util.List;


@Controller
public class OpcionesInternasController {

    @Autowired
    private PacientesService pacientesService;

    @Autowired
    private LaboratoriosService laboratoriosService;

    ResultadosPy resultadosPy;

    OpcionesInternasController (ResultadosPy resultadosPy_) {
        this.resultadosPy = resultadosPy_;
    }

    @GetMapping("/CrearListadoLaboratoriosPacientes")
    public String CrearListadosLaboratoriosPacientes(Model model) {
        List<Pacientes> pacientes = resultadosPy.buscaPacientes(laboratoriosService.listarTodos().getFirst(), pacientesService.listarTodos());

        /*
        List<LaboratorioPacientes> laboratorioPacientesList = new ArrayList<>();
        for(int i=0; i<laboratoriosService.listarTodos().size();i++) {
            LaboratorioPacientes laboratorioPacientes = new LaboratorioPacientes();

            laboratorioPacientes.setLaboratorio(laboratoriosService.listarTodos().get(i));
            laboratorioPacientes.setListaPacientes(
                    resultadosPy.buscaPacientes(laboratoriosService.listarTodos().get(i), pacientesService.listarTodos())
            );
            laboratorioPacientesList.add(laboratorioPacientes);
        }
        */
        return "ListadoLaboratoriosPacientes";
    }
}
