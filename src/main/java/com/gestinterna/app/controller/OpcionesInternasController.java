package com.gestinterna.app.controller;

import com.gestinterna.app.model.postgresql.Laboratorios;
import com.gestinterna.app.pythonConf.listado_LaboratorioPacientes;
import com.gestinterna.app.repository.mysql.PacientesRepository;
import com.gestinterna.app.repository.postgresql.LaboratoriosRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;

import java.io.File;
import java.io.IOException;
import java.util.List;

@Controller
public class OpcionesInternasController {

    listado_LaboratorioPacientes listado_laboratorioPacientes;

    @Autowired
    private LaboratoriosRepository laboratoriosRepository;

    @Autowired
    private PacientesRepository pacientesRepository;

    @GetMapping("/CrearListadoLaboratoriosPacientes")
    public String CrearListadosLaboratoriosPacientes(Model model) {


        List<Laboratorios> laboratoriosList = laboratoriosRepository.findAll();
        for (int i=0; i<laboratoriosList.size();i++) {

            listado_laboratorioPacientes.buscaPacientes(laboratoriosList.get(i), pacientesRepository.findAll());
        }


        return "ListadoLaboratoriosPacientes";
    }
}
