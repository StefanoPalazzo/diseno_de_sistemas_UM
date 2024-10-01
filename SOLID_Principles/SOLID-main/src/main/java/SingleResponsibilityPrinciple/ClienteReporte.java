package SingleResponsibilityPrinciple;

public class ClienteReporte {
    public void imprimirDetalles(Cliente cliente) {
        System.out.println("Cliente: " + cliente.getNombre());
        System.out.println("Email: " + cliente.getEmail());
        System.out.println("Pedidos: ");
        for (Pedido pedido : cliente.getPedidos()) {
            System.out.println("- Producto: " + pedido.getProducto() + ", Cantidad: " + pedido.getCantidad());
        }
    }
}
