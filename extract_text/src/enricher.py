class Enricher:

    @staticmethod
    def risk_score(text: str, hostile_words: list, less_hostile_words: list):
        words = text.split()
        score = 0
        word_count = 0
        for h in hostile_words:
            if len(h) == 1:
                if h in words:
                    score += 10
                    word_count += 1
            elif len(h) > 1:
                if h in text:
                    score += 10
                    word_count += 1

        for lh in less_hostile_words:
            if len(lh) == 1:
                if lh in words:
                    score += 10
                    word_count += 1
            elif len(lh) > 1:
                if lh in text:
                    score += 5
                    word_count += 1

        return score, word_count

    @staticmethod
    def danger_percentages(len_of_text: int, score: int, word_count: int):
        percentage = len_of_text / 100 * score * word_count
        return percentage if percentage < 100 else 100

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

