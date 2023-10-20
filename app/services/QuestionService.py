from typing import Sequence, Type
from datetime import datetime
import requests
from fastapi import HTTPException

from app.crud.QuestionCRUD import QuestionCrud
from app.models.QuestionModels import QuestionModels


def get_questions_from_api(num: int) -> dict:
    response = requests.get(f"https://jservice.io/api/random?count={num}")
    return response.json()


def write_duplicate_log(q_id) -> None:
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as f:
        f.write(f"{date} - Duplicate outer id - {q_id}\n")


LAST = {}


class QuestionService:
    def __init__(self, crud: QuestionCrud):
        self.crud = crud

    async def get_questions(self) -> Sequence[QuestionModels]:
        return await self.crud.get_list()

    async def get_question_by_id(self, _id: int) -> Type[QuestionModels]:
        question = await self.crud.get(_id)
        if question is None:
            raise HTTPException(status_code=404, detail="Question not found")
        return question

    async def add_questions(self, num) -> dict:
        global LAST
        result = LAST
        unique_questions = []
        questions = get_questions_from_api(num)
        count = 0
        for question in questions:
            check_in_base = await self.crud.get(question['id'])
            while check_in_base:
                count += 1
                write_duplicate_log(question['id'])
                question = get_questions_from_api(1)[0]
                check_in_base = await self.crud.get(question['id'])
                if count > 10:
                    break
                if not check_in_base:
                    break
            unique_questions.append(question)

        data = await self.crud.create(unique_questions)
        LAST = data
        return result

