# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='python', password='Python1!',
                              host='127.0.0.1',
                              database='pedidos')

print("PedidosClient")

query = "SELECT * FROM WorkList"
cursor = cnx.cursor()
cursor.execute(query)
results = cursor.fetchall()
pass
for (idWorkList, editTime, Pedido_idPedido, Estado, data, Obervacoes, Doente_idDoente, idEpisodio, Relatorio) in cursor:
    cursor2 = cnx.cursor()
    queryPatient = ("SELECT * FROM Doente WHERE idDoente =" + Doente_idDoente)
    cursor2.execute(query)
    patient = cursor2.fetchone()
    pass
