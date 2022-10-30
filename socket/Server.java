package socket;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        System.out.println("Waiting for client`s...");
        try {
            ServerSocket serverSocket = new ServerSocket(1111);
            Socket socket = serverSocket.accept();
            System.out.println("Hello World!");

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
