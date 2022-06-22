from question import quiz


def check_ans(question, ans, attempts, score):
    """
    Toma los argumentos y confirma si la respuesta proporcionada por el usuario es correcta.
    Convierte todas las respuestas a minúsculas para asegurarse de que el cuestionario no distinga entre mayúsculas
    y minúsculas.
    """
    if quiz[question]['respuesta'].lower() == ans.lower(): #answer
        print(f"Respuesta correcta! \nTu puntaje es {score + 1}!")
        return True
    else:
        print(f"Respuesta equivicada :( \nte quedan {attempts - 1} intentos restantes! \nPrueba de nuevo...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
    Presenta al usuario el quiz y las reglas, y toma una entrada del usuario para iniciar el quiz.
     Devuelve verdadero independientemente de cualquier tecla presionada.
    """
    print("Bienvenido al juego de trivia \n¿Estás listo para poner a prueba tus conocimientos sobre cultura general?")
    print("Hay un total de 6 preguntas, puede omitir una pregunta en cualquier momento escribiendo 'skip'")
    input("Presiones cualquier tecla para comenzar ;) ")
    return True


# python project.py
intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['pregunta']) #question
            answer = input("Ingrese la respuesta (Para pasar a la siguiente pregunta, escriba 'skip'): ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1
    break

print(f"Tu puntaje final es : {score}!\n\n")
print("¿Quieres saber las respuestas correctas? ¡Véalas a continuación! ;)\n")
print_dictionary()
print("Gracias por jugar!! 💜")
