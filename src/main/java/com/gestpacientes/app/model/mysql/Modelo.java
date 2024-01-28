package com.gestpacientes.app.model.mysql;

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

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public String getRangoEdad() {
        return rangoEdad;
    }

    public void setRangoEdad(String rangoEdad) {
        this.rangoEdad = rangoEdad;
    }

    public String getMenopausia() {
        return menopausia;
    }

    public void setMenopausia(String menopausia) {
        this.menopausia = menopausia;
    }

    public String getTamanoTumor() {
        return tamanoTumor;
    }

    public void setTamanoTumor(String tamanoTumor) {
        this.tamanoTumor = tamanoTumor;
    }

    public String getNumGanglios() {
        return numGanglios;
    }

    public void setNumGanglios(String numGanglios) {
        this.numGanglios = numGanglios;
    }

    public String getNodeCaps() {
        return nodeCaps;
    }

    public void setNodeCaps(String nodeCaps) {
        this.nodeCaps = nodeCaps;
    }

    public String getGradoMalignidad() {
        return gradoMalignidad;
    }

    public void setGradoMalignidad(String gradoMalignidad) {
        this.gradoMalignidad = gradoMalignidad;
    }

    public String getMama() {
        return mama;
    }

    public void setMama(String mama) {
        this.mama = mama;
    }

    public String getCuadranteMamario() {
        return cuadranteMamario;
    }

    public void setCuadranteMamario(String cuadranteMamario) {
        this.cuadranteMamario = cuadranteMamario;
    }

    public String getRadiacion() {
        return radiacion;
    }

    public void setRadiacion(String radiacion) {
        this.radiacion = radiacion;
    }

    @Column
    private String mama;

    @Column
    private String cuadranteMamario;

    @Column
    private String radiacion;
}
