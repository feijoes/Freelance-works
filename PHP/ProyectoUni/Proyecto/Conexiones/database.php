<?php

class database 
{
    private $servername = "localhost";
    private $username = "root";
    private $password = "12345678";
    private $database = "proyectobd";
    private $charset = "utf8";
    
    function conectar()
    {   
        
        try{
            $conexion = "mysql:host=" . $this->servername . "; dbname=" . $this->database . ";
            charset=" . $this->charset;
            $options = [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_EMULATE_PREPARES => false
            ];

            $pdo = new PDO($conexion, $this->username, $this->password, $options);

            return $pdo;
        } catch(PDOException $e) {
            echo 'Error conexion: ' . $e->getMessage();
            exit;
        }
    }
}

?>
