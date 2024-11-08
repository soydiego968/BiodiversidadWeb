<?php
// Configuración de la base de datos
$servername = "localhost"; // O la dirección de tu servidor de base de datos
$username = "root"; // Tu usuario de MySQL
$password = ""; // Tu contraseña de MySQL
$dbname = "parque_biodiversidad"; // Nombre de tu base de datos

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Obtener los datos del formulario
$nombre = $_POST['Nombre'];
$colegio = $_POST['Colegio'];
$fecha = $_POST['Fecha'];
$hora = $_POST['Hora'];
$alumnos = $_POST['Alumnos'];
$correo = $_POST['Correo'];
$tipoVisita = $_POST['TipoVisita'];
$mensaje = $_POST['Mensaje'];
$aceptaTerminos = isset($_POST['TerminosCondiciones']) ? 1 : 0;

// Preparar la consulta SQL
$sql = "INSERT INTO visitas (nombre, colegio, fecha, hora, alumnos, correo, tipo_visita, mensaje, acepta_terminos) 
        VALUES ('$nombre', '$colegio', '$fecha', '$hora', '$alumnos', '$correo', '$tipoVisita', '$mensaje', '$aceptaTerminos')";

// Ejecutar la consulta
if ($conn->query($sql) === TRUE) {
    echo json_encode(["success" => true, "message" => "Formulario enviado correctamente."]);
} else {
    echo json_encode(["success" => false, "message" => "Error: " . $sql . "<br>" . $conn->error]);
}

// Cerrar la conexión
$conn->close();
?>
