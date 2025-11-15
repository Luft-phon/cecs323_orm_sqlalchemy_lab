from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from configparser import ConfigParser

# read database configuration from config.ini
config = ConfigParser()
config.read('config.ini')
userID: str = config['credentials']['userid']
password: str = config['credentials']['password']
host: str = config['credentials']['host']
port: str = config['credentials']['port']
database: str = config['credentials']['database']

db_url: str = f"postgresql+psycopg2://{userID}:{password}@{host}:{port}/{database}"
db_url_display: str = f"postgresql+psycopg2://{userID}:********@{host}:{port}/{database}"
print("DB URL: " + db_url_display)
engine = create_engine(db_url, pool_size=5, pool_recycle=3600, echo=False)

session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)

def setup_database(create_tables: bool = False):
    """Return a new scoped session bound to the engine.

    If `create_tables` is True, import the declarative Base and create
    any tables that are defined by the models. Importing Base inside
    the function avoids circular imports at module load time.
    """
    if create_tables:
        try:
            from base import Base

            Base.metadata.create_all(engine)
        except Exception as e:
            print("Warning: failed to create tables:", e)

    return Session()


def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("Connected successfully!")
            print("PostgreSQL version:", result.scalar())
            print(config['credentials']['database'])
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    test_connection()