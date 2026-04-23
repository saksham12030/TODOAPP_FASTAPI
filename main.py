from fastapi import FastAPI,Depends
from pydantic import BaseModel
from models import TodoModel
from database import sessionLocal,engine
from typing import Optional,List
from sqlalchemy.orm import Session

app=FastAPI();


TodoModel.metadata.create_all(bind=engine)

# class TodoUpdate(BaseModel):
#     title: Optional[str] = None
#     description: Optional[str] = None
#     completed: Optional[bool] = None
    
    
class TodoBase(BaseModel):
    title: str
    description: Optional[str]=None
    completed: bool = False

class ToDoResponse(TodoBase):
    id : int

    class Config:
        orm_mode:True 
        
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close();

@app.get("/")
def gethealth():
    return {"data":os.getenv('foo')}
    
@app.get("/todos",response_model=List[ToDoResponse])
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(TodoModel).all()
    return todos

@app.get("/todos/{todo_id}",response_model=ToDoResponse)
def get_todo(todo_id:int, db:Session=Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id==todo_id)
    return todo.first();

@app.post("/todos",response_model=ToDoResponse)
def createtodo(todo:TodoBase, db : Session = Depends(get_db)):
    
    todo=TodoModel(title=todo.title,description=todo.description,completed=todo.completed)
    db.begin()
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}",response_model=ToDoResponse)
def deletetodo(todo_id:int, db : Session = Depends(get_db)):
    todo=db.query(TodoModel).filter(TodoModel.id==todo_id).first()
    db.begin()    # force the transaction to begin
    db.delete(todo)
    db.commit()
    return todo
    
# @app.patch("/todos/{todo_id}")
# def updateTodo(todo_id:int, updateddata:TodoUpdate):

#     for todo in todos:
#         if todo["id"]==todo_id:
#             data=updateddata.dict(exclude_unset=True);
#             todo.update(data)
#             return todo
#     return {"Error":"Todo not found"}

