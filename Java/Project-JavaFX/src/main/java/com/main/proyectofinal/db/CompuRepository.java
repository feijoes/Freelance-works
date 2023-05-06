package com.main.proyectofinal.db;

import java.sql.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class CompuRepository {
    private final String url = "jdbc:postgresql://dpg-chao3rvdvk4lphpc0j10-a.oregon-postgres.render.com:5432/db_wvtg?ssl=true&user=admin&password=6Bw7eKfynEl4Atm1H9ydb4EisbFGOsN0";
    private final String user = "admin";
    private final String password = "6Bw7eKfynEl4Atm1H9ydb4EisbFGOsN0";

    private Compu createCompuFromResultSet(ResultSet resultSet) throws SQLException {
        int id = resultSet.getInt("id");
        String codigoArchivo = resultSet.getString("codigo_archivo");
        String numeroInventario = resultSet.getString("numero_inventario");
        String marca = resultSet.getString("marca");
        String modelo = resultSet.getString("modelo");
        String numeroSerial = resultSet.getString("numero_serial");
        String sucursal = resultSet.getString("sucursal");
        LocalDate fechaCompra = resultSet.getDate("fecha_compra").toLocalDate();
        float costoCompra = resultSet.getFloat("costo_compra");
        float costoReemplazo = resultSet.getFloat("costo_reemplazo");
        int ramSize = resultSet.getInt("ram_size");
        int diskSize = resultSet.getInt("disk_size");
        String board = resultSet.getString("board");
        String monitor = resultSet.getString("monitor");
        String mouse = resultSet.getString("mouse");
        String printer = resultSet.getString("printer");
        String garantia = resultSet.getString("garantia");
        String mantenimientoPreventivoIntervalo = resultSet.getString("mantenimiento_preventivo_intervalo");
        LocalDate ultimoMantenimientoPreventivo = resultSet.getDate("ultimo_mantenimiento_preventivo").toLocalDate();
        int numeroReparaciones = resultSet.getInt("numero_reparaciones");
        float totalCostoReparaciones = resultSet.getFloat("total_costo_reparaciones");

        return new Compu(id, codigoArchivo, numeroInventario, marca, modelo, numeroSerial, sucursal,
                fechaCompra, costoCompra, costoReemplazo, ramSize, diskSize, board, monitor,
                mouse, printer, garantia, mantenimientoPreventivoIntervalo,
                ultimoMantenimientoPreventivo, numeroReparaciones, totalCostoReparaciones);
    }


    public void createTable()  {
        String query = "CREATE TABLE IF NOT EXISTS compus (" +
                "id SERIAL PRIMARY KEY, " +
                "codigo_archivo TEXT NOT NULL, " +
                "numero_inventario TEXT NOT NULL, " +
                "marca TEXT NOT NULL, " +
                "modelo TEXT NOT NULL, " +
                "numero_serial TEXT NOT NULL, " +
                "sucursal TEXT NOT NULL, " +
                "fecha_compra DATE NOT NULL, " +
                "costo_compra FLOAT NOT NULL, " +
                "costo_reemplazo FLOAT NOT NULL, " +
                "ram_size INT NOT NULL, " +
                "disk_size INT NOT NULL, " +
                "board TEXT NOT NULL, " +
                "monitor TEXT NOT NULL, " +
                "mouse TEXT NOT NULL, " +
                "printer TEXT NOT NULL, " +
                "garantia TEXT NOT NULL, " +
                "mantenimiento_preventivo_intervalo TEXT NOT NULL, " +
                "ultimo_mantenimiento_preventivo DATE NOT NULL, " +
                "numero_reparaciones INT NOT NULL, " +
                "total_costo_reparaciones FLOAT NOT NULL" +
                ")";
        try (Connection con = DriverManager.getConnection(url, user, password)) {
            PreparedStatement preparedStatement = con.prepareStatement(query);

            preparedStatement.executeUpdate();

        } catch (SQLException e) {
            System.out.println("error");
            e.printStackTrace();
        }
    }
    public void create(Compu compu) {
        String query = "INSERT INTO compus(codigo_archivo, numero_inventario, marca, modelo, numero_serial, sucursal, fecha_compra, costo_compra, costo_reemplazo, ram_size, disk_size, board, monitor, mouse, printer, garantia, mantenimiento_preventivo_intervalo, ultimo_mantenimiento_preventivo, numero_reparaciones, total_costo_reparaciones) "
                + "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";


        try (Connection con = DriverManager.getConnection(url, user, password);
             PreparedStatement pst = con.prepareStatement(query)) {
            pst.setString(1, compu.getCodigoArchivo());
            pst.setString(2, compu.getNumInventario());
            pst.setString(3, compu.getMarca());
            pst.setString(4, compu.getModelo());
            pst.setString(5, compu.getNumSerial());
            pst.setString(6, compu.getSucursal());
            pst.setDate(7, Date.valueOf(compu.getFechaCompra()));
            pst.setDouble(8, compu.getCostoCompra());
            pst.setDouble(9, compu.getCostoReemplazo());
            pst.setInt(10, compu.getRamSize());
            pst.setInt(11, compu.getHddSize());
            pst.setString(12, compu.getBoard());
            pst.setString(13, compu.getMonitorType());
            pst.setString(14, compu.getMouseType());
            pst.setString(15, compu.getPrinterType());
            pst.setString(16, compu.getGarantia());
            pst.setString(17, compu.getMantenimientoInterval());
            pst.setDate(18, Date.valueOf(compu.getLastMaintenanceDate()));
            pst.setInt(19, compu.getRepairCount());
            pst.setDouble(20, compu.getTotalRepairCost());

            pst.executeUpdate();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
    public List<Compu> findAll() {
        List<Compu> compus = new ArrayList<>();
        String query = "SELECT * FROM compus";

        try (Connection con = DriverManager.getConnection(url, user, password);
             PreparedStatement pst = con.prepareStatement(query);
             ResultSet rs = pst.executeQuery()) {
            while (rs.next()) {
                Compu compu = createCompuFromResultSet(rs);
                compus.add(compu);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return compus;
    }
}
