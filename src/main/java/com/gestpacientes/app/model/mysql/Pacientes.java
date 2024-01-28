package com.gestpacientes.app.model.mysql;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;



@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Pacientes {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long id;

    @Column
    private String nombre;

    @Column
    private String email;

    @ManyToMany (mappedBy = "pacientesList")
    private List<FarmacosPacientes> farmacosPacientesList;

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

    public List<FarmacosPacientes> getFarmacosPacientesList() {
        return farmacosPacientesList;
    }

    public void setFarmacosPacientesList(List<FarmacosPacientes> farmacosPacientesList) {
        this.farmacosPacientesList = farmacosPacientesList;
    }
}
