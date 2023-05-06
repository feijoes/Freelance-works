package com.main.proyectofinal;

import com.main.proyectofinal.db.Compu;
import com.main.proyectofinal.db.CompuRepository;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.time.LocalDate;
import java.util.Optional;

public class HelloApplication extends Application {
    private static CompuRepository compuRepository;
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("Main.fxml"));
        Scene scene = new Scene(fxmlLoader.load());

        stage.setTitle("COMPUTADORAS DE CARIBE ");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        compuRepository = new CompuRepository();

        Compu a = compuRepository.findAll().stream().findFirst().orElseThrow();
        System.out.println(a.getCodigoArchivo());
        launch();
    }
}