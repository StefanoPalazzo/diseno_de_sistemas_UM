package com.example;

public class Persona {
    private String nombre;
    private int edad;

    public Persona(){

    }
    public Persona(String nom, int edad){
        this.nombre = nom;
        this.edad = edad;
    }

    public String getNombre(){
        return this.nombre;
    }

    public int getEdad(){
        return this.edad;
    }
}
