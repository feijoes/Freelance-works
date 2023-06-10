<?php

class Conexion{


	static public function conectar(){

		$link = new PDO("mysql:host=localhost;dbname=u823652872_sistemapos",
			            "u823652872_yelsinSC",
			            "Y@lberto2022");

		$link->exec("set names utf8");

		return $link;
	}
}

?>