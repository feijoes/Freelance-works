package com.main.proyectofinal.controllers;

import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;
import java.net.URL;

public class MenuController {

    private Stage stage = new Stage();

    public void switchScene(String sceneName) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource(sceneName));
        Scene scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

    public void switchScene2(String resourcePath) throws IOException {
        URL url = new File(resourcePath).toURI().toURL();
        Parent root = FXMLLoader.load(url);
        Scene scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

    public void switchToScene1(ActionEvent event) throws IOException {
        switchScene2("C:\\Users\\Pedro\\OneDrive\\Frelance-works\\Java\\Project-JavaFX\\src\\main\\resources\\com\\main\\proyectofinal\\f.fxml");
    }

    public void switchToScene2(ActionEvent event) throws IOException {
        switchScene2("C:\\Users\\Pedro\\OneDrive\\Frelance-works\\Java\\Project-JavaFX\\src\\main\\resources\\com\\main\\proyectofinal\\save.fxml");
    }
}
