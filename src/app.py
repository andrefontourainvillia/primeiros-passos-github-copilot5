"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path
from pymongo import MongoClient
from typing import Dict, List, Any

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['high_school_db']
activities_collection = db['activities']

# Initial activities data
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
   },
   "Educação Física": {
      "description": "Educação física e atividades esportivas",
      "schedule": "Segundas, quartas e sextas, 14h - 15h",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   },
   # Esportivas
   "Futebol": {
      "description": "Treinos e partidas de futebol para todos os níveis",
      "schedule": "Terças e quintas, 16h - 17h30",
      "max_participants": 22,
      "participants": ["lucas@mergington.edu", "marcos@mergington.edu"]
   },
   "Vôlei": {
      "description": "Aulas e jogos de vôlei para iniciantes e avançados",
      "schedule": "Quartas e sextas, 15h - 16h30",
      "max_participants": 14,
      "participants": ["ana@mergington.edu", "carla@mergington.edu"]
   },
   # Artísticas
   "Teatro": {
      "description": "Expressão corporal, atuação e montagem de peças teatrais",
      "schedule": "Segundas e quartas, 16h - 17h30",
      "max_participants": 18,
      "participants": ["bruno@mergington.edu", "lara@mergington.edu"]
   },
   "Oficina de Pintura": {
      "description": "Técnicas de pintura em tela e criatividade artística",
      "schedule": "Sábados, 10h - 12h",
      "max_participants": 15,
      "participants": ["juliana@mergington.edu", "rafael@mergington.edu"]
   },
   # Intelectuais
   "Clube de Leitura": {
      "description": "Leitura e discussão de livros clássicos e contemporâneos",
      "schedule": "Quartas, 17h - 18h",
      "max_participants": 16,
      "participants": ["camila@mergington.edu", "pedro@mergington.edu"]
   },
   "Olimpíada de Matemática": {
      "description": "Preparação para olimpíadas e desafios matemáticos",
      "schedule": "Sextas, 14h - 15h30",
      "max_participants": 25,
      "participants": ["fernanda@mergington.edu", "gustavo@mergington.edu"]
   }
}


@app.on_event("startup")
def startup_db_client():
    """Initialize the database on startup if it's empty"""
    # Check if the activities collection is empty
    if activities_collection.count_documents({}) == 0:
        # Insert the initial activities data
        for activity_name, activity_data in initial_activities.items():
            activities_collection.insert_one({
                "_id": activity_name,
                **activity_data
            })
        print("Initialized MongoDB with sample activities")


@app.on_event("shutdown")
def shutdown_db_client():
    """Close the MongoDB connection on shutdown"""
    client.close()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    """Get all activities from MongoDB"""
    result = {}
    for doc in activities_collection.find():
        activity_name = doc.pop('_id')
        result[activity_name] = doc
    return result


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    activity = activities_collection.find_one({"_id": activity_name})
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")

    # Validar se o estudante já está inscrito
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Estudante já inscrito nesta atividade")
    
    # Add student
    activities_collection.update_one(
        {"_id": activity_name},
        {"$push": {"participants": email}}
    )
    return {"message": f"{email} inscrito(a) em {activity_name} com sucesso"}


@app.post("/activities/{activity_name}/remove")
def remove_participant(activity_name: str, email: str):
    """Remove a student from an activity"""
    # Validate activity exists
    activity = activities_collection.find_one({"_id": activity_name})
    if not activity:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    
    # Validate student is enrolled
    if email not in activity["participants"]:
        raise HTTPException(status_code=400, detail="Participante não está inscrito nesta atividade")
    
    # Remove student
    activities_collection.update_one(
        {"_id": activity_name},
        {"$pull": {"participants": email}}
    )
    return {"message": f"{email} removido(a) de {activity_name} com sucesso"}
