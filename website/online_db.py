import asyncio
import sqlite3
import time
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


async def initialiser_db():
    conn = sqlite3.connect('../evenements.db')
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


async def display_db():
    cur, conn = await initialiser_db()
    cur.execute('SELECT * FROM evenements')
    evenements = cur.fetchall()
    return evenements


async def enregistrer_evenement(cur, conn, auteur, id, date, roles, name):
    cur.execute('''
        INSERT INTO evenements (id, name, date, auteur, roles)
        VALUES (?, ?, ?, ?, ?)
    ''', (id, name, date, auteur, roles))
    conn.commit()


async def supprimer_evenement(cur, conn, id):
    cur.execute("DELETE FROM evenements WHERE id = ?", (id,))
    conn.commit()


@app.route('/post_event', methods=['POST'])
def post_event():
    name = request.form.get('name')
    date = request.form.get('date')
    roles = request.form.get('roles')

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    cur, conn = loop.run_until_complete(initialiser_db())
    loop.run_until_complete(enregistrer_evenement(cur, conn, 'web_user', int(time.time()), date, roles, name))

    return 'Event ajouté avec succées à la base de données !'


@app.route('/delete_event', methods=['POST'])
def delete_event():
    id = request.form.get('id')

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    cur, conn = loop.run_until_complete(initialiser_db())
    loop.run_until_complete(supprimer_evenement(cur, conn, id))

    return 'Event supprimé avec succées de la base de données !'


@app.route('/get_events', methods=['GET'])
def get_events():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    cur, conn = loop.run_until_complete(initialiser_db())
    evenements = loop.run_until_complete(display_db())
    return json.dumps(evenements)


if __name__ == '__main__':
    app.run(debug=True, port=63342)