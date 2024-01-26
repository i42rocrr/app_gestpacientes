package com.gestpacientes.app.controller;

import com.gestpacientes.app.model.mysql.Modelo;
import com.gestpacientes.app.service.ModeloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class ModeloController {
    @Autowired
    private ModeloService modeloService;

    @GetMapping("/pacientes/modelo")
    public String mostrarFormularioDeNuevaEncuesta(Model model){
        model.addAttribute("encuesta",new Modelo());

        return "NuevoModeloForm";
    }

    @PostMapping("/pacientes/modelo/guardar")
    public String predecir(@ModelAttribute Modelo EncuestaModel) {

        System.out.println("Rango de Edad: " + EncuestaModel.getRangoEdad());
        System.out.println("Menopausia: " + EncuestaModel.getMenopausia());
        System.out.println("Tamaño del tumor: " + EncuestaModel.getTamanoTumor());
        System.out.println("Número de gánglios: " + EncuestaModel.getNumGanglios());
        System.out.println("NodeCaps: " + EncuestaModel.getNodeCaps());
        System.out.println("Grado de malignidad: " + EncuestaModel.getGradoMalignidad());
        System.out.println("Mama afectada: " + EncuestaModel.getMama());
        System.out.println("Cuadrante mamario: " + EncuestaModel.getCuadranteMamario());
        System.out.println("Radioterapia: " + EncuestaModel.getRadiacion());

        modeloService.EjecutaPython();

        return "redirect:/OpcionesPacientes";
    }
}
