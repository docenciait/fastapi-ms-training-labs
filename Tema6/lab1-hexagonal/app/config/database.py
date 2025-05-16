from databases import Database

DATABASE_URL = "mysql+aiomysql://user:password@db:3306/app_db"
database = Database(DATABASE_URL)