package com.example;


public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Persona p1 = new Persona("Juan", 10);
        System.out.println(p1.getNombre() + " tiene " +  p1.getEdad());
    }
}

