from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from db.database import engine, get_db, SessionLocal
from users import user_model
from users.user_schemas import UserRequest, UserResponse
from users.user_model import User
from sqlalchemy.orm import Session
from users.user_schemas import UserBase

from datetime import datetime, date, timedelta, time
import pandas as pd

from fastapi.middleware.cors import CORSMiddleware


db = SessionLocal()

app = FastAPI()

"""
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
origins = [
    "http://localhost",
#    "http://localhost:4200",
    "http://localhost:8080",
    "http://localhost:8081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


user_model.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return { 'message': 'Server alive!', 'time': datetime.now() }

@app.get('/api/clientes', status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    print('ANGULAR')
    all_users = db.query(User).all()
    return all_users

@app.get('/api/users', status_code=status.HTTP_200_OK, response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users

@app.post('/api/clientes', status_code=status.HTTP_201_CREATED, response_model=UserResponse) 
def create_user(user: UserRequest, db: Session = Depends(get_db)):  
    print('Crear', user)    
    new_user = user_model.User(name=user.name, surname=user.surname, email=user.email, password=user.password, fchnace=user.fchnace)
    db.add(new_user)
    db.commit()
#    db.refresh(new_user)
    return new_user

@app.delete('/api/clientedeletei/{todo_id}', response_model=UserResponse, status_code=200)
def delete_Todo(todo_id: int): 
    print('MIERDA 1', todo_id)
    find_Todo = db.query(user_model.User).filter(
        user_model.User.id == todo_id).first()  
    if find_Todo is not None:
        db.delete(find_Todo)
        db.commit()
        print('MIERDA 2', find_Todo)
        return find_Todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="No Delete")


@app.delete('/api/clientedelete/{todo_id}', response_model=UserResponse, status_code=200)
def delete_Todo(todo_id: int):
    # Delete a Todo from the database
    find_Todo = db.query(user_model.User).filter(
        user_model.User.id == todo_id).first()
    if find_Todo is not None:
        db.delete(find_Todo)
        db.commit()
        return find_Todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Todo not found")

# Read (GET)
@app.get("/api/clientes/{item_id}")
async def read_item(item_id: int):
    print('MIERDA 3', item_id)
    db = SessionLocal()
    item = db.query(User).filter(User.id == item_id).first()
    return item

# Read (GET)
@app.get("/api/clientes/{item_id}")
async def read_item(item_id: int):
    print('MIERDA 3', item_id)
    db = SessionLocal()
    item = db.query(User).filter(User.id == item_id).first()
    return item
  
# Update (PUT)
@app.put("/api/items/{item_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_item(item_id: int, name: str, surname: str, email: str, password: str):
    db = SessionLocal()
    db_item = db.query(user_model.User).filter(user_model.User.id == item_id).first()
    if db_item is not None:
        db_item.name = name
        db_item.surname = surname
        db_item.email = email
        db_item.password = password
        db.commit()
        return db_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Todo not found db_item")
    
@app.put("/api/update/{id}")
def updateTodo(id: int, product: UserBase, db:Session = Depends(get_db)):
    updated_post = db.query(user_model.User).filter(user_model.User.id == id).first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post with such id: {id} does not exist')
    else:
        updated_post.update(product.dict(), synchronize_session=False)
        db.commit()
    return updated_post.first()

@app.put('/api/update_todo/{todo_id}', status_code=status.HTTP_202_ACCEPTED)
def update_Chito(todo_id: int, todo: UserBase):
    # Update a Todo's details in the database
    find_Todo = db.query(user_model.User).filter(user_model.User.id == todo_id).first()
    if find_Todo is not None:         
        enacimiento = todo.fchnace
        fecha_nacimiento = pd.to_datetime(enacimiento)
        ydia = fecha_nacimiento.day
        ymes = fecha_nacimiento.month
        yano = fecha_nacimiento.year
        print("")
        print("Fecha_Nacimiento es: ", fecha_nacimiento)      
        print("Dia Nacimiento es: ", ydia)
        print("Dia Nacimiento es: ", ymes)
        print("Dia Nacimiento es: ", yano)
        print("")
        
        fecha_actual = datetime.now()
        dactual = fecha_actual.day
        mactual = fecha_actual.month
        yactual = fecha_actual.year
        print("Fecha_Actual es: ", fecha_actual)      
        print("Dia Actual es: ", dactual)
        print("Mes Actual es: ", mactual)
        print("Ano Actual es: ", yactual)        
        print("")
        efecha = yactual - yano
                
        if ymes > mactual:
            if ydia > dactual:
                efecha = efecha - 1
                print('Edad : ', efecha)
        else:
         print('Edad : ', efecha)   
                     
        if ymes > mactual:
            if ydia < dactual:
                efecha = efecha - 1
                print('Edad : ', efecha)
        else:
            print('Edad : ', efecha)                            
#        print(f"Tu edad es: {efecha} años")
        print("")
#-----------------------------------------------------------                 
        fecha1 = date(2023, 7 ,2)
        fecha2 = date(2023, 7, 11)
        diferencia = fecha2 - fecha1
        print('Dias de diferencia : ', diferencia)
        dias = diferencia.days
        print('Hay ', dias, 'dias de diferencia ')
        print("")
#---------------------------------------------------------          
        # today = date.today()
        # print("Today's date:", today)        
        # print ('Name : ', todo.name)
        # print ('Surname : ', todo.surname)  
        # print ('Fchnace : ', todo.fchnace)       
        # date1 = today.strftime('%d/%m/%Y')
        # print('date1 =', date1)      
        # print ('find_Todo email: ', find_Todo.email)
        
#--------------------------------------------------------------------------

        # fecha_inicio = datetime.date(2024, 6, 11)
        # print('Fecha inicio : ', fecha_inicio)      
        # periodo = 1    # en años
        # intervalo_pago = 30     # en días
        # fecha_fin = fecha_inicio + datetime.timedelta(days=365 * periodo)
        # print('Fecha fin : ', fecha_fin)       
        # fechas_de_pago = []
        # while fecha_inicio <= fecha_fin:
        #     fecha_inicio = fecha_inicio + datetime.timedelta(days=45)
        #     fechas_de_pago.append(fecha_inicio)
        # print('Fechas de pago : ', fechas_de_pago)
        
#---------------------------------------------------------------------------        
            
        find_Todo.name = todo.name
        find_Todo.surname = todo.surname
        find_Todo.email = todo.email
        find_Todo.password = todo.password
        find_Todo.fchnace = todo.fchnace
        db.commit()
        return find_Todo
   
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Todo not found")
 
 #-----------------------------------------------
    



