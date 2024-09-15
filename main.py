from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)

jogo1 = Jogo("Tetris", "Puzzle", "Atatri")
jogo2 = Jogo("Battlebit", "FPS", "PC")
jogo3 = Jogo("Crash BomDeCoito", "Coito", "PS1")
jogo4 = Jogo("Mortal kombat", "Luta", "PS2")
jogosList = [jogo1, jogo2, jogo3, jogo4]


@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=jogosList)


@app.route("/newgame")
def newGame():
    return render_template("newGame.html", titulo="Novo Jogo")


@app.route(
    "/criar",
    methods=[
        "POST",
    ],
)
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]

    jogo = Jogo(nome=nome, categoria=categoria, console=console)
    jogosList.append(jogo)

    return redirect('/')


app.run(port=8080, debug=True)
