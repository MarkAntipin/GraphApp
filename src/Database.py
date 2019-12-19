import string
import random
from itertools import product

from utils import log
from models import Words, db


class Database(object):
    database = db
    WordsModel = Words
    word_size = 2
    available_letters = [l for l in string.ascii_lowercase]

    def add_word(self, word: str):
        assert len(word) == self.word_size, (
            f"length of word must be {self.word_size}"
        )
        assert word[0] and word[1] in self.available_letters, (
            f"word must can contain only {self.available_letters}"
        )
        self.WordsModel.create(word=word)

    def get_all_words(self) -> list:
        record = self.WordsModel.select()
        return [r.word for r in record]

    def __get_n_random_words(self, n: int) -> list:
        all_words = self.get_all_words()

        assert len(all_words) < n, log.error("Database doesn't have so much words")

        return [random.choice(all_words) for _ in range(n)]

    def _add_n_random_word(self, n: int):
        """
        developer function for fast db filling
        """
        letters = [l for l in string.ascii_lowercase]
        comb = product(letters, repeat=self.word_size)
        all_words = [''.join(c) for c in comb]
        random_words = [self.WordsModel(word=random.choice(all_words)) for _ in range(n)]
        with self.database.atomic():
            self.WordsModel.bulk_create(random_words, batch_size=100)
