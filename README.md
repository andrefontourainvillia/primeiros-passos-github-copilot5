# Sistema de Gerenciamento de Atividades Escolares - Mergington High School

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

## Sobre o Projeto

Este é um sistema de gerenciamento de atividades extracurriculares para a Escola Mergington, desenvolvido com FastAPI e MongoDB. O sistema permite que estudantes visualizem e se inscrevam em diversas atividades extracurriculares da escola.

## Funcionalidades

- Listagem de todas as atividades extracurriculares disponíveis
- Inscrição de estudantes em atividades
- Cancelamento de inscrição em atividades

## Tecnologias Utilizadas

- FastAPI: Framework web para APIs
- MongoDB: Banco de dados NoSQL
- Pytest: Framework de testes
- Mongomock: Mock de MongoDB para testes

## Estrutura do Projeto

- `src/`: Código fonte da aplicação
  - `app.py`: API principal
  - `static/`: Arquivos estáticos para a interface web
- `tests/`: Testes automatizados
  - `test_app.py`: Testes dos endpoints da API
  - `test_functions.py`: Testes de funções específicas
  - `test_integration.py`: Testes de fluxos completos

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Inicie o MongoDB (se não estiver usando um serviço externo)

3. Execute a aplicação:
   ```bash
   uvicorn src.app:app --reload
   ```

## Testes

Execute os testes com o comando:

```bash
pytest -v
```

Para mais detalhes sobre os testes, consulte o [README da pasta de testes](./tests/README.md).

## Exercício Original

[![](https://img.shields.io/badge/Ir%20para%20o%20Exerc%C3%ADcio-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/andrefontourainvillia/primeiros-passos-github-copilot5/issues/1)

---

&copy; 2025 GitHub &bull; [Código de Conduta](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [Licença MIT](https://gh.io/mit)

