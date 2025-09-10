import re


class Enricher:

    @staticmethod
    def risk_score(text: str, hostile_words: list, less_hostile_words: list):
        text = re.sub(r'[^\w\s]', '', text.lower())
        words = text.split()
        score = 0

        for h in hostile_words:
            if len(h) == 1:
                if h in words:
                    score += 2

            elif len(h) > 1:
                if h in text:
                    score += 2

        for lh in less_hostile_words:
            if len(lh) == 1:
                if lh in words:
                    score += 1

            elif len(lh) > 1:
                if lh in text:
                    score += 1


        return score

    @staticmethod
    def danger_percentages(len_of_text: int, score: int):
        percentage_impression =  (score / len_of_text) * 100
        if percentage_impression < 1:
            danger_percentages = percentage_impression * 10
        elif percentage_impression < 2:
            danger_percentages = percentage_impression * 20
        else:
            danger_percentages = percentage_impression * 30


        return danger_percentages if danger_percentages < 100 else 100

    @staticmethod
    def is_bds(percentage: int):
        return percentage > 30

    @staticmethod
    def risk_level(percentage: int):
        if percentage <= 10:
            return 'none'
        elif percentage <= 30:
            return 'medium'
        else:
            return 'high'

