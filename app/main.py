from fastapi import FastAPI
from app.routes.QuestionRoutes import main_router, debug_router


app = FastAPI(
    title="BeWise Quiz Game Questions",
)

app.include_router(
    debug_router,
    prefix="/api/v1",
    tags=["Debug"],
)

app.include_router(
    main_router,
    prefix="/api/v1",
    tags=["Questions"],
)


