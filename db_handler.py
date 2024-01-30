# ------ Atlanta Bot ------
#  By : helias5605
# -------------------------

import sqlite3
import time
from main import *
import os
import json


def initialiser_db():
    conn = sqlite3.connect('evenements.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS evenements (
            id INTEGER PRIMARY KEY,
            name TEXT,
            date TEXT,
            auteur TEXT,
            roles TEXT
        )
    ''')
    conn.commit()
    return cur, conn


def enregistrer_evenement(cur, conn, auteur, id, date, roles, name):
    cur.execute('''
        INSERT INTO evenements (id, name, date, auteur, roles)
        VALUES (?, ?, ?, ?, ?)
    ''', (id, name, date, auteur, roles))
    conn.commit()


def supprimer_evenement(cur, conn, id):
    cur.execute('''
        DELETE FROM evenements WHERE ID = ?
    ''', (id,))
    conn.commit()


def display_db():
    cur, conn = initialiser_db()
    cur.execute('SELECT * FROM evenements')
    evenements = cur.fetchall()
    return evenements


def purge_events(cur, conn):
    cur.execute("DELETE FROM evenements")
    conn.commit()