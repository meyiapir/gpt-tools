import openai

class GetAnswer:
    def __init__(self, question: str, max_tokens: int = None):
        self.question = question
        self.base_query = None
        self.max_tokens = max_tokens

    def get_answer(self, base_query: str):
        self.base_query = base_query
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{self.base_query} Text: \"{self.question}\"",
            max_tokens=len(self.question.strip()) * 4 + 10
        ) if self.max_tokens is None else openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{self.base_query} Text: \"{self.question}\"",
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()
