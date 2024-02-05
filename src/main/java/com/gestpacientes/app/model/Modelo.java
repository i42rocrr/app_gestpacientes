package com.gestpacientes.app.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Modelo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long id;

    @Column
    private String categoria;

    @Column
    private String rangoEdad;

    @Column
    private String menopausia;

    @Column
    private String tamanoTumor;

    @Column
    private String numGanglios;

    @Column
    private String nodeCaps;

    @Column
    private String gradoMalignidad;

    @Column
    private String mama;

    @Column
    private String cuadranteMamario;

    @Column
    private String radiacion;
}
