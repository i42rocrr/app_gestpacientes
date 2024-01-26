package com.gestpacientes.app.repository.postgresql;

import com.gestpacientes.app.model.postgresql.FarmacosLaboratorios;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
@Repository
public interface FarmacosLaboratoriosRepository extends JpaRepository<FarmacosLaboratorios,Long> {

}
