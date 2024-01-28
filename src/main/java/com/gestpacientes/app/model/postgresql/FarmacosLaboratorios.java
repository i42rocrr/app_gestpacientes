package com.gestpacientes.app.model.postgresql;

import com.gestpacientes.app.model.postgresql.Laboratorios;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class FarmacosLaboratorios {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long id;

    @Column
    private String nombre;

    @ManyToMany (fetch = FetchType.LAZY)
    @JoinTable(
            name = "FarmacosLaboratorios_Lista",
            joinColumns = @JoinColumn(name = "farmaco_id"),
            inverseJoinColumns = @JoinColumn(name="laboratorio_id")
    )
    private List<Laboratorios> laboratoriosList;

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

    public List<Laboratorios> getLaboratoriosList() {
        return laboratoriosList;
    }

    public void setLaboratoriosList(List<Laboratorios> laboratoriosList) {
        this.laboratoriosList = laboratoriosList;
    }
}
