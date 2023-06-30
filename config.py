from os import getenv
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta
from discord_cooldown import (
    Cooldown,
    SQlite, MySQL, PostgreSQL
)

__all__ = [
    "Secrets",
    "CD",
]

load_dotenv(find_dotenv(raise_error_if_not_found=True))


class Secrets:
    token: str = getenv("TOKEN")

    # If you want to use MySQL or PostgreSQL then uncomment below code
    db_host = getenv("DB_HOST")
    db_port = getenv("DB_PORT")
    db_user = getenv("DB_USER")
    db_passwd = getenv("DB_PASSWD")
    db_name = getenv("DB_NAME")


# For sqlite
db = SQlite()

# For mysql
# db = MySQL(
#     host=Secrets.db_host, port=int(Secrets.db_port),
#     user=Secrets.db_user, passwd=Secrets.db_passwd,
#     db_name=Secrets.db_name
# )

# for postgresql
# db = PostgreSQL(
#     host=Secrets.db_host, port=int(Secrets.db_port),
#     user=Secrets.db_user, passwd=Secrets.db_passwd,
#     db_name=Secrets.db_name
# )

# For Indian timezone, use this
timezone = +timedelta(hours=5, minutes=30)

# For US timezone, use this
# timezone = -timedelta(hours=4)


# don't pass any timezone to make it UTC time
CD = Cooldown(db, timezone)
