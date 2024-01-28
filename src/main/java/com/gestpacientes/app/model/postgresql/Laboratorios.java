package com.gestpacientes.app.model.postgresql;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;


@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Laboratorios {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long id;

    @Column
    private String nombre;

    @Column
    private String email;

    @ManyToMany (mappedBy = "laboratoriosList")
    private List<FarmacosLaboratorios> farmacosLaboratoriosList;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<FarmacosLaboratorios> getFarmacosLaboratoriosList() {
        return farmacosLaboratoriosList;
    }

    public void setFarmacosLaboratoriosList(List<FarmacosLaboratorios> farmacosLaboratoriosList) {
        this.farmacosLaboratoriosList = farmacosLaboratoriosList;
    }
}
