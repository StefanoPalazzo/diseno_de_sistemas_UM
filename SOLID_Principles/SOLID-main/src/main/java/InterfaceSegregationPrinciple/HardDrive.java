package InterfaceSegregationPrinciple;

public class HardDrive implements Readable, Writable {
    @Override
    public void readData(String source) {
        System.out.println("Reading data from hard drive: " + source);
    }

    @Override
    public void writeData(String data) {
        System.out.println("Writing data to hard drive: " + data);
    }
}
