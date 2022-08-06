const express = require("express");
const router = express.Router();
const {
    Login,
    Regiter
} = require("../controllers/authentication")

router.route("/register").get(Regiter)
router.route("/login").get(Login)

module.exports = router