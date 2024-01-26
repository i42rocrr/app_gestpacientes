package com.gestpacientes.app.repository.postgresql;

import com.gestpacientes.app.model.postgresql.Laboratorios;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LaboratoriosRepository extends JpaRepository<Laboratorios,Long> {
}
