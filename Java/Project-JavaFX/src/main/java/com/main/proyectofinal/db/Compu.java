package com.main.proyectofinal.db;

import java.time.LocalDate;

public class Compu {

    private int id;

    private String codigoArchivo;
    private String numInventario;
    private String marca;
    private String modelo;
    private String numSerial;
    private String sucursal;
    private LocalDate fechaCompra;
    private double costoCompra;
    private double costoReemplazo;
    private int ramSize;
    private int hddSize;
    private String board;
    private String monitorType;
    private String mouseType;
    private String printerType;
    private String garantia;
    private String mantenimientoInterval;
    private LocalDate lastMaintenanceDate;
    private int repairCount;
    private double totalRepairCost;
    @Override
    public String toString() {
        return "Compu{" +
                "id=" + id +
                ", codigoArchivo='" + codigoArchivo + '\'' +
                ", numInventario='" + numInventario + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                ", numSerial='" + numSerial + '\'' +
                ", sucursal='" + sucursal + '\'' +
                ", fechaCompra=" + fechaCompra +
                ", costoCompra=" + costoCompra +
                ", costoReemplazo=" + costoReemplazo +
                ", ramSize=" + ramSize +
                ", hddSize=" + hddSize +
                ", board='" + board + '\'' +
                ", monitorType='" + monitorType + '\'' +
                ", mouseType='" + mouseType + '\'' +
                ", printerType='" + printerType + '\'' +
                ", garantia='" + garantia + '\'' +
                ", mantenimientoInterval='" + mantenimientoInterval + '\'' +
                ", lastMaintenanceDate=" + lastMaintenanceDate +
                ", repairCount=" + repairCount +
                ", totalRepairCost=" + totalRepairCost +
                '}';
    }

    public Compu(int id ,String codigoArchivo, String numInventario, String marca, String modelo, String numSerial,
                 String sucursal, LocalDate fechaCompra, double costoCompra, double costoReemplazo, int ramSize,
                 int hddSize, String board, String monitorType, String mouseType, String printerType, String garantia,
                 String  mantenimiento_preventivo_intervalo, LocalDate lastMaintenanceDate, int repairCount, double totalRepairCost) {
        this.id = id;
        this.codigoArchivo = codigoArchivo;
        this.numInventario = numInventario;
        this.marca = marca;
        this.modelo = modelo;
        this.numSerial = numSerial;
        this.sucursal = sucursal;
        this.fechaCompra = fechaCompra;
        this.costoCompra = costoCompra;
        this.costoReemplazo = costoReemplazo;
        this.ramSize = ramSize;
        this.hddSize = hddSize;
        this.board = board;
        this.monitorType = monitorType;
        this.mouseType = mouseType;
        this.printerType = printerType;
        this.garantia = garantia;
        this.mantenimientoInterval = mantenimiento_preventivo_intervalo;
        this.lastMaintenanceDate = lastMaintenanceDate;
        this.repairCount = repairCount;
        this.totalRepairCost = totalRepairCost;
    }
    public Compu(String codigoArchivo, String numInventario, String marca, String modelo, String numSerial,
                 String sucursal, LocalDate fechaCompra, double costoCompra, double costoReemplazo, int ramSize,
                 int hddSize, String board, String monitorType, String mouseType, String printerType, String garantia,
                 String mantenimiento_preventivo_intervalo, LocalDate lastMaintenanceDate, int repairCount, double totalRepairCost) {
        this.codigoArchivo = codigoArchivo;
        this.numInventario = numInventario;
        this.marca = marca;
        this.modelo = modelo;
        this.numSerial = numSerial;
        this.sucursal = sucursal;
        this.fechaCompra = fechaCompra;
        this.costoCompra = costoCompra;
        this.costoReemplazo = costoReemplazo;
        this.ramSize = ramSize;
        this.hddSize = hddSize;
        this.board = board;
        this.monitorType = monitorType;
        this.mouseType = mouseType;
        this.printerType = printerType;
        this.garantia = garantia;
        this.mantenimientoInterval = mantenimiento_preventivo_intervalo;
        this.lastMaintenanceDate = lastMaintenanceDate;
        this.repairCount = repairCount;
        this.totalRepairCost = totalRepairCost;
    }

    // getters and setters
    public int getId() {
        return id;
    }

    public String getCodigoArchivo() {
        return codigoArchivo;
    }

    public String getNumInventario() {
        return numInventario;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public String getNumSerial() {
        return numSerial;
    }

    public String getSucursal() {
        return sucursal;
    }

    public LocalDate getFechaCompra() {
        return fechaCompra;
    }

    public double getCostoCompra() {
        return costoCompra;
    }

    public double getCostoReemplazo() {
        return costoReemplazo;
    }

    public int getRamSize() {
        return ramSize;
    }

    public int getHddSize() {
        return hddSize;
    }

    public String getBoard() {
        return board;
    }

    public String getMonitorType() {
        return monitorType;
    }

    public String getMouseType() {
        return mouseType;
    }

    public String getPrinterType() {
        return printerType;
    }

    public String getGarantia() {
        return garantia;
    }

    public String getMantenimientoInterval() {
        return mantenimientoInterval;
    }

    public LocalDate getLastMaintenanceDate() {
        return lastMaintenanceDate;
    }

    public int getRepairCount() {
        return repairCount;
    }

    public double getTotalRepairCost() {
        return totalRepairCost;
    }
}