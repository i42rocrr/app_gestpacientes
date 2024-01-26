package com.gestpacientes.app.repository.mysql;

import com.gestpacientes.app.model.mysql.Pacientes;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PacientesRepository extends JpaRepository<Pacientes,Long> {
}
