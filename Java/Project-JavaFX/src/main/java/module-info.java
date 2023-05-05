module com.main.proyectofinal {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;

    opens com.main.proyectofinal to javafx.fxml;
    exports com.main.proyectofinal;
    exports com.main.proyectofinal.controllers;
    opens com.main.proyectofinal.controllers to javafx.fxml;
}