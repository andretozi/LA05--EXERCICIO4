from lista_livros import biblioteca

def filto_livros(criterios):

    return [livro for livro in biblioteca if all(livro.get(chave) == valor for chave, valor in criterios.items())]