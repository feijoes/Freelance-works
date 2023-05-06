package com.main.proyectofinal.controllers;

import com.main.proyectofinal.db.Compu;
import com.main.proyectofinal.db.CompuRepository;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.control.Separator;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.VBox;

import java.net.URL;
import java.time.LocalDate;
import java.util.List;
import java.util.ResourceBundle;
public class SaveController implements Initializable {

    @FXML
    private VBox compusBox;

    private CompuRepository compuRepository = new CompuRepository();

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        List<Compu> compus = compuRepository.findAll();

        for (Compu compu : compus) {
            Label idLabel = new Label("ID: " + compu.getId());
            Label codigoArchivoLabel = new Label("Codigo de archivo: " + compu.getCodigoArchivo());
            Label numInventarioLabel = new Label("Numero de inventario: " + compu.getNumInventario());
            Label marcaLabel = new Label("Marca: " + compu.getMarca());
            Label modeloLabel = new Label("Modelo: " + compu.getModelo());
            Label numSerialLabel = new Label("Numero de serie: " + compu.getNumSerial());
            Label sucursalLabel = new Label("Sucursal: " + compu.getSucursal());
            Label fechaCompraLabel = new Label("Fecha de compra: " + compu.getFechaCompra());
            Label costoCompraLabel = new Label("Costo de compra: " + compu.getCostoCompra());
            Label costoReemplazoLabel = new Label("Costo de reemplazo: " + compu.getCostoReemplazo());
            Label ramSizeLabel = new Label("Tamaño de RAM: " + compu.getRamSize());
            Label hddSizeLabel = new Label("Tamaño de HDD: " + compu.getHddSize());
            Label boardLabel = new Label("Board: " + compu.getBoard());
            Label monitorTypeLabel = new Label("Tipo de monitor: " + compu.getMonitorType());
            Label mouseTypeLabel = new Label("Tipo de mouse: " + compu.getMouseType());
            Label printerTypeLabel = new Label("Tipo de impresora: " + compu.getPrinterType());
            Label garantiaLabel = new Label("Garantia: " + compu.getGarantia());
            Label mantenimientoIntervalLabel = new Label("Intervalo de mantenimiento: " + compu.getMantenimientoInterval());
            Label lastMaintenanceDateLabel = new Label("Ultima fecha de mantenimiento: " + compu.getLastMaintenanceDate());
            Label repairCountLabel = new Label("Cantidad de reparaciones: " + compu.getRepairCount());
            Label totalRepairCostLabel = new Label("Costo total de reparaciones: " + compu.getTotalRepairCost());

            VBox compuBox = new VBox(idLabel, codigoArchivoLabel, numInventarioLabel, marcaLabel, modeloLabel, numSerialLabel,
                    sucursalLabel, fechaCompraLabel, costoCompraLabel, costoReemplazoLabel, ramSizeLabel, hddSizeLabel,
                    boardLabel, monitorTypeLabel, mouseTypeLabel, printerTypeLabel, garantiaLabel, mantenimientoIntervalLabel,
                    lastMaintenanceDateLabel, repairCountLabel, totalRepairCostLabel);
            compuBox.setStyle("-fx-background-color: #f0f0f0; -fx-padding: 10px; -fx-spacing: 5px; -fx-border-radius: 5px;");
            compusBox.getChildren().addAll(compuBox,new Separator());
        }

    }
}