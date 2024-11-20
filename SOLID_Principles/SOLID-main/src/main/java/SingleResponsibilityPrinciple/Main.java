package SingleResponsibilityPrinciple;

public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("Juan Perez", "juan.perez@email.com");

        Pedido pedido = new Pedido("Laptop", 2);
        ClienteGestor gestor = new ClienteGestor();
        ClienteReporte reporte = new ClienteReporte();

        gestor.agregarPedido(cliente, pedido);  // Agregar pedido al cliente
        reporte.imprimirDetalles(cliente);  // Imprimir detalles del cliente y sus pedidos
    }
}
