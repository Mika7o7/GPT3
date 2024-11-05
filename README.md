# GigaChat Console Application

### Описание проекта

Это консольное приложение на языке Python предоставляет удобный способ взаимодействия с нейронной сетью GigaChat. Пользователь может вводить запросы, отправлять их в нейронную сеть через API и получать ответы прямо в консоли. Приложение поддерживает простое управление доступом с использованием токенов API и предлагает приятный опыт общения с искусственным интеллектом.

---

### Функциональные возможности

- **Ввод произвольных запросов**: Пользователь может вводить любые текстовые сообщения.
- **Отправка запросов в нейронную сеть**: Сообщения отправляются в GigaChat через API.
- **Получение ответов**: Ответы от нейронной сети выводятся в консоли.
- **Выход из приложения**: Завершите работу приложения командами `exit` или `quit`.
- **Управление доступом**: Использование токенов для авторизации в API.

---

### Установка и настройка

1. **Клонируйте репозиторий на ваш компьютер**:
   ```bash
   git clone https://github.com/Mika7o7/GPT3.git
   cd GPT3


2. **Создайте и активируйте виртуальное окружение**:
   
   **Для Linux и macOS**:
   ```bash
   python3 -m venv env
   source env/bin/activate

   **Для Windows**:
   ```bash
    python3 -m venv env
    env\Scripts\activate


3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt


4. **Создайте файл SECRETS в корневой папке проекта**:

    ### В файле SECRETS укажите ваши API токены и секретные ключи в следующем формате:
   ```makefile
   API_TOKEN=ваш_токен

**Использование**

    **Запустите приложение**:

    ```bash
    python main.py

### Введите ваш запрос: Просто напишите сообщение и нажмите Enter. Приложение отправит запрос в нейронную сеть и выведет полученный ответ.
### Завершите работу: Для выхода из программы введите exit или quit и нажмите Enter.

