from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import os
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option('sqlalchemy.url', os.getenv('DB_URI', "sqlite:///./sqlite.db"))
# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from sqlmodel import SQLModel

from appmodels.airflow.dag import Dag
from appmodels.airflow.dag_run import DagRun

from appmodels.airflow.dag_task import DagTask
from appmodels.airflow.dag_task_run import DagTaskRun

from appmodels.email.contact import Contact
from appmodels.email.mail_server import MailServer
from appmodels.email.mailbox import Mailbox
from appmodels.email.attachment import Attachment
from appmodels.email.category import Category
from appmodels.email.email import Email, SentBCCContactLink,SentToContactLink, SentCCContactLink, EmailAttachmentLink, EmailCategoryLink
from appmodels.access_control.user import User
from appmodels.access_control.group import Group
from appmodels.access_control.client_roles import ClientRole
from appmodels.access_control.user_links import UserGroupLink, UserClientRoleLink
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            render_as_batch=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
