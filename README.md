# Sistema de Ordenação de Atendimento
Este script organiza a ordem de atendimento de pessoas com base em suas características: status de urgência, idade e prioridade.

Descrição
O sistema recebe uma lista de pessoas com nome, idade e status (urgente ou normal) e retorna a ordem de atendimento seguindo as regras:

Pessoas com status urgente têm prioridade máxima e são ordenadas por idade decrescente.

Pessoas com idade maior ou igual a 60 anos (idosos) têm prioridade após os urgentes.

As demais pessoas são atendidas por último, na ordem em que foram inseridas.