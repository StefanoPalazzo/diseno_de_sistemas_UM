package InterfaceSegregationPrinciple;

public class SDReader implements Readable {
    @Override
    public void readData(String source) {
        System.out.println("Reading data from SD card: " + source);
    }
}