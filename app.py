from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

utenti = [
    {'id': 1, 'nome': 'Elisabetta', 'eta': 130},
    {'id': 2, 'nome': 'Barbanera', 'eta': 50}
]
@app.route('/api/utenti')
def lista_utenti():
    return jsonify([{'id': u['id'], 'nome': u['nome']} for u in utenti])

@app.route('/api/utenti/<id>')
def dettaglio_utente(id):
    lista = [ u for u in utenti if u['id'] == int(id)]
    if len(lista) == 1:
        return jsonify(lista[0])
    else:
        return jsonify([])

@app.route('/api/utenti', methods = ['POST'])
def aggiungi_utente():
    if request.headers['Content-Type'] == 'application/json':
        utente = request.json
        newId = max([u['id'] for u in utenti]) + 1
        utenti.append( {
            'id': newId,
            'nome': utente['nome'],
            'eta': utente['eta']
        }
        )
    return  jsonify(newId)

@app.route('/api/utenti/<id>', methods = ['PUT'])
def modifica_utente(id):
    pass ## TODO

@app.route('/api/utenti/<id>', methods = ['DELETE'])
def cancella_utente(id):
    utenti[:] = [u for u in utenti if u['id']!= int(id)]
    return 'Utente cancellato con successo'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    n_studenti = 13
    return render_template('about.html', studenti = n_studenti)

if __name__ == '__main__':
    app.run()
