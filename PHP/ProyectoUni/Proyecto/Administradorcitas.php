<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Css/Citasadmin.css">
    <title>Administar citas</title>
    <script src="https://kit.fontawesome.com/24eb7a5550.js" crossorigin="anonymous"></script>
</head>
<body>
    <header>
        <div class="logo">
            <img src="Img/Logo1.png" alt="logo empresa">
            <h2 class="logo-nombre">Beauty Lashes</h2>
        </div>
        <nav>
            <a href="Principal.php" class="nav-link">Inicio</a>
            <a href="Pestañas.php" class="nav-link">Pestañas</a>
            <a href="Maquillaje.php" class="nav-link">Maquillaje</a>
            <a href="Cortes.php" class="nav-link">Cortes</a>
            <a href="Administrador2.php" class="nav-link">Productos </a>
            <a href="Citasadministrador.php" class="nav-link">Citas</a>
            <a href="Sesion.php" class="nav-link">Usuario</a>
        </nav>
    </header>

    <div class="titulo">
        <h2>Citas Agendadas</h2>
    </div>
    <div class="citas-table">
        <table>
            <thead>
                <tr>
                    <th>Usuario</th>
                    <th>Tipo de Servicio</th>
                    <th>Hora</th>
                    <th>Acción</th> <!-- Agregamos una columna para los botones -->
                </tr>
            </thead>
            <tbody>
                <!-- Filas de ejemplo -->
                <tr>
                    <td>Nombre de Usuario 1</td>
                    <td>Servicio 1</td>
                    <td>10:00 AM</td>
                    <td><button class="eliminar-button"  onclick="eliminarFila(this)">Eliminar</button></td>
                </tr>
                <tr>
                    <td>Nombre de Usuario 2</td>
                    <td>Servicio 2</td>
                    <td>2:30 PM</td>
                    <td><button class="eliminar-button" onclick="eliminarFila(this)">Eliminar</button></td>
                </tr>
                <tr>
                    <td>Nombre de Usuario 2</td>
                    <td>Servicio 2</td>
                    <td>2:30 PM</td>
                    <td><button class="eliminar-button" onclick="eliminarFila(this)">Eliminar</button></td>
                </tr>
                <tr>
                    <td>Nombre de Usuario 2</td>
                    <td>Servicio 2</td>
                    <td>2:30 PM</td>
                    <td><button class="eliminar-button" onclick="eliminarFila(this)">Eliminar</button></td>
                </tr>
                <tr>
                    <td>Nombre de Usuario 2</td>
                    <td>Servicio 2</td>
                    <td>2:30 PM</td>
                    <td><button class="eliminar-button" onclick="eliminarFila(this)">Eliminar</button></td>
                </tr>

                <!-- Puedes seguir agregando más filas -->
            </tbody>
        </table>
    </div>

    <script>
        function eliminarFila(button) {
            var row = button.parentNode.parentNode; // Obtenemos la fila padre del botón
            row.parentNode.removeChild(row); // Eliminamos la fila
        }
    </script>
</body>
</html>