import requests
import json
import uuid

class GigaChatAPI:
    def __init__(self, api_token):
        self.api_token = api_token
        self.access_token = None
        self.conversation_history = []

    def get_token(self, scope="GIGACHAT_API_PERS"):
        # Создаем идентификатор UUID (36 знаков)
        rq_uid = str(uuid.uuid4())

        # API URL
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        # Заголовки
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "RqUID": rq_uid,
            "Authorization": f"Basic {self.api_token}"
        }

        # Тело запроса
        payload = {
            'scope': scope
        }

        try:
            # Делаем POST запрос с отключенной SSL верификацией
            response = requests.post(url, headers=headers, data=payload, verify=False)
            if response.status_code == 200:
                self.access_token = response.json().get("access_token")
                print("Токен успешно получен.")
            else:
                print(f"Ошибка при получении токена: {response.text}")
        except requests.RequestException as e:
            print(f"Ошибка: {str(e)}")
            self.access_token = None

    def send_message(self, user_message):
        if not self.access_token:
            print("Токен не найден. Получите токен перед выполнением запроса.")
            return None

        # URL API, к которому мы обращаемся
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        # Добавляем сообщение пользователя в историю диалога
        self.conversation_history.append({
            'role': 'user',
            'content': user_message,
        })

        # Тело запроса
        payload = json.dumps({
            "model": "GigaChat",
            "messages": self.conversation_history,
            "temperature": 1,
            "top_p": 0.1,
            "n": 1,
            "stream": False,
            "max_tokens": 512,
            "repetition_penalty": 1,
            "update_interval": 0,
        })

        # Заголовки запроса
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

        try:
            # Выполнение POST-запроса
            response = requests.post(url, headers=headers, data=payload, verify=False)
            if response.status_code == 200:
                request_data = response.json()

                # Добавляем ответ модели в историю диалога
                self.conversation_history.append({
                    'role': 'assistant',
                    'content': request_data['choices'][0]['message']['content'],
                })

                return request_data['choices'][0]['message']['content']
            else:
                print(f"Ошибка при получении ответа от GigaChat: {response.text}")
                return None
        except requests.RequestException as e:
            print(f"Ошибка: {str(e)}")
            return None


