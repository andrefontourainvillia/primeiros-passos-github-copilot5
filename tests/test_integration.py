"""
Testes de integração para verificar o fluxo completo de uso da aplicação
"""
import pytest

def test_complete_student_flow(test_client):
    """Teste do fluxo completo de um estudante interagindo com o sistema"""
    # 1. Consultar atividades disponíveis
    response = test_client.get("/activities")
    assert response.status_code == 200
    activities = response.json()
    assert len(activities) >= 2
    
    # 2. Escolher e se inscrever em uma atividade (Aula de Programação)
    email = "novo.estudante@mergington.edu"
    activity = "Aula de Programação"
    
    response = test_client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert f"{email} inscrito(a) em {activity} com sucesso" in response.text
    
    # 3. Verificar se está na lista de participantes
    response = test_client.get("/activities")
    activities = response.json()
    assert email in activities[activity]["participants"]
    
    # 4. Tentar se inscrever novamente na mesma atividade (deve falhar)
    response = test_client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 400
    assert "Estudante já inscrito nesta atividade" in response.text
    
    # 5. Se inscrever em outra atividade (Clube de Xadrez)
    activity2 = "Clube de Xadrez"
    response = test_client.post(f"/activities/{activity2}/signup?email={email}")
    assert response.status_code == 200
    
    # 6. Verificar inscrição na segunda atividade
    response = test_client.get("/activities")
    activities = response.json()
    assert email in activities[activity2]["participants"]
    
    # 7. Desistir da primeira atividade
    response = test_client.post(f"/activities/{activity}/remove?email={email}")
    assert response.status_code == 200
    
    # 8. Verificar que não está mais na primeira atividade
    response = test_client.get("/activities")
    activities = response.json()
    assert email not in activities[activity]["participants"]
    assert email in activities[activity2]["participants"]

def test_admin_operations_flow(test_client, mock_mongodb):
    """
    Teste simulando operações de um administrador 
    (assumindo que seriam implementadas no futuro)
    """
    # Como a API atual não tem operações administrativas específicas,
    # este teste simula o que poderia ser testado quando essas funções
    # forem implementadas
    
    # 1. Criamos uma nova atividade direto no banco de dados (simulando uma função admin)
    new_activity = {
        "_id": "Oficina de Robótica",
        "description": "Aprenda a montar e programar robôs",
        "schedule": "Quintas, 15h - 17h",
        "max_participants": 15,
        "participants": []
    }
    from src.app import activities_collection
    activities_collection.insert_one(new_activity)
    
    # 2. Verificar se a atividade foi criada
    response = test_client.get("/activities")
    activities = response.json()
    assert "Oficina de Robótica" in activities
    
    # 3. Inscrever um aluno
    email = "estudante.robotica@mergington.edu"
    response = test_client.post(f"/activities/Oficina de Robótica/signup?email={email}")
    assert response.status_code == 200
    
    # 4. Verificar a inscrição
    response = test_client.get("/activities")
    activities = response.json()
    assert email in activities["Oficina de Robótica"]["participants"]
