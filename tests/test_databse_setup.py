import sqlalchemy

from typing import Any
from sqlalchemy.orm import declarative_base

from twelve_factor_app import app, Config, ConfigStrategy


config = Config.get_instance(ConfigStrategy.ENV_VAR)

host = config.get_string(Config.DATABASE_HOST)
port = config.get_string(Config.DATABASE_PORT)
user = config.get_string(Config.DATABASE_USER)
password = config.get_string(Config.DATABASE_PASSWORD)
database = config.get_string(Config.DATABASE_NAME)
database_engine = config.get_string(Config.DATABASE_ENGINE)
database_url = f"{database_engine}://{user}:{password}@{host}:{port}/test_{database}"


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
