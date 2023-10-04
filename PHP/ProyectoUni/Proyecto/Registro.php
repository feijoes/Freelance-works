<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Css/estilosesion.css">
    <title>Registro</title>
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
            <a href="Agenda.php" class="nav-link">Agenda</a>
            <a href="Sesion.php" class="nav-link">Usuario</a>
        </nav>
    </header>
    <div class="container">
        <form action="Conexiones/registrouser.php" method="POST" class="formulario">
            <h2 class="titulo">Registrar</h2>
       
            <div class="padre">
                <div class="NOMBRE">
                    <label for="">Nombres</label>
                    <input type="text" name="nombres">
                </div>
                <div class="APE_MAT">
                    <label for="">Apellido Materno</label>
                    <input type="text" name="apellido_materno">
                </div>
                <div class="APE_PAT">
                    <label for="">Apellido Paterno</label>
                    <input type="text" name="apellido_paterno">
                </div>
                <div class="TELEFONO">
                    <label for="">Telefono</label>
                    <input type="text" name="telefono">
                </div>
                <div class="CORREO">
                    <label for="">CORREO</label>
                    <input type="text" name="email">
                </div>
                <div class="CLAVE">
                    <label for="">Contraseña</label>
                    <input type="password" name="password" required>
                </div>
                <div class="cuenta">
                    <input class="boton" type="submit" value="Registrar" name="registro">
                    <a href="Principal.php">SALIR</a>

                </div>
                
            </div>







        </form>
        

    </div>
    
    

</body>

</html>