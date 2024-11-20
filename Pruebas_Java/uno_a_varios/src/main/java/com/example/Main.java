package com.example;

public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Creo una variable del tipo Persona llamada p
        Persona p = new Persona("PEREZ","JUAN");
        // Asigno el nombre y el appelido d ela persona creada
    

        // creo en forma independiente 3 autos
        Auto auto1 = new Auto("FORD","CRQ234");
        Auto auto2 = new Auto("RENAULT","FGH456");
        Auto auto3 = new Auto("CHEVROLET","UYT498");
  
      // Agrego al contenedor ArrayList correspondiente de la clase persona,
        // pasándole como parámetros al método los autos creados, para asocialos con la persona

        p.AgregarUnAuto(auto1);
        p.AgregarUnAuto(auto2);
        p.AgregarUnAuto(auto3);
        
      //
        System.out.println("NOMBRE COMPLETO: " + p.getNombre() + " " + p.getApellido());
        // Acà vemos como funciona la navegabilidad, llegamos a travès del objeto persona a su contenedor a travès
        // de la variable y luego dentro del contenedor accedemos a la posiciòn determinada por el subindice y desde ahí
        // al atributo deseado, patente, marca, etc
        System.out.println("AUTO1: " + p.getAuto().get(0).getMarca() + " " + p.getAuto().get(0).getPatente());
        System.out.println("AUTO2: " + p.getAuto().get(1).getMarca() + " " + p.getAuto().get(1).getPatente());
        System.out.println("AUTO3: " + p.getAuto().get(2).getMarca() + " " + p.getAuto().get(2).getPatente());
    }

}