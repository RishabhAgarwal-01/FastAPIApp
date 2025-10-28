from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth
from .config import settings


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastAPI", user="postgres", 
#                                 password="rishabh46", cursor_factory=RealDictCursor)
        
#         cursor = conn.cursor()
#         print("Database connection is successful")
#         break
#     except Exception as error:
#         print(f"Connection failed due to {error}")
#         time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "First path operation"}
