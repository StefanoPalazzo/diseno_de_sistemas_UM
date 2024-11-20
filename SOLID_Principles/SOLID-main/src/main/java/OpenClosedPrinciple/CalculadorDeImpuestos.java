package OpenClosedPrinciple;

public class CalculadorDeImpuestos {
    public double calcularMontoTotal(double monto, Impuesto impuesto) {
        return monto + impuesto.calcularImpuesto(monto);
    }
}
