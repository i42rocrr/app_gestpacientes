package com.gestpacientes.app.controller;

import com.gestpacientes.app.model.mysql.Modelo;
import com.gestpacientes.app.service.ModeloService;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import java.io.*;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

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
        try {

            String rutaRecursos = "src/main/python/recursos";//Ruta del archivo CSV
            FileWriter fileWriter = new FileWriter(
                    Paths
                        .get(rutaRecursos+"/datosPaciente.csv")
                        .toString()
            );

            List<String[]> listaModelo = new ArrayList<>();
            listaModelo.add(new String[]{
                            "age",
                            "menopause",
                            "tumor-size",
                            "inv-nodes",
                            "node-caps",
                            "deg-malig",
                            "breast",
                            "breast-quad",
                            "irradiat"
                    }
            );
            listaModelo.add(
                    new String[]{
                            EncuestaModel.getRangoEdad(),
                            EncuestaModel.getMenopausia(),
                            EncuestaModel.getTamanoTumor(),
                            EncuestaModel.getNumGanglios(),
                            EncuestaModel.getNodeCaps(),
                            EncuestaModel.getGradoMalignidad(),
                            EncuestaModel.getMama(),
                            EncuestaModel.getCuadranteMamario(),
                            EncuestaModel.getRadiacion()
                    }
            );

            CSVPrinter csvPrinter = new CSVPrinter(fileWriter,CSVFormat.DEFAULT);
            csvPrinter.printRecords(listaModelo);
            csvPrinter.close();
            fileWriter.close();

            modeloService.EjecutaPython("HazPrediccion.py");

            FileReader fileReader = new FileReader(
                    Paths
                            .get(rutaRecursos+"/resultados.txt")
                            .toString()
            );

            /***** Leer el fichero de resultados ******/

            /***** Leer el fichero de resultados ******/

            fileReader.close();

        } catch(IOException e) {
            e.printStackTrace();
        }



        return "redirect:/OpcionesPacientes";
    }
}
