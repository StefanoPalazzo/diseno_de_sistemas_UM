package OpenClosedPrinciple;

public class Main {
    public static void main(String[] args) {
        Impuesto impuestoUS = new ImpuestoUS();
        Impuesto impuestoEU = new ImpuestoEU();

        CalculadorDeImpuestos calculador = new CalculadorDeImpuestos();

        System.out.println("Total con impuesto US: " + calculador.calcularMontoTotal(100.0, impuestoUS));
        System.out.println("Total con impuesto EU: " + calculador.calcularMontoTotal(100.0, impuestoEU));
    }
}

