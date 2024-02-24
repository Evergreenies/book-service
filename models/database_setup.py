import uuid
import sqlalchemy

from typing import Any
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

# from sqlalchemy.ext.declarative import DeferredReflection  # declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base


from twelve_factor_app import app, Config, ConfigStrategy


config = Config.get_instance(ConfigStrategy.ENV_VAR)

book_app = app()

host = config.get_string(Config.DATABASE_HOST)
port = config.get_string(Config.DATABASE_PORT)
user = config.get_string(Config.DATABASE_USER)
password = config.get_string(Config.DATABASE_PASSWORD)
database = config.get_string(Config.DATABASE_NAME)
database_engine = config.get_string(Config.DATABASE_ENGINE)
database_url = f"{database_engine}://{user}:{password}@{host}:{port}/{database}"

book_app.config["SQLALCHEMY_DATABASE_URI"] = database_url


class Engine:
    host = host
    port = port
    user = user
    password = password
    database = database
    database_engine = database_engine

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return sqlalchemy.create_engine(
            f"{database_engine}://{user}:{password}@{host}:{port}/{database}",
            connect_args=dict(connect_timeout=10),
        )


Base = declarative_base()

engine_maker = Engine()
db = SQLAlchemy(app.app)
db_engine = engine_maker()
session_maker = sessionmaker(bind=db_engine)


class UUID4(db.TypeDecorator):
    impl = UUID

    def process_bind_param(self, value, dialect):
        if value is None:
            return uuid.uuid4()
        return value

    def process_result_param(self, value, dialect):
        return value
