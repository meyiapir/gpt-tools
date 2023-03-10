from gptools.modules.api_query import GetAnswer
from gptools.modules.BASE_QUERIES import (
    BASE_QUERY_CORRECT,
    BASE_QUERY_TRANSLATE
)

class TextEdit(GetAnswer):
    def __init__(self, text: str, max_tokens: int = None):
        super().__init__(text, max_tokens)

    def correct(self):
        return self.get_answer(BASE_QUERY_CORRECT)

    def translate(self, to_lang: str = "English"):
        return self.get_answer(BASE_QUERY_TRANSLATE.format(to_lang))
