import random
from random import randint

import requests
from loguru import logger


class CatAPIService:
    """
    Сервис для получения изображений котов с публичного API.
    """
    BASE_URL = "https://api.thecatapi.com/v1/images/search"

    @staticmethod
    def get_cat_photos(count: int = 1) -> list[str]:
        """
        Получает список URL изображений котов.

        :param count: количество изображений (1–3)
        :return: список URL
        """
        try:
            response = requests.get(CatAPIService.BASE_URL, params={"limit": count}, timeout=5)
            response.raise_for_status()
            data = response.json()
            return [item["url"] for item in data][:count]
        except Exception as e:
            logger.error(f"Ошибка при получении фото кота: {e}")
            return []


class GoodNightMessage:
    """
    Генератор сообщений «Спокойной ночи» с вариациями текста и эмодзи.
    """

    GREETINGS = [
        "Сладких снов",
        "Спокойной ночи",
        "Приятных сновидений",
        "Пусть приснится что-то хорошее",
        "До завтра",
        "Пусть ночь будет уютной",
        "Мягких подушек и тёплого одеяла",
        "Пусть приснится что-то волшебное",
        "До встречи в новом дне",
        "Отдыхай и набирайся сил",
        "Пусть утро будет лёгким и радостным",
        "Сон принесёт новые идеи",
        "Пусть ночь подарит покой",
        "Добрых грёз",
        "Сладких и ярких снов",
        "Пусть твой сон будет глубоким",
        "Скорее засыпай в уюте",
        "Мирных и спокойных снов",
        "Счастливых сновидений",
        "Пусть твои мечты будут красивыми"
    ]

    EMOJIS = [
        "🌌", "☄️", "⭐", "✨", "🌃", "🌙", "💤", "🛌",
        "🌠", "🌑", "🌒", "🌓", "🌔", "🌕",
        "🐱", "🐾", "🦉", "🕊️", "🌺", "🌸",
        "🍵", "🕯️", "🌲", "🌳"
    ]

    @staticmethod
    def get_message() -> str:
        """
        Формирует случайное пожелание на ночь.
        """
        greeting = random.choice(GoodNightMessage.GREETINGS)
        emojis = "".join(random.sample(GoodNightMessage.EMOJIS, k=randint(2, 4)))
        return f"{greeting} {emojis}"