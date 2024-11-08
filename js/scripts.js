function procesarFormulario(event) {
    event.preventDefault();

    var nombre = document.getElementById('Nombre').value.trim();
    var colegio = document.getElementById('Colegio').value.trim();
    var fecha = document.getElementById('Fecha').value;
    var hora = document.getElementById('Hora').value;
    var cantidadAlumnos = document.getElementById('Alumnos').value.trim();
    var correo = document.getElementById('Correo').value.trim();
    var tipoVisita = document.getElementById('TipoVisita').value;
    var mensaje = document.getElementById('Mensaje').value.trim();
    var aceptaTerminos = document.getElementById('TerminosCondiciones').checked;

    var nombreError = document.getElementById('nombreError');

    
    if (nombre === '') {
        nombreError.textContent = 'Por favor, ingresa tu nombre completo.';
        return;
    } else {
        nombreError.textContent = '';
    }

    if (colegio === '' || cantidadAlumnos === '' || correo === '' || !aceptaTerminos) {
        alert('Por favor, completa todos los campos obligatorios y acepta los términos y condiciones.');
        return;
    }

    
    var emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    if (!emailPattern.test(correo)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return;
    }

    
    if (cantidadAlumnos <= 0 || isNaN(cantidadAlumnos)) {
        alert('Por favor, ingresa un número válido de alumnos.');
        return;
    }

    var formData = new FormData();
    formData.append('Nombre', nombre);
    formData.append('Colegio', colegio);
    formData.append('Fecha', fecha);
    formData.append('Hora', hora);
    formData.append('Alumnos', cantidadAlumnos);
    formData.append('Correo', correo);
    formData.append('TipoVisita', tipoVisita);
    formData.append('Mensaje', mensaje);
    formData.append('TerminosCondiciones', aceptaTerminos);

    var submitButton = document.querySelector('input[type="submit"]');
    submitButton.disabled = true; 

    fetch('url_para_procesar_formulario.php', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        submitButton.disabled = false; 
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del servidor:', data);
        alert('Formulario enviado correctamente.');
    })
    .catch(error => {
        submitButton.disabled = false; 
        console.error('Error al enviar formulario:', error);
        alert('Hubo un error al enviar el formulario.');
    });
}

document.querySelector('.formulario').addEventListener('submit', procesarFormulario);


var nombreInput = document.getElementById('Nombre');
nombreInput.addEventListener('input', function() {
    var nombre = this.value.trim();
    var nombreError = document.getElementById('nombreError');

    if (nombre === '') {
        nombreError.textContent = 'Por favor, ingresa tu nombre completo.';
    } else {
        nombreError.textContent = '';
    }
});




