from fastapi import FastAPI
from blog import schemas, models
from blog.database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(authentication.router)  # ✅ Include the authentication router


app.include_router(blog.router)  # ✅ Include the blog router

app.include_router(user.router)  # ✅ Include the user router


