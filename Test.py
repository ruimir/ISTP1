# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='python', password='Python1!',
                              host='127.0.0.1',
                              database='pedidos')

print("PedidosApp")


def registarpedido():
    print("Numero de Paciente:")
    paciente = int(input())
    query = ("SELECT * from Doente "
             "WHERE idDoente = " + str(paciente))
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    if result is None:
        print("Doente not found")
        quit(1)
    print("Doente Identifiado:" + str(result[2]))
    print("Episodio")
    episodio = int(input())
    print("Observacoes:")
    orbservacoes = raw_input()
    print("Relatorio:")
    relatorio = raw_input()
    hoje = datetime.now().date()
    inserir = ("INSERT INTO Pedido "
               "(idPedido, Estado, data, Observações, Doente_idDoente, idEpisodio, Relatorio)"
               "VALUES (NULL, %(estado)s, %(data)s, %(obser)s,%(doente)s,%(episodio)s,%(relatorio)s)")
    data = {
        'data': hoje,
        'estado': "Scheduled",
        'obser': orbservacoes,
        'doente': paciente,
        'episodio': episodio,
        'relatorio': relatorio
    }
    cursor.execute(inserir, data)
    cnx.commit()
    cursor.close()
    print ("Registo Concluído")


while True:
    print("1 - Registar Pedido")
    print("2 - Alterar Pedido")
    res = int(input())
    if res == 1:
        registarpedido()
    if res == 2:
        pass
    else:
        print("Erro!")
