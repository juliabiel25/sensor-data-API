from .sql_app.database import SessionLocal

# create a new SQLAlchemy session that will be used in a single request and then close it once the request is finished
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
