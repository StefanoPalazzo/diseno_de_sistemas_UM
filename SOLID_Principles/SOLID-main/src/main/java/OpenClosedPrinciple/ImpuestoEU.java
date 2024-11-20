package OpenClosedPrinciple;

public class ImpuestoEU extends Impuesto {
    @Override
    public double calcularImpuesto(double monto) {
        return monto * 0.20; // 20% de IVA
    }
}