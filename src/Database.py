import string
import random
from itertools import product

from models import Words, db


class Database(object):
    database = db
    WordsModel = Words
    words_available_sizes = {2, 3}
    available_letters = [later for later in string.ascii_lowercase]

    def add_word(self, word: str):
        assert len(word) in self.words_available_sizes, (
            f"length of word must be in {self.words_available_sizes}"
        )
        for letter in word:
            assert letter in self.available_letters, (
                f"word must can contain only {self.available_letters}"
            )
        self.WordsModel.create(word=word)

    def get_all_words(self):
        record = self.WordsModel.select()
        return [r.word for r in record]

    def get_words(self, word_length: int) -> list:
        record = self.WordsModel.select().where(
            self.WordsModel.word_length == word_length
        )
        return [r.word for r in record]

    def _add_n_random_word(self, n: int, word_length: int):
        """
        developer function for fast db filling
        """
        comb = product(self.available_letters, repeat=word_length)
        all_words = [''.join(c) for c in comb]
        random_words = [
            self.WordsModel(word=random.choice(all_words), word_length=word_length)
            for _ in range(n)
        ]
        with self.database.atomic():
            self.WordsModel.bulk_create(random_words, batch_size=100)
