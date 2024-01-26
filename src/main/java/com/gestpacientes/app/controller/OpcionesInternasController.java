package com.gestpacientes.app.controller;

import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;

import java.io.File;
import java.io.IOException;

@Controller
public class OpcionesInternasController {
    ResourceLoader resourceLoader;

    public OpcionesInternasController(ResourceLoader resourceLoader_local) {
        this.resourceLoader = resourceLoader_local;
    }


    @GetMapping("/opcionesInternas/CrearListadoLaboratoriosPacientes")
    public String CrearListadosLaboratoriosPacientes(Model model) {

        try {
            String venvExePath = new File("/graalenv/bin/graalpy")
                    .getPath()
                    .toString();

            Context context = Context
                    .newBuilder("python")
                    .allowAllAccess(true)
                    .allowNativeAccess(true)
                    .option("python.ForceImportSite", "true")
                    .option("python.PythonPath", ".")
                    .option("python.Executable", venvExePath)
                    .build();


            String recursosPython="classpath:servicios";
            Source source = Source
                    .newBuilder(
                            "python",
                            resourceLoader
                                    .getResource(recursosPython + "/HazListaLaboratoriosPacientes.py")
                                    .getFile()
                    )
                    .build();


            context.eval(source);
            Value recogeFuncionPython = context
                    .getBindings("python")
                    .getMember("HazListaPython");

            String valorDevuelto = recogeFuncionPython
                                    .execute()
                                    .toString();
        } catch (IOException ioException) {
            System.out.println("Algo pasó en el Bean de generación del context de python......................");
            System.out.println("-Causa del error: " + ioException.getCause());
            System.out.println("-Mensaje de error: " + ioException.getMessage());
            System.out.println("-Localizado en: " + ioException.getLocalizedMessage());
        }


        return "OpcionesInternas";
    }
}
