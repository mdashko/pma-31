package socket;

import java.io.IOException;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        System.out.println("Client is--->");
        try {
            Socket socket = new Socket("localhost",1111);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}