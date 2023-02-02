import openai


class GetAnswerText:
    @classmethod
    def get_answer(cls, query: str, max_tokens: int = 1024):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=max_tokens
        )
        return response['choices'][0]['text'].strip()