# ------ Atlanta Bot ------
#  By : helias5605
# -------------------------

import sqlite3
import time
from main import *
import os
import json


async def initialiser_db():
    conn = sqlite3.connect('../evenements.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS evenements (
            id INTEGER PRIMARY KEY,
            name TEXT,
            date TEXT,
            auteur TEXT,
            roles TEXT,
            user_reservations TEXT
        )
    ''')
    conn.commit()
    return cur, conn


async def enregistrer_evenement(cur, conn, auteur, id, date, roles, name, user_reservations):
    cur.execute('''
        INSERT INTO evenements (id, name, date, auteur, roles, user_reservations)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (id, name, date, auteur, roles, user_reservations))
    conn.commit()


async def supprimer_evenement(cur, conn, id):
    cur.execute('''
        DELETE FROM evenements WHERE ID = ?
    ''', (id,))
    conn.commit()


async def update_event(id, new_value):
    cur, conn = await initialiser_db()
    cur.execute("UPDATE events SET column_name = ? WHERE id = ?", (new_value, id))
    conn.commit()
    conn.close()


async def display_db():
    cur, conn = await initialiser_db()
    cur.execute('SELECT * FROM evenements')
    evenements = cur.fetchall()
    return evenements


async def purge_events(cur, conn):
    cur.execute("DELETE FROM evenements")
    conn.commit()