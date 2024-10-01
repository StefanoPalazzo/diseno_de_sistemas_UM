package LiskovSubstitutionPrinciple;

public class PayPal extends MetodoDePago {
    @Override
    public void procesarPago(double monto) {
        System.out.println("Procesando el pago de $" + monto + " con PayPal.");
    }
}