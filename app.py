import random
import sqlite3 as sq
from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = "6767 aura tipo não choraxxx udfgcyuawgf87sgdf7gagbha97gwe8bgvuaw7efh8uashgf97awge87gfiyg86gf67age8fg87gfa67gfbhfuysdgv7tfduawefby8fadg7afdsgafeuih87adsftg6etfg67aewgfawe"

DB_PATH = "nomes"


def gerar_nomes():
  conect = sq.connect(DB_PATH)
  cursor = conect.cursor()

  cursor.execute("SELECT nome FROM nomes")
  nomes = cursor.fetchall()

  cursor.execute("SELECT complemento FROM complementos")
  complementos = cursor.fetchall()

  cursor.execute("SELECT sobrenome FROM sobrenomes")
  sobrenomes = cursor.fetchall()

  conect.close()

  if not nomes or not complementos or not sobrenomes:
    return ""

  r1 = random.choice(nomes)[0]
  r2 = random.choice(complementos)[0]
  r3 = random.choice(sobrenomes)[0]

  return f"{r1} {r3} {r2}"


@app.route("/", methods=["GET"])
def home():
  nome_atual = session.pop("nome_gerado", "")
  return render_template("index.html", texto=nome_atual)


@app.route("/gerar", methods=["POST"])
def gerar():
  session["nome_gerado"] = gerar_nomes()
  return redirect("/")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)