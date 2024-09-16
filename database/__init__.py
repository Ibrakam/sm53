from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# Указываем тип бд(sqlite, postgres)
SQLALCHEMY_DATABASE_URI = "sqlite:///social_media.db"
# Создадим движок
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Создаем сессию чтобы хранить данные
SessionLocal = sessionmaker(bind=engine)
# Создаем полноценню базу
Base = declarative_base()


# Подключение к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()



