<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Css/estilosinicio.css">
    <title>Inicio De Sesion</title>
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

    <div class="formulario">
        <h1>Inicio de Sesión</h1>
        <form method="post">
            <div class="username">
                <input type="text" required>
                <label>Correo Electrónico</label>
            </div>
            <div class="contraseña">
                <input type="password" required>
                <label>Contraseña</label>
            </div>
            <div class="recordar">
                <a href="Registro.php">
                    <button type="button">Hacer el registro</button>
                  </a>
                <input type="submit" value="Iniciar" onclick="window.location.href='Principal.php'">
            </div>
            
            </div>
        </form>
    </div>
    <footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a href="#">
                        <img src="Img/Logo1.png" alt="Logofooter">
                    </a>
                </figure>
            </div>
            <div class="box">
                <h2>SOBRE NOSOTROS</h2>
                <p>Beauty Lashes es un moderno y acogedor salón de belleza especializado en realzar la mirada con servicios de
                    extensiones de pestañas y diseño de cejas. Resalta tu belleza natural con nosotros.</p>
                
            </div>
            <div class="box">
                <h2>SIGUENOS</h2>
                <div class="red-social">
                    <a href="https://www.facebook.com/"class="fa fa-facebook"></a>
                    <a href="https://www.instagram.com/"class="fa fa-instagram"></a>
                    <a href="https://twitter.com/home"class="fa fa-twitter"></a>
                    <a href="https://www.youtube.com/"class="fa fa-youtube"></a>
                </div>
            </div>
        </div>
        <div class="grupo-2">
            <small>&copy; 2023 <b>Beauty Lashes</b> - Todos los Derechos Reservados </small>



  

        </div>




    </footer>

</body>

</html>
