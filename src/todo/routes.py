from fastapi import APIRouter, status
from typing import List
from src.todo.todo_data import todos
from src.todo.schemas import TodoSchema, TodoUpdateSchema
from fastapi.exceptions import HTTPException



todo_router = APIRouter()


# Get all todos
@todo_router.get("/all_todos", response_model=List[TodoSchema])
async def all_todos():
    return todos


# Add new todo
@todo_router.post("/new_todo", status_code=status.HTTP_201_CREATED)
async def new_todo(todo_data: TodoSchema) -> dict:
    new_todo = todo_data.model_dump()
    todos.append(new_todo)
    return new_todo

# Get a todo item 
@todo_router.get("/todo_details/{todo_id}")
async def todo_details(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not Found")


# Update a todo item
@todo_router.patch("/update_todo/{todo_id}")
async def update_todo(todo_id: int, todo_data: TodoUpdateSchema) -> dict:
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = todo_data.title
            todo["content"] = todo_data.content

            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not Found")


# Delete a todo
@todo_router.delete("/delete_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo successfully deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not Found")