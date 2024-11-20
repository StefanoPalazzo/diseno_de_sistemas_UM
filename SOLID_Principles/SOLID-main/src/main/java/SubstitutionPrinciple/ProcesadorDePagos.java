package LiskovSubstitutionPrinciple;

public class ProcesadorDePagos {
    public void realizarPago(MetodoDePago metodo, double monto) {
        metodo.procesarPago(monto);
    }


}
