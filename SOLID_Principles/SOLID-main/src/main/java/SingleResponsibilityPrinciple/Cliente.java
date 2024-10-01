package SingleResponsibilityPrinciple;

public class ClienteGestor {
    public void agregarPedido(Cliente cliente, Pedido pedido) {
        cliente.agregarPedido(pedido);
    }

    public boolean verificarPedido(Cliente cliente, Pedido pedido) {
        return cliente.getPedidos().contains(pedido);
    }
}
