from fastapi import FastAPI
from src.todo.routes import todo_router

version = "v1"


app = FastAPI(
    title = "Todo App",
    description = "This is a todo app",
    version = version
)

app.include_router(todo_router, prefix=f"/api/{version}/todo", tags=['todo'])