const express = require("express");
const router = express.Router();
const {
    GetAllProductos,
    PostProducto,
    GetOneProducto
} = require("../controlers/productos")

router.route("/").get(GetAllProductos).post(PostProducto)
router.route("/:id").get(GetOneProducto)

module.exports = router