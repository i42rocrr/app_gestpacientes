package com.gestpacientes.app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class appController {
    @GetMapping("")
    public String verPaginaDeInicio() {
        return "index";
    }

    @GetMapping("/OpcionesPacientes")
    public String verPaginaDeOpcionesPacientes() {
        return "OpcionesPacientes";
    }

    @GetMapping("/OpcionesInternas")
    public String verPaginaDeOpcionesInternas() {
        return "OpcionesInternas";
    }
}
