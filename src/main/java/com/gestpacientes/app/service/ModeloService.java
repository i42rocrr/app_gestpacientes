package com.gestpacientes.app.service;

import com.gestpacientes.app.model.mysql.Modelo;

import java.util.List;
import java.util.Optional;

public interface ModeloService {

    public List<Modelo> listarTodos();

    public Optional<Modelo> buscarModelo(Long id);

    public Modelo guardarModelos(Modelo modelo);

    public void borrarModelos(Modelo modelo);

    public void EjecutaPython();

}
