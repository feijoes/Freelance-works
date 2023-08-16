<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Administrador 2</title>
    <link rel="stylesheet" href="Css/Adminis2.css">
</head>
<body>
    <header id="header">
        <h1>Productos</h1>
    </header>

    <main>
        <div class="contenedor">
            <div class="añadir">
                <h2>Añadir</h2>
                <form>
                    <label>Nombre del producto</label>
                    <input type="text" id="productoAñadir" name="nombreDelProducto">

                    <label>Valor del producto</label>
                    <input type="number" id="valorAñadir">

                    <label>Existencia</label>
                    <input type="number" id="existenciaAñadir">

                    <label>Url Imagen</label>
                    <input type="text" id="ImagenAñadir">

                    <input class="button" type="button" id="botonAñadir" value="Añadir">
                </form>
            </div>

            <div class="editar">
                <h2>Editar</h2>
                <form>
                    <label>Nombre del producto</label>
                    <select id="productoEditar">
                        <option value="">---</option>
                    </select>

                    <label>Atributo</label>
                    <select id="atributoEditar">
                        <option value="">---</option>
                    </select>

                    <label>Nuevo valor</label>
                    <input type="text" id="nuevoAtributo">

                    <input class="button" type="button" id="botonEditar" value="Editar">
                </form>
            </div>

            <div class="eliminar">
                <h2>Eliminar</h2>
                <form>
                    <label>Nombre del producto</label>
                    <select id="productoEliminar">
                        <option value="">---</option>
                    </select>
                    <input class="button" type="button" id="botonEliminar" value="Eliminar">
                </form>
            </div>
        </div>

        <div class="contenedorMensaje">
            <div id="mensaje"></div>
        </div>

        <div class="contenedorProductos">
            <h2>Productos</h2>
            <div class="mostrarProductos" id="mostrarProductos"></div>
        </div>
    </main>
    <script src="Javas/admin.js" type="text/javascript"></script>
</body>
</html>
