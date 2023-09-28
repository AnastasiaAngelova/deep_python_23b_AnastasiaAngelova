"""Задание 1 ДЗ 1"""
import random


class SomeModel:
    """
    Пример модели, используемой для предсказания настроения сообщения.
    """

    def predict(self, message: str) -> float:
        """
        Предсказывает настроение сообщения.
        """
        return random.random()


def check_thresholds(bad_threshold: float, good_threshold: float):
    """
    Проверяет корректность значений порогов настроения.
    """
    if (not isinstance(bad_threshold, (float, int))
            or not isinstance(good_threshold, (float, int))):
        raise ValueError("bad_threshold и good_threshold должны быть числами")

    if (not (0 <= bad_threshold <= 1) or not (0 <= good_threshold <= 1)
            or bad_threshold >= good_threshold):
        raise ValueError("Неправильные значения bad_threshold "
                         "и good_threshold")


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_threshold: float = 0.3,
        good_threshold: float = 0.8,
) -> str:
    """
    Предсказывает настроение сообщения на основе заданных порогов.
    """
    check_thresholds(bad_threshold, good_threshold)

    if not message.strip():
        raise ValueError("Сообщение не может быть пустым")

    mood_score = model.predict(message)

    if mood_score <= bad_threshold:
        return "неуд"
    if mood_score >= good_threshold:
        return "отл"
    return "норм"
