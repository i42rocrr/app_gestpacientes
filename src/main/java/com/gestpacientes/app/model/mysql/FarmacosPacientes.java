package com.gestpacientes.app.model.mysql;

import com.gestpacientes.app.model.mysql.Pacientes;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class FarmacosPacientes {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long id;

    @Column
    private String nombre;

    @ManyToMany (fetch = FetchType.LAZY)
    @JoinTable(
            name = "FarmacosPacientes_Lista",
            joinColumns = @JoinColumn(name = "farmaco_id"),
            inverseJoinColumns = @JoinColumn(name="paciente_id")
    )
    private List<Pacientes> pacientesList;

}
