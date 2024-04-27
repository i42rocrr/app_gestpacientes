package com.gestpacientes.app.controller;

import com.gestpacientes.app.model.Modelo;
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

    List<String> datosPrediccion;

    @GetMapping("/pacientes/modelo")
    public String mostrarFormularioDeNuevaEncuesta(Model model){
        model.addAttribute("encuesta",new Modelo());

        return "NuevoModeloForm";
    }

    @PostMapping("/pacientes/modelo/guardar")
    public String predecir(@ModelAttribute Modelo EncuestaModel) {
        try {

            // El usuario habrá configurado los parámetros de su tumor anterior a través del formulario
            // "NuevoModeloForm". Todos estos valores se recogerán y se almacenarán en el fichero
            // "datosPaciente.csv" (si no existe, lo crea), que se ubicará en la ruta "src/main/python/recursos/".
            // El programa python "HazPrediccion.py" tomará ese fichero y lo usará para predecir el resultado y
            // las medidas de calidad de los diferentes modelos de Machine learning que haya usado
            //  (árbol de decisión, K-Neibourght, Naive-Bayes, RandonForest, etc).

            // La función "EjecutaPython", del service llamado "modeloService", ejecutará el programa python
            // "HazPrediccion.py" (nombre de fichero que se pasará como parámetro),
            // El programa python creará los modelos de Machine Learning entrenándolos con los datos del dataset
            // "Breast Cancer" (repositorio "ucirepo"), que almacenará en el fichero "datosPaciente_X.csv". Una vez
            // creados y entrenados los modelos mencionados, tomará los datos de este formulario, que se han
            // almacenado en el fichero "datosPaciente.csv" y hará la predicción correspondiente. El resultado de esa
            // predicción la almacena en el fichero "resultados.txt". Este service, a través de esta función "predecir"
            // abre ese fichero "resultados.txt", y lo lee línea a línea, almacenando esos resultados en el array
            // "datosPrediccion" que será el que se recorra para enviar cada uno de esos elementos a la vista
            // redirigiendo este @PostMapping "/pacientes/modelo/guardar" al @GetMapping "/pacientes/modelo/Resultado"
            // que abrirá la vista "ResultadoPrediccion.html", a la que se le pasará el array "datosPrediccion"
            // para que muestre por pantalla los resultados generados en Python.


            // Creación, si no existe, y apertura del fichero "datosPaciente.csv" en donde se van a guardar los datos
            // de este formulario
            String rutaRecursos = "src/main/python/recursos";//Ruta del archivo CSV
            FileWriter fileWriter = new FileWriter(
                    Paths
                        .get(rutaRecursos+"/datosPaciente_X.csv")
                        .toString()
            );


            //Recogida de datos del formulario. El elemento de la vista que tiene esos datos es "EncuestaModel"
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

            //Escritura de los datos del formulario en el fichero "datosPaciente.csv", que se habrá creado si
            // éste aún no estaba creado en el sistema contenedor.
            CSVPrinter csvPrinter = new CSVPrinter(fileWriter,CSVFormat.DEFAULT);
            csvPrinter.printRecords(listaModelo);
            csvPrinter.close();
            fileWriter.close();

            //LLamada a la función del service que va a ejecutar el programa python "HazPrediccion.py"
            modeloService.EjecutaPython("HazPrediccion.py");

            // El programa python ya se ha ejecutado y ha puesto los resultados en el fichero "resultados.txt"
            // Se va a abrir en modo lectura y se va a leer línea a línea, ya que cada línea tiene un valor que
            // debe de mostrarse en la Vista "ResultadoPrediccion.html".
            FileReader fileReader = new FileReader(
                    Paths
                            .get(rutaRecursos+"/resultados.txt")
                            .toString()
            );

            // Una vez abierto el fichero resultados, hay que leerse y almacenar sus valores en un array Java "datosPrediccion",
            // más manejable. Este array es público para esta clase, que queda instanciado aquí ahora y que va a contener
            // los valores resultado.
            /***** Leer el fichero de resultados ******/
            BufferedReader br = new BufferedReader(fileReader);

            datosPrediccion  = new ArrayList<>();
            String contenido;
            while((contenido = br.readLine())!=null) {
                datosPrediccion.add(contenido);
            }
            /***** Fin Leer el fichero de resultados ******/

            fileReader.close();

        } catch(IOException e) {
            e.printStackTrace();
        }

        // Se devuelve el control de la vista al @GetMapping "/pacientes/modelo/Resultado", que ejecutará la función
        // "mostrarResultadosPython" que muestra los resultados por pantalla
        return "redirect:/pacientes/modelo/Resultado";
    }

    @GetMapping("/pacientes/modelo/Resultado")
    public String mostrarResultadosPython(Model model){
        // Muestra en la Vista los resultados de la predicción hecha en el @PostMapping "/pacientes/modelo/guardar",
        //ejecutando la función "predecir".

        //Árbol de decisión
        if (datosPrediccion.get(3).equals("[0]")) {
            model.addAttribute("arbol_prediccion", "Bajo"); //Valor predecido
        } else {
            model.addAttribute("arbol_prediccion", "Alto"); //Valor predecido
        }
        model.addAttribute("arbol_media", datosPrediccion.get(0)); //Media de los resultados del modelo
        model.addAttribute("arbol_sdt", datosPrediccion.get(1)); //Desviación típica de los resultados del modelo
        model.addAttribute("arbol_precision", datosPrediccion.get(2)); //Precisión del modelo
        model.addAttribute("arbol_probacierto", datosPrediccion.get(4)); //Probabilidad de acierto
        model.addAttribute("arbol_precisionmedia", datosPrediccion.get(5)); //Precisión media de los datos


        //Regresión logística
        if (datosPrediccion.get(9).equals("[0]")) {
            model.addAttribute("rl_prediccion", "Bajo"); //Valor predecido
        } else {
            model.addAttribute("rl_prediccion", "Alto"); //Valor predecido
        }
        model.addAttribute("rl_media", datosPrediccion.get(6)); //Media de los resultados del modelo
        model.addAttribute("rl_sdt", datosPrediccion.get(7)); //Desviación típica de los resultados del modelo
        model.addAttribute("rl_precision", datosPrediccion.get(8)); //Precisión del modelo
        model.addAttribute("rl_probacierto", datosPrediccion.get(10)); //Probabilidad de acierto
        model.addAttribute("rl_precisionmedia", datosPrediccion.get(11)); //Precisión media de los datos


        //K-Nearest Neighbours
        if (datosPrediccion.get(15).equals("[0]")) {
            model.addAttribute("kn_prediccion", "Bajo"); //Valor predecido
        } else {
            model.addAttribute("kn_prediccion", "Alto"); //Valor predecido
        }
        model.addAttribute("kn_media", datosPrediccion.get(12)); //Media de los resultados del modelo
        model.addAttribute("kn_sdt", datosPrediccion.get(13)); //Desviación típica de los resultados del modelo
        model.addAttribute("kn_precision", datosPrediccion.get(14)); //Precisión del modelo
        model.addAttribute("kn_probacierto", datosPrediccion.get(16)); //Probabilidad de acierto
        model.addAttribute("kn_precisionmedia", datosPrediccion.get(17)); //Precisión media de los datos


        //Gaussian Naïve Bayes Algorithm
        if (datosPrediccion.get(21).equals("[0]")) {
            model.addAttribute("nb_prediccion", "Bajo"); //Valor predecido
        } else {
            model.addAttribute("nb_prediccion", "Alto"); //Valor predecido
        }
        model.addAttribute("nb_media", datosPrediccion.get(18)); //Media de los resultados del modelo
        model.addAttribute("nb_sdt", datosPrediccion.get(19)); //Desviación típica de los resultados del modelo
        model.addAttribute("nb_precision", datosPrediccion.get(20)); //Precisión del modelo
        model.addAttribute("nb_probacierto", datosPrediccion.get(22)); //Probabilidad de acierto
        model.addAttribute("nb_precisionmedia", datosPrediccion.get(23)); //Precisión media de los datos


        //Random Forest Algorithm
        if (datosPrediccion.get(27).equals("[0]")) {
            model.addAttribute("rf_prediccion", "Bajo"); //Valor predecido
        } else {
            model.addAttribute("rf_prediccion", "Alto"); //Valor predecido
        }
        model.addAttribute("rf_media", datosPrediccion.get(24)); //Media de los resultados del modelo
        model.addAttribute("rf_sdt", datosPrediccion.get(25)); //Desviación típica de los resultados del modelo
        model.addAttribute("rf_precision", datosPrediccion.get(26)); //Precisión del modelo
        model.addAttribute("rf_probacierto", datosPrediccion.get(28)); //Probabilidad de acierto
        model.addAttribute("rf_precisionmedia", datosPrediccion.get(29)); //Precisión media de los datos


        return "ResultadoPrediccion";
    }
}
