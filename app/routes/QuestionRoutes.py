from fastapi import APIRouter, Depends, Body
from typing import Annotated, Union

from app.depends import get_menu_service
from app.schemas.QuestionSchemas import QuestGet, QuestCreate, Message404, QuestReturn
from app.services.QuestionService import QuestionService

main_router = APIRouter()
debug_router = APIRouter()


@main_router.post(
    "/questions", response_model=Union[QuestGet, QuestReturn],

    summary="Загрузить вопросы с удаленного ресурса",
    response_description="Вопросы успешно загружены",
    status_code=201,
)
async def create_menu(
        num: Annotated[QuestCreate, Body(
            example={
                "questions_num": 1,
            }
        )],
        quest_service: Annotated[QuestionService, Depends(get_menu_service)],
):
    """
    Загрузить вопросы с удаленного ресурса \n
    "questions_num": 1 (укажите кол-во вопросов)
    """
    return await quest_service.add_questions(num=num.questions_num)


@debug_router.get(
    "/questions/{question_id}", response_model=QuestGet,
    responses={404: {"model": Message404}},
    summary="Получить вопрос по id",
    response_description="Полученный вопрос",
)
async def read_menu(
        question_id: int,
        quest_service: Annotated[QuestionService, Depends(get_menu_service)],
):
    """Получить вопрос по id"""
    return await quest_service.get_question_by_id(question_id)


@debug_router.get(
    "/questions",
    response_model=list[QuestGet],
    summary="Получить список всех вопросов",
    response_description="Список всех вопросов в БД",

)
async def get_all_questions(
        quest_service: Annotated[QuestionService, Depends(get_menu_service)],
):
    """Получить список всех вопросов"""
    return await quest_service.get_questions()

