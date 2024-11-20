package SingleResponsibilityPrinciple;

public class ProductoGestor {
    public void actualizarStock(Producto producto, int cantidad) {
        producto.setStock(producto.getStock() + cantidad);
    }

    public boolean verificarDisponibilidad(Producto producto, int cantidad) {
        return producto.getStock() >= cantidad;
    }
}
