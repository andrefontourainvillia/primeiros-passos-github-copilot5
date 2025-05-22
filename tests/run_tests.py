"""
Script para facilitar a execução dos testes
"""
import pytest
import os
import sys

if __name__ == "__main__":
    # Adiciona o diretório atual ao path do sistema
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Executa os testes
    pytest.main(["-v"])
