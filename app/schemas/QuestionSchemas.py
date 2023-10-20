from datetime import datetime

from pydantic import BaseModel, field_validator


class QuestCreate(BaseModel):
    questions_num: int

    @field_validator("questions_num")
    def validate_questions_num(cls, value):
        if value <= 0:
            raise ValueError("the number must be greater than 0")
        return value


class QuestGet(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        from_attributes = True


class QuestReturn(BaseModel):
    pass


class Message404(BaseModel):
    detail: str
