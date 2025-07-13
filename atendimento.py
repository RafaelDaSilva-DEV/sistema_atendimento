def ordem_atendimento(lista_pessoas):
    urgentes = []
    idosos = []
    demais = []

    for pessoa in lista_pessoas:
        nome, idade, status = pessoa
        idade = int(idade)

        if status == "urgente":
            urgentes.append((nome, idade))
        elif idade >= 60:
            idosos.append(nome)
        else:
            demais.append(nome)

    urgentes.sort(key=lambda x: x[1], reverse=True)
    urgentes_nomes = [nome for nome, idade in urgentes]
    ordem_final = urgentes_nomes + idosos + demais

    return ordem_final