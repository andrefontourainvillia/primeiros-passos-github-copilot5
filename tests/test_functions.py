"""
Testes para funções específicas e comportamentos detalhados da aplicação
"""
import pytest
from fastapi import HTTPException
import mongomock
import sys
import os

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_activity_max_participants(mock_mongodb):
    """Teste para verificar limite máximo de participantes (não implementado na API atual)"""
    # Esse teste é para demonstrar como testar uma funcionalidade que ainda seria implementada
    
    # Importar aqui para garantir que o mock já está ativo
    from src.app import activities_collection
    
    # Cria uma atividade com capacidade máxima
    activities_collection.insert_one({
        "_id": "Atividade Limitada",
        "description": "Atividade com limite de participantes",
        "schedule": "Terças, 14h - 15h",
        "max_participants": 2,
        "participants": ["aluno1@mergington.edu", "aluno2@mergington.edu"]
    })
    
    # Verifica se a atividade foi criada corretamente
    activity = activities_collection.find_one({"_id": "Atividade Limitada"})
    assert activity is not None
    assert len(activity["participants"]) == 2
    assert activity["max_participants"] == 2
    
    # Em um sistema completo, tentaríamos adicionar um terceiro aluno e esperaríamos uma exceção
    # Como essa funcionalidade não está implementada ainda, o teste termina aqui
    # Em um cenário real, adicionaríamos algo como:
    # with pytest.raises(HTTPException) as excinfo:
    #     # Chamar função que adiciona aluno quando já atingiu o limite
    # assert "Limite de participantes atingido" in str(excinfo.value)

def test_mongodb_operations(mock_mongodb):
    """Testa operações básicas no MongoDB"""
    # Importar aqui para garantir que o mock já está ativo
    from src.app import activities_collection
    
    # Inserir uma nova atividade
    new_activity = {
        "_id": "Nova Atividade",
        "description": "Descrição da nova atividade",
        "schedule": "Segunda, 10h - 11h",
        "max_participants": 15,
        "participants": []
    }
    
    activities_collection.insert_one(new_activity)
    
    # Verificar se foi inserido corretamente
    activity = activities_collection.find_one({"_id": "Nova Atividade"})
    assert activity is not None
    assert activity["description"] == "Descrição da nova atividade"
    
    # Atualizar a atividade
    activities_collection.update_one(
        {"_id": "Nova Atividade"},
        {"$set": {"description": "Descrição atualizada"}}
    )
    
    # Verificar a atualização
    updated_activity = activities_collection.find_one({"_id": "Nova Atividade"})
    assert updated_activity["description"] == "Descrição atualizada"
    
    # Deletar a atividade
    activities_collection.delete_one({"_id": "Nova Atividade"})
    
    # Verificar se foi deletado
    deleted_activity = activities_collection.find_one({"_id": "Nova Atividade"})
    assert deleted_activity is None
