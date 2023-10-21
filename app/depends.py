from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.QuestionCRUD import QuestionCrud
from app.database.db import get_db
from app.services.QuestionService import QuestionService


def get_question_crud(db: Annotated[AsyncSession, Depends(get_db)]):
    return QuestionCrud(db)


def get_question_service(
        crud: Annotated[QuestionCrud, Depends(get_question_crud)],
):
    return QuestionService(crud)
