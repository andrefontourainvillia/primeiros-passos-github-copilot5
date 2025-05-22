"""
Testes para os endpoints da API da aplicação de gerenciamento de atividades escolares
"""
import pytest
from fastapi import HTTPException

def test_get_activities(test_client):
    """Testa se o endpoint GET /activities retorna as atividades corretamente"""
    response = test_client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    
    # Verifica se os dados correspondem ao esperado
    assert "Clube de Xadrez" in data
    assert "Aula de Programação" in data
    assert data["Clube de Xadrez"]["description"] == "Aprenda estratégias e participe de torneios de xadrez"
    assert len(data["Clube de Xadrez"]["participants"]) == 2

def test_signup_for_activity_success(test_client):
    """Testa inscrição bem-sucedida em uma atividade"""
    email = "novo.aluno@mergington.edu"
    activity = "Clube de Xadrez"
    
    response = test_client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert response.json() == {"message": f"{email} inscrito(a) em {activity} com sucesso"}
    
    # Verifica se o aluno foi realmente adicionado
    activities = test_client.get("/activities").json()
    assert email in activities["Clube de Xadrez"]["participants"]

def test_signup_for_activity_already_enrolled(test_client):
    """Testa inscrição em uma atividade quando o aluno já está inscrito"""
    email = "michael@mergington.edu"  # aluno que já está inscrito
    activity = "Clube de Xadrez"
    
    response = test_client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 400
    assert "Estudante já inscrito nesta atividade" in response.text

def test_signup_for_nonexistent_activity(test_client):
    """Testa inscrição em uma atividade que não existe"""
    email = "aluno@mergington.edu"
    activity = "Atividade Inexistente"
    
    response = test_client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 404
    assert "Atividade não encontrada" in response.text

def test_remove_participant_success(test_client):
    """Testa remoção bem-sucedida de um participante"""
    email = "michael@mergington.edu"
    activity = "Clube de Xadrez"
    
    response = test_client.post(f"/activities/{activity}/remove?email={email}")
    assert response.status_code == 200
    assert response.json() == {"message": f"{email} removido(a) de {activity} com sucesso"}
    
    # Verifica se o aluno foi realmente removido
    activities = test_client.get("/activities").json()
    assert email not in activities["Clube de Xadrez"]["participants"]

def test_remove_participant_not_enrolled(test_client):
    """Testa remoção de um participante não inscrito"""
    email = "nao.inscrito@mergington.edu"
    activity = "Clube de Xadrez"
    
    response = test_client.post(f"/activities/{activity}/remove?email={email}")
    assert response.status_code == 400
    assert "Participante não está inscrito nesta atividade" in response.text

def test_remove_from_nonexistent_activity(test_client):
    """Testa remoção de uma atividade que não existe"""
    email = "aluno@mergington.edu"
    activity = "Atividade Inexistente"
    
    response = test_client.post(f"/activities/{activity}/remove?email={email}")
    assert response.status_code == 404
    assert "Atividade não encontrada" in response.text

def test_root_redirect(test_client):
    """Testa se o endpoint raiz redireciona para a página estática"""
    response = test_client.get("/", follow_redirects=False)
    assert response.status_code == 307  # Redirecionamento temporário
    assert response.headers["location"] == "/static/index.html"
