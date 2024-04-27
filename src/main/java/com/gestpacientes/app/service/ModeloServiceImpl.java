package com.gestpacientes.app.service;

import com.gestpacientes.app.model.Modelo;
import com.gestpacientes.app.repository.ModeloRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;

import java.util.List;
import java.util.Optional;

@Service
public class ModeloServiceImpl implements ModeloService {
    @Autowired
    private ModeloRepository modelosRepository;

    public List<Modelo> listarTodos(){return modelosRepository.findAll();}
    @Override
    public Optional<Modelo> buscarModelo(Long id){return modelosRepository.findById(id);}

    @Override
    public Modelo guardarModelos(Modelo modelo){return modelosRepository.save(modelo);}

    @Override
    public void borrarModelos(Modelo modelo){modelosRepository.delete(modelo);}

    @Override
    public void EjecutaPython(String nombreFicheroPython){

        //Función que se encarga de crear el contexto adecuado para enviar al sistema contenedor el programa
        // python que se quiera ejecutar. El sistema operativo tomará el control de la ejecución y se lo
        // devolverá al programa nuevamente una vez que el programa python haya terminado de ejecutarse.
        try {
            // El sistema programado está preparado para llamar a esta función del service "EjecutaPython"
            // para que ejecute el programa python que queramos. Esta función "EjecutaPython", recibe
            // como parámetro, una cadena de texto "nombreFicheroPython" con el nombre del fichero Python
            // a ejecutar. Por tanto, desde e controller, en este caso desde "ModeloController",
            // se puede llamar a esta función "EjecutaPython", del service "ModeloServiceImpl",
            // tantas veces se quiera para ejecutar tantos programas python como se requiera.
            // En este caso, para este programa Java sólo se va a ejecutar el programa "HazPrediccion.py"

            //Se configura el recurso python (el fichero python a ejecutar) como un Java
            String ficheroPython = new File("/src/main/python/servicios/"+nombreFicheroPython)
                    .getPath()
                    .toString();

            //Se crea el proceso que va a ejecutar el programa python
            ProcessBuilder procesadorPython = new ProcessBuilder("python", ficheroPython)
                    .inheritIO();

            //Comienza el proceso con la ejecución del programa python y se espera a que éste acabe
            Process procesoPython = procesadorPython.start();
            procesoPython.waitFor();

            //Se ha terminado de ejecutar el programa python. El sistema operativo devuelve el control al programa
            //que continúa con su ejecución
        } catch (IOException | InterruptedException e) {
            System.out.println("Vaya! Algo salió mal en ModeloServiceImpl.EjecutaPython()......................");
            System.out.println(e.getMessage());
        }
    }
}
