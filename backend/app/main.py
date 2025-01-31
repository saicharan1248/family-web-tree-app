from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routes import family_tree

app = FastAPI()

app.include_router(family_tree.router)

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Family Tree API"}