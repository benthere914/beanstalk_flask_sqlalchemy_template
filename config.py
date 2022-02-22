import os
username = ""
password = ""
rds_endpoint = ""
rds_port = ""
rds_database_name = ""
class Config:
    SECRET_KEY = 'SECRET'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{rds_endpoint}:{rds_port}/{rds_database_name}"
