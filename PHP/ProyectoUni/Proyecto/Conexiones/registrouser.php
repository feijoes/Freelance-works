<?php
phpinfo();
/*
if (!empty($_POST["registro"])){
if (empty($_POST["nombres"]) or empty ($_POST["apellido_materno"]) or empty ($_POST["apellido_paterno"]) or empty ($_POST["telefono"]) or empty ($_POST["email"]) or empty ($_POST["password"])){
    echo 'Uno de los campos esta vacio';
} else {
    
    
     $servername = "localhost";
     $username = "root";
     $password = "12345678";
     $database = "proyectobd";
     $charset = "utf8";

    try{
        $conexion = "mysql:host=" . $this->servername . "; dbname=" . $this->database . ";
        charset=" . $this->charset;
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_EMULATE_PREPARES => false
        ];

        $db = new PDO($conexion, $this->username, $this->password, $options);

        
    } catch(PDOException $e) {
        echo 'Error conexion: ' . $e->getMessage();
        exit;
    }
    
    try {
        echo "Se guardo la informacion";
        $db= conectar();
        $query=$db->prepare("INSERT INTO users (nombres,apellido_materno,apellido_paterno,telefono,email,password)VALUES(:nombres,:apellido_materno,:apellido_paterno,:telefono,:email,:hash_password)");
    
        $query->bindParam("nombres",$_POST["nombres"],PDO::PARAM_STR);
        $hash_password= hash('sha256', $_POST["password"]); //Password encryption
        $query->bindParam("hash_password", $hash_password,PDO::PARAM_STR) ;
        $query->bindParam("email", $_POST["email"],PDO::PARAM_STR) ;
        $query->bindParam("telefono",$_POST["telefono"],PDO::PARAM_STR) ;
        $query->bindParam("apellido_paterno",$_POST["apellido_paterno"],PDO::PARAM_STR) ;
        $query->bindParam("apellido_materno",$_POST["apellido_materno"],PDO::PARAM_STR) ;
        $query->execute();
        $uid=$db->lastInsertId(); // Last inserted row id
        $db = null;
        echo $uid;
        //code...
    } catch (\Exception $e) {
        echo $e->getMessage();
    }
   

    



}

    
}
?>