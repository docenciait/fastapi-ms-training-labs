import sqlalchemy
from databases import Database
from app.core.models import User

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

class MariaDBUserRepository:
    def __init__(self, db: Database):
        self.db = db

    async def list_users(self):
        query = users.select()
        rows = await self.db.fetch_all(query)
        return [User(id=row["id"], name=row["name"]) for row in rows]