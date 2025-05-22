"""
Configurações e fixtures para testes
"""
import pytest
from fastapi.testclient import TestClient
import mongomock
import sys
import os
from pathlib import Path

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock do MongoDB
@pytest.fixture
def mock_mongodb(monkeypatch):
    """Mock do cliente MongoDB"""
    # Cria um cliente MongoDB mock
    mock_client = mongomock.MongoClient()
    mock_db = mock_client['high_school_db']
    mock_activities = mock_db['activities']
    
    # Primeiro monkeypatch o client para evitar a conexão real com MongoDB
    monkeypatch.setattr("pymongo.MongoClient", lambda *args, **kwargs: mock_client)
    
    # Agora importa o módulo quando o patch já está ativo
    from src.app import client, db, activities_collection
    
    # Substitui o cliente e coleção reais pelos mocks
    monkeypatch.setattr("src.app.client", mock_client)
    monkeypatch.setattr("src.app.db", mock_db)
    monkeypatch.setattr("src.app.activities_collection", mock_activities)
    
    # Insere dados iniciais de teste
    initial_activities = {
        "Clube de Xadrez": {
            "description": "Aprenda estratégias e participe de torneios de xadrez",
            "schedule": "Sextas, 15h30 - 17h",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Aula de Programação": {
            "description": "Aprenda fundamentos de programação e desenvolva projetos de software",
            "schedule": "Terças e quintas, 15h30 - 16h30",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        }
    }
    
    for activity_name, activity_data in initial_activities.items():
        mock_activities.insert_one({
            "_id": activity_name,
            **activity_data
        })
    
    return mock_client

@pytest.fixture
def test_client(mock_mongodb):
    """Cria um cliente de teste para a aplicação FastAPI"""
    from src.app import app
    client = TestClient(app)
    return client
