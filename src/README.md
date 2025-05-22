# API de Atividades da Escola Mergington High

Uma aplicação FastAPI super simples que permite aos estudantes visualizar e se inscrever em atividades extracurriculares.

## Funcionalidades

- Visualizar todas as atividades extracurriculares disponíveis
- Inscrever-se em atividades

## Começando

1. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

2. Configure o MongoDB:
   
   ```
   # Certifique-se de que o MongoDB está instalado e em execução
   # Por padrão, a aplicação se conecta em: mongodb://localhost:27017/
   ```

3. Execute a aplicação:

   ```
   python app.py
   ```

3. Abra seu navegador e acesse:
   - Documentação da API: http://localhost:8000/docs
   - Documentação alternativa: http://localhost:8000/redoc

## Endpoints da API

| Método | Endpoint                                                          | Descrição                                                           |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Obter todas as atividades com seus detalhes e contagem atual de participantes |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Inscrever-se em uma atividade                                        |
| POST   | `/activities/{activity_name}/remove?email=student@mergington.edu` | Remover a inscrição de um estudante em uma atividade                 |

## Modelo de Dados

A aplicação utiliza um modelo de dados simples com identificadores significativos:

1. **Atividades** - Usa o nome da atividade como identificador:

   - Descrição
   - Programação
   - Número máximo de participantes permitidos
   - Lista de emails dos estudantes inscritos

2. **Estudantes** - Usa o email como identificador:
   - Nome
   - Nível escolar

Os dados são armazenados no MongoDB, o que garante a persistência mesmo após o servidor ser reiniciado.
