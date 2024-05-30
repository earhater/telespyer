from alembic import context
from dotenv import load_dotenv
from sqlalchemy import create_engine, pool
from logging.config import fileConfig
import sys
import os

from database.models.User import BaseModel
from database.models.Channels import BaseModel
from database.models.Appearances import BaseModel
load_dotenv()
# Add your project directory to the sys.path to ensure the models can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your models here  # Import Base from your models package

# this is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("PG_CONNECT"))
# Interpret the config file for Python logging.
fileConfig(config.config_file_name)


# add your model's MetaData object here for 'autogenerate' support
target_metadata = BaseModel.metadata  # Corrected to use Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )

    with context.begin_transaction():
        context.run_migration()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(config.get_main_option("sqlalchemy.url"))

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
