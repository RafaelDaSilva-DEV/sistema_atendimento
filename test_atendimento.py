import pytest
from atendimento import ordem_atendimento

def test_ordem_basica():
    entrada = [
        ("João", "70", "normal"),
        ("Maria", "30", "urgente"),
        ("Ana", "25", "normal"),
        ("Carlos", "65", "normal"),
        ("Paulo", "40", "urgente")
    ]
    resultado = ordem_atendimento(entrada)
    
    assert resultado == ["Paulo", "Maria", "João", "Carlos", "Ana"]

def test_somente_urgentes():
    entrada = [
        ("Lucas", "50", "urgente"),
        ("Pedro", "55", "urgente"),
        ("Felipe", "20", "urgente"),
    ]
    resultado = ordem_atendimento(entrada)
    
    assert resultado == ["Pedro", "Lucas", "Felipe"]

def test_somente_idosos():
    entrada = [
        ("Dona Lúcia", "75", "normal"),
        ("Seu José", "80", "normal"),
        ("Vó Maria", "90", "normal"),
    ]
    resultado = ordem_atendimento(entrada)
    assert resultado == ["Dona Lúcia", "Seu José", "Vó Maria"]

def test_somente_demais():
    entrada = [
        ("João", "20", "normal"),
        ("Ana", "25", "normal"),
        ("Pedro", "30", "normal"),
    ]
    resultado = ordem_atendimento(entrada)
    assert resultado == ["João", "Ana", "Pedro"]

def test_urgente_e_idoso():
    entrada = [
        ("Maria", "65", "urgente"),
        ("João", "70", "normal"),
        ("Ana", "20", "normal"),
    ]
    resultado = ordem_atendimento(entrada)
   
    assert resultado == ["Maria", "João", "Ana"]
    