<?php

$servername = "localhost"; 
$username = "root"; 
$password = ""; // 
$dbname = "parque_biodiversidad"; 


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$nombre = $_POST['Nombre'];
$colegio = $_POST['Colegio'];
$fecha = $_POST['Fecha'];
$hora = $_POST['Hora'];
$alumnos = $_POST['Alumnos'];
$correo = $_POST['Correo'];
$tipoVisita = $_POST['TipoVisita'];
$mensaje = $_POST['Mensaje'];
$aceptaTerminos = isset($_POST['TerminosCondiciones']) ? 1 : 0;


$sql = "INSERT INTO visitas (nombre, colegio, fecha, hora, alumnos, correo, tipo_visita, mensaje, acepta_terminos) 
        VALUES ('$nombre', '$colegio', '$fecha', '$hora', '$alumnos', '$correo', '$tipoVisita', '$mensaje', '$aceptaTerminos')";


if ($conn->query($sql) === TRUE) {
    echo json_encode(["success" => true, "message" => "Formulario enviado correctamente."]);
} else {
    echo json_encode(["success" => false, "message" => "Error: " . $sql . "<br>" . $conn->error]);
}


$conn->close();
?>
