package DependencyInversionPrinciple;

public class Main {
    public static void main(String[] args) {
        PaymentMethod creditCardPayment = new CreditCardPayment();
        PaymentProcessor processor1 = new PaymentProcessor(creditCardPayment);
        processor1.makePayment(100.0);

        PaymentMethod payPalPayment = new PayPalPayment();
        PaymentProcessor processor2 = new PaymentProcessor(payPalPayment);
        processor2.makePayment(200.0);
    }
}
