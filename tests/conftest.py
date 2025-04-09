import pytest
import sqlite3
import os

from models.Users.Employee import Employee
from models.Repositories.RepositoryFacade import RepositoryFacade


@pytest.fixture
def mock_user():
    return Employee(0, 'John', 'Doe', 25)


@pytest.fixture
def setup_database():
    test_db = 'test_database.db'
    if os.path.exists(test_db):
        os.remove(test_db)
    
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INT,
            role TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DaysOff (
            employee_id INT,
            day DATE,
            status TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    
    yield test_db
    
    # Cleanup
    if os.path.exists(test_db):
        os.remove(test_db)

@pytest.fixture
def mock_repository_facade(setup_database):
    return RepositoryFacade(db_name=setup_database)