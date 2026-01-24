"""
Задание 2. Работа с параметрами запроса
Программа принимает название города от пользователя,
отправляет GET-запрос к OpenWeather API и выводит
текущую температуру и описание погоды.
"""

import requests


API_KEY = "......"


def get_weather(city: str):
    """Получает и выводит погоду для указанного города."""
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric", 
        "lang": "ru"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]

        print("=" * 40)
        print(f"Погода в городе: {city_name}")
        print("=" * 40)
        print(f"Температура: {temperature}°C")
        print(f"Описание: {description}")

    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Ошибка: Неверный API ключ.")
            print("Получите ключ на https://openweathermap.org/api")
        elif response.status_code == 404:
            print(f"Ошибка: Город '{city}' не найден.")
        else:
            print(f"HTTP ошибка: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")


def main():
    """Основная функция программы."""
    print("Программа для получения погоды")
    print("-" * 40)

    city = input("Введите название города: ").strip()

    if not city:
        print("Ошибка: Название города не может быть пустым.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
