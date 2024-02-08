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
        try {
            String ficheroPython = new File("/src/main/python/servicios/"+nombreFicheroPython)
                    .getPath()
                    .toString();

            ProcessBuilder procesadorPython = new ProcessBuilder("python", ficheroPython)
                    .inheritIO();

            Process procesoPython = procesadorPython.start();
            procesoPython.waitFor();

        } catch (IOException | InterruptedException e) {
            System.out.println("Vaya! Algo salió mal en ModeloServiceImpl.EjecutaPython()......................");
            System.out.println(e.getMessage());
        }
    }
}
