package com.main.proyectofinal.controllers;

import com.main.proyectofinal.db.Compu;
import com.main.proyectofinal.db.CompuRepository;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;

import java.time.LocalDate;

public class CreateController {
    @FXML
    private TextField codigoArchivoField;

    @FXML
    private TextField numInventarioField;

    @FXML
    private TextField marcaField;

    @FXML
    private TextField modeloField;

    @FXML
    private TextField numSerialField;

    @FXML
    private TextField sucursalField;

    @FXML
    private DatePicker fechaCompraPicker;

    @FXML
    private TextField costoCompraField;

    @FXML
    private TextField costoReemplazoField;

    @FXML
    private TextField ramSizeField;

    @FXML
    private TextField hddSizeField;

    @FXML
    private TextField boardField;

    @FXML
    private TextField monitorTypeField;

    @FXML
    private TextField mouseTypeField;

    @FXML
    private TextField printerTypeField;

    @FXML
    private TextField garantiaField;

    @FXML
    private TextField mantenimientoIntervalField;

    @FXML
    private DatePicker lastMaintenanceDatePicker;

    @FXML
    private TextField repairCountField;

    @FXML
    private TextField totalRepairCostField;

    private Compu compu;


    @FXML
    private void handleGuardar(ActionEvent event) {
        // Get values from the input fields

        String codigoArchivo = codigoArchivoField.getText();
        String numInventario = numInventarioField.getText();
        String marca = marcaField.getText();
        String modelo = modeloField.getText();
        String numSerial = numSerialField.getText();
        String sucursal = sucursalField.getText();
        LocalDate fechaCompra = fechaCompraPicker.getValue();
        double costoCompra = Double.parseDouble(costoCompraField.getText());
        double costoReemplazo = Double.parseDouble(costoReemplazoField.getText());
        int ramSize = Integer.parseInt(ramSizeField.getText());
        int hddSize = Integer.parseInt(hddSizeField.getText());
        String board = boardField.getText();
        String monitorType = monitorTypeField.getText();
        String mouseType = mouseTypeField.getText();
        String printerType = printerTypeField.getText();
        String garantia = garantiaField.getText();
        String mantenimientoInterval = mantenimientoIntervalField.getText();
        LocalDate lastMaintenanceDate = lastMaintenanceDatePicker.getValue();
        int repairCount = Integer.parseInt(repairCountField.getText());
        double totalRepairCost = Double.parseDouble(totalRepairCostField.getText());

        // Create a new Compu object with the input values
        Compu compu = new Compu(codigoArchivo, numInventario, marca, modelo, numSerial, sucursal,
                fechaCompra, costoCompra, costoReemplazo, ramSize, hddSize, board, monitorType,
                mouseType, printerType, garantia, mantenimientoInterval, lastMaintenanceDate,
                repairCount, totalRepairCost);
        CompuRepository compuRepository = new CompuRepository();
        compuRepository.create(compu);


    }
}
