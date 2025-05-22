# Testes do Sistema de Gerenciamento de Atividades Escolares

Este diretório contém testes automatizados para o Sistema de Gerenciamento de Atividades Escolares da Escola Mergington.

## Estrutura de Testes

- `test_app.py`: Testes para os endpoints da API
- `test_functions.py`: Testes para funções específicas e comportamentos detalhados
- `test_integration.py`: Testes de fluxo completo do sistema
- `conftest.py`: Configurações e fixtures para os testes
- `run_tests.py`: Script auxiliar para execução dos testes

## Execução dos Testes

Para executar todos os testes, use:

```bash
pytest -v
```

Para executar um conjunto específico de testes:

```bash
pytest -v tests/test_app.py      # Testa apenas endpoints
pytest -v tests/test_functions.py  # Testa apenas funções específicas
pytest -v tests/test_integration.py  # Testa fluxos completos
```

## Cobertura de Testes

Os testes abrangem:

1. **Testes de API**: Testam todos os endpoints da API
   - Consulta de atividades
   - Inscrição de alunos
   - Remoção de alunos
   - Redirecionamento da página raiz

2. **Testes de Funções**: Testam comportamentos específicos do sistema
   - Manipulação do banco de dados
   - Verificação de limites de participantes

3. **Testes de Integração**: Testam fluxos completos
   - Fluxo de uso do estudante
   - Operações administrativas simuladas

## Fixtures de Teste

- `mock_mongodb`: Mock do banco de dados MongoDB
- `test_client`: Cliente de teste para a API FastAPI

## Requisitos de Teste

Os requisitos para executar os testes estão no arquivo `requirements.txt` principal:

- pytest
- httpx
- pytest-mock
- mongomock
