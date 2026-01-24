"""
Задание 1. Получение данных из публичного API
Скрипт отправляет GET-запрос к JSONPlaceholder /posts
и выводит заголовки и тела первых 5 постов.
"""

import requests


def get_posts():
    """Получает и выводит первые 5 постов из JSONPlaceholder API."""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        response.raise_for_status()

        posts = response.json()

        print("=" * 60)
        print("Первые 5 постов из JSONPlaceholder API")
        print("=" * 60)

        for i, post in enumerate(posts[:5], 1):
            print(f"\nПост #{i}")
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}")
            print("-" * 60)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")


if __name__ == "__main__":
    get_posts()
