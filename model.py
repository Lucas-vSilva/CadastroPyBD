import this
from conexao import conexao

class model:
    def __init__(self):
        self.conex = conexao()
        self.conex.conectar()
    def inserir(self,nome, telefone, endereco, dataDeNascimento):
        try:
            sql="Insert into person(cod, nome, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.conex.execute(sql)
            self.conex.commit()
        return "{} Inserido!".format(self.conex.rowcount)
    except Exception as erro:
        return erro

    def consultar(self, cod):
        try:
            sql = "select * from person where cod" = '{}'".format(cod)
            self.conex.execute(sql)


            for(cod, nome, telefone, endereco, dataDeNascimento) in self.conex:
                msg = msg + "\nCódigo: {},\nNome: {},\nTelefone: {},\nEndereço: {},\nData: {}".format(cod, nome, telefone, endereco, dataDeNascimento)
        return msg
    except Exception as erro:
        return erro