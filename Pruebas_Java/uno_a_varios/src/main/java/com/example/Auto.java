package com.example;

public class Auto {

    private String marca;

    private String patente;

    public Auto () {
    }
  public Auto ( String pmarca,String ppatente ) {
      marca = pmarca;
      patente = ppatente;
    }
    public String getMarca () {
        return marca;
    }

    public void setMarca (String val) {
        this.marca = val;
    }

    public String getPatente () {
        return patente;
    }

    public void setPatente (String val) {
        this.patente = val;
    }

}
