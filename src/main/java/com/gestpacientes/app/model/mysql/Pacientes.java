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


}
