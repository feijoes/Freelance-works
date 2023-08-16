<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Css/Compraproductos.css">
    <title>Comprar productos</title>
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
        <h2>Detalle del Producto </h2>
        <div class="product">
            <img src="Img/Producto4.jpg" alt="Producto 1">
            <h3> Brocha de maquillaje Éclat BrushPro</h3>
            <p>La brocha de maquillaje "Éclat BrushPro" es una herramienta esencial para todos los amantes del
                maquillaje que buscan obtener un acabado profesional en su rutina diaria. Diseñada meticulosamente con
                materiales de alta calidad y una combinación única de cerdas sintéticas y naturales, esta brocha ha sido
                creada para brindar una experiencia de maquillaje excepcional..</p>

            <form action="procesar_compra_producto1.php" method="post">
                <label for="cantidad">Cantidad:</label>
                <input type="number" name="cantidad" id="cantidad" min="1" value="1">
                <p>
                    Tipo de Envio:
                    <select name="envio">
                        <option>En tienda</option>
                    </select>

                </p>
                <input type="submit" value="Confirmar compra">
            </form>
        </div>
    </div>

</body>

</html>