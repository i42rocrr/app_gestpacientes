package com.gestpacientes.app.repository.mysql;

import com.gestpacientes.app.model.mysql.Modelo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ModeloRepository extends JpaRepository<Modelo,Long> {

}
