from flask import Flask, render_template, request
from lista_livros import biblioteca

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    livros_para_mostrar = biblioteca
    termo_pesquisado = ""

    if request.method == "POST":
        termo_pesquisado = request.form.get("termo_busca", "").lower().strip()

        if termo_pesquisado:
            livros_para_mostrar = []
            for livro in biblioteca:
                if (termo_pesquisado in livro["titulo"].lower() or
                        termo_pesquisado in livro["autor"].lower() or
                        termo_pesquisado in livro["categoria"].lower() or
                        termo_pesquisado in str(livro["ano"])):
                    livros_para_mostrar.append(livro)

    return render_template("index.html", livros=livros_para_mostrar, termo_pesquisado=termo_pesquisado)


if __name__ == "__main__":
    app.run(debug=True)