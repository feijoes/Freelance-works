<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Css/Agendaestilos.css">
    <title>Agenda</title>
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
            <a href="Productos.php" class="nav-link">Productos</a>
            <a href="#" class="nav-link">Agenda</a>
            <a href="Sesion.php" class="nav-link">Usuario</a>
        </nav>
    </header>
    <div class="Titulo">
        <h1>Agenda Tu Cita</h1>
    </div>
    <div class="container">
        
        <form method="post">
            <div class="nombre">
                <input type="text" required>
                <label>Nombre</label>
            </div>
            <div class="correo">
                <input type="text" required>
                <label>Correo Electrónico</label>    
            </div>
            <div class="calendario">
                <input type="date" name="calendario"> 
                <label>Fecha</label>
            </div>
            <div class="hora">
                <label>Hora</label>
                <select name="hora">
                    <option>13:00</option>
                    <option>14:00</option>
                    <option>15:00</option>
                    <option>16:00</option>
                    <option>17:00</option>
                    <option>18:00</option>
                    <option>19:00</option>
                    <option>20:00</option>
                    <option>21:00</option>
                </select>
            </div>
            <div class="servicio">
                <label>Selecciona un servicio:</label>
                <select name="envio">
                    <option>Extensiones 1X1 Flat</option>
                    <option>Extensiones Hawaianas</option>
                    <option>Extensiones Clasicas 1X1</option>
                    <option>Extensiones Foxy</option>
                    <option>Corte1</option>
                    <option>Corte2</option>
                    <option>Corte3</option>
                    <option>Corte4</option>
                    <option>XV Años</option>
                    <option>Bodas</option>
                    <option>Evento Social</option>
                    <option>Evento Noche</option>
                </select>
            </div>
            <div class="enviar">
                <a href="Agendado.html" class="add-to-cart"> Agendar </a>
            </div>
        </form>
    </div>
</body>
</html>
