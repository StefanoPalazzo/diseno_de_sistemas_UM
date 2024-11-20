package LiskovSubstitutionPrinciple;

public class Main {
    public static void main(String[] args) {
        MetodoDePago tarjeta = new TarjetaDeCredito();
        MetodoDePago paypal = new PayPal();

        ProcesadorDePagos procesador = new ProcesadorDePagos();
        procesador.realizarPago(tarjeta, 150.0);
        procesador.realizarPago(paypal, 75.0);
    }
}