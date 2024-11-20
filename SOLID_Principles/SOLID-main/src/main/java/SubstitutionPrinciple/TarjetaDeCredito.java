package LiskovSubstitutionPrinciple;

public class TarjetaDeCredito extends MetodoDePago {
    @Override
    public void procesarPago(double monto) {
        System.out.println("Procesando el pago de $" + monto + " con tarjeta de crédito.");
    }
}