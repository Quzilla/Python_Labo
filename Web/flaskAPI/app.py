from flask import Flask, request, g
import sqlite3
import json

dbpath = 'test.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(dbpath)
        db.execute('CREATE TABLE IF NOT EXISTS tweets_tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, tweet VARCHAR(140))')
    return db

@app.route('/tweet', methods=['GET'])
def get_tweet():
    con = get_db()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute('SELECT * FROM tweets_tbl')
    tweets = []
    for row in cur.fetchall():
        tweets.append(dict(row))
        
    return json.dumps(tweets, indent=2)

@app.route("/tweet", methods=['POST'])
def post_tweet():
    con = get_db()
    cur = con.cursor()
    
    tweet = request.json["tweet"]
    cur.execute(f"INSERT INTO tweets_tbl(tweet) values('{tweet}')")
    con.commit()
    
    return 'Success a Tweet!\n'

@app.route('/tweet/<id>', methods=['PUT'])
def put_tweet(id):
    con = get_db()
    cur = con.cursor()
    
    tweet = request.json['tweet']
    cur.execute(f"UPDATE tweets_tbl SET tweet = '{tweet}' WHERE id = {id}")
    con.commit()
    
    return 'Update a Tweet!\n'

@app.route('/tweet/<id>', methods=['DELETE'])
def delete_tweet(id):
    con = get_db()
    cur = con.cursor()
    cur.execute(f"DELETE FROM tweets_tbl WHERE id = {id}")
    con.commit()
    
    return 'Delete a Tweet!\n'


if __name__ == "__main__":
    app.run(debug=True)