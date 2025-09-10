import re


class Enricher:

    @staticmethod
    def risk_score(text: str, hostile_words: list, less_hostile_words: list):
        """
        The function receives two lists and text,
        the lists contain dangerous words to search for in the text.
        One of the lists is more dangerous,
        so each word in it will receive a double rating.
        The function returns a rating of the text,
        according to the occurrences of the dangerous words in it.
        """
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
        """
        The function receives len of text and score,
        it calculates the risk percentage according to the score and len of the text.
        and returns a risk level according to the percentage of appearances in the text,
        where the higher the percentage of appearances,
        the higher the risk percentage
        """
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
        """
        The function accepts a percentage,
        and returns whether it is a sufficient percentage to determine risk.
        """
        return percentage > 30

    @staticmethod
    def risk_level(percentage: int):
        # The function accepts percentages and returns the risk level.
        if percentage <= 10:
            return 'none'
        elif percentage <= 30:
            return 'medium'
        else:
            return 'high'

