from datetime import datetime
from typing import Type, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.QuestionModels import QuestionModels
from app.schemas.QuestionSchemas import QuestCreate


class QuestionCrud:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, q_id: int) -> Type[QuestionModels]:
        return await self.db.get(QuestionModels, q_id)

    async def get_list(self) -> Sequence[QuestionModels]:
        return (
            await self.db.execute(select(QuestionModels))
        ).scalars().fetchall()

    async def create(self, questions: list[QuestCreate]):
        for q in questions:
            created_at = datetime.strptime(q['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
            new = QuestionModels(id=q['id'], question=q['question'], answer=q['answer'], created_at=created_at)
            self.db.add(new)
        await self.db.commit()
        await self.db.refresh(new)
        return new
