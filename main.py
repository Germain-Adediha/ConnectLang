from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
import databases

# Create FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = "postgresql://germain:17koffiGerkoff@localhost/connectlang"
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    language = Column(String, index=True)
    chosen_language = Column(String, index=True)
    known_language = Column(String, index=True)
    spoken_language = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API routes
@app.post("/users/", response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# New API route for searching users
@app.get("/search_users/", response_model=list[User])
async def search_users(
    chosen_language: str = Query(..., title="Chosen Language"),
    known_language: str = Query(..., title="Known Language"),
    spoken_language: str = Query(..., title="Spoken Language"),
    db: Session = Depends(get_db),
):
    users = (
        db.query(User)
        .filter(
            User.language == chosen_language,
            User.known_language == known_language,
            User.spoken_language == spoken_language,
        )
        .all()
    )
    return users