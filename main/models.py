import sqlalchemy
from sqlalchemy import DateTime

from main.constants import *
from main.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("is_locked", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("is_blocked", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("is_premium", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("lock_password", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("location", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("gmail", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("current_chat_id", sqlalchemy.BigInteger, nullable=True),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.Enum(UserStatus), default=UserStatus.active, nullable=True),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)

directory = sqlalchemy.Table(
    "directories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("parent_id", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("owner_id", sqlalchemy.BigInteger, default=0),

    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.Enum(DirectoryStatus), default=DirectoryStatus.inactive),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)

files = sqlalchemy.Table(
    "files",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, nullable=True),
    sqlalchemy.Column("directory_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("directories.id"),
                      default=0),
    sqlalchemy.Column("file_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("hashtags", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("link", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("file_id", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.Enum(FileStatus), default=FileStatus.active),
    sqlalchemy.Column("file_type", sqlalchemy.Enum(FileType), default=FileType.photo),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)
