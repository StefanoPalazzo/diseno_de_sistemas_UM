package InterfaceSegregationPrinciple;

public class Main {
    public static void main(String[] args) {
        Readable hardDriveReader = new HardDrive();
        Writable hardDriveWriter = new HardDrive();

        hardDriveReader.readData("file.txt");
        hardDriveWriter.writeData("New file content");

        Readable sdReader = new SDReader();
        sdReader.readData("photo.jpg");
    }
}