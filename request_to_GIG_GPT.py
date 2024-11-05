import os
from dotenv import load_dotenv

from models import GigaChatAPI





def main():

    # Определите путь к файлу SECRETS
    current_directory = os.path.dirname(__file__)
    secrets_path = os.path.join(current_directory, "SECRETS")



    # Загрузка данных из файла SECRETS
    load_dotenv(secrets_path)
    api_token = os.getenv("API_TOKEN") # Замените на ваш токен


    # Используем ваш уже существующий класс GigaChatAPI
    gigachat = GigaChatAPI(api_token)  # Создайте объект вашего класса
    gigachat.get_token()  # Получите токен доступа

    if not gigachat.access_token:
        print("Не удалось получить токен доступа. Завершаем работу.")
        return

    print("Добро пожаловать в консольный чат! Введите 'exit' для выхода.")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ["exit", "quit"]:
            print("До свидания!")
            break
        
        # Отправляем запрос пользователя и получаем ответ
        response = gigachat.send_message(user_input)
        if response:
            print(f"GigaChat: {response}")
        else:
            print("Не удалось получить ответ от нейронной сети.")



if __name__ == "__main__":
    main()