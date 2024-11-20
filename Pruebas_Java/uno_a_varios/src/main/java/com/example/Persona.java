package com.example;

import java.util.ArrayList;

public class Persona {
// Declaro los atributos
    private String nombre;

    private String apellido;
// Declaro la variable de refeerncia del tipo contenedor dinámico que la vincula con
  // la Clase Auto.
    private ArrayList<Auto> mAuto;

// Constructor vacio
    public Persona () {
        // Creo el contenedor de autos para una persona determinada
        mAuto= new ArrayList<Auto>();
    }


    // Constructor vacio
    public Persona (String pnombre, String papellido) {
        nombre = pnombre;
         apellido =  papellido;

        // Creo el contenedor de autos para una persona determinada
        mAuto= new ArrayList<Auto>();
    }
// Agregar un auto a una persona
    // Utilizando el método ADD de la clase ArrayList de las colecciones
	public void AgregarUnAuto(Auto auto){

	mAuto.add(auto);
	}

// Declaracion de los métodos set y get de los atributos
    public String getApellido () {
        return apellido;
    }

    public void setApellido (String val) {
        this.apellido = val;
    }

    public ArrayList<Auto> getAuto () {
        return mAuto;
    }

    public void setAuto (ArrayList<Auto> val) {
        this.mAuto = val;
    }

    public String getNombre () {
        return nombre;
    }

    public void setNombre (String val) {
        this.nombre = val;
    }

}