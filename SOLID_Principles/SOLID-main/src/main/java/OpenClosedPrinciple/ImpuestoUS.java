package OpenClosedPrinciple;

public class ImpuestoUS extends Impuesto {
    @Override
    public double calcularImpuesto(double monto) {
        return monto * 0.07; // 7% de impuesto
    }
}