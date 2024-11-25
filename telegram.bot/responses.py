import re

def process_message(message, response_array, response):
   
    
    list_message = re.findall(r"[\w']+|[.,!?¿¡;]", message.lower())
    
    
    score = 0
    for word in list_message:
        if word in response_array:
            score += 1

    return score, response


def process_phone_number(message):
   
    
    if re.search(r'\+?\d{7,15}', message):
        return 1, '¡Gracias!'
    return 0, ''


def get_response(message):
   
    
  
    response_list = [
        process_message(message, ['hola', 'hey', 'buenas', 'tardes' 'holis', 'días', 'noche'], '¡Hola! ¿Cómo estás?'),
        process_message(message, ['bye', 'chau', 'adios', 'hasta', 'luego'], '¡Chau! ¡Que la pases bien!'),
        process_message(message, ['como', 'estas', 'vos'], 'Yo estoy muy bien, muchas gracias.'),
        process_message(message, ['cual', 'es', 'tu', 'nombre', 'como', 'te', 'llamas'], 'Me llamo Diego Victoria.'),
        process_message(message, ['me', 'puedes', 'ayudar', 'help', 'ayuda'], '¡Sí! ¿En qué puedo ayudarte?'),
        process_message(message, ['turno', 'hay turno', 'puedo reservar', 'quiero turno', 'si', 'no'], 'Por favor, déjenos su número de teléfono y nos comunicaremos con usted a la brevedad.'),
        process_message(message, ['horario', 'atencion', 'abierto', 'cerrado'], 'Nuestros horarios de atención son de lunes a viernes de 8:00 a 13:00 horas. Los fines de semana y feriados atendemos de 9:00 a 13:00 horas'),
        process_message(message, ['cuanto', 'valor', 'entrada', 'cuánto', 'cuál', 'precio'], 'El valor de la entrada es $800. ¿Te gustaría reservar un turno?'),
        process_message(message, ['gracias', 'muchas gracias', 'ok'], '¡Gracias a usted!.'),
        
      
        process_phone_number(message)
    ]
    
    
    best_score = 0
    best_response = "Lo siento, no entiendo lo que dices."  

    for score, response in response_list:
        if score > best_score:
            best_score = score
            best_response = response

    
    print('La respuesta del Bot:', best_response)
    return best_response



if __name__ == "__main__":
    user_message = input("Escribe tu mensaje: ")
    bot_response = get_response(user_message)
    print(bot_response)
