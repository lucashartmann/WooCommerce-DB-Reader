import mysql.connector


class MySQL_Banco:

    dados = {
        "host": "",
        "user": "",
        "password": "",
        "database": ""
    }

    def criar_tabela(self, sql):
        try:
            with mysql.connector.connect(host=self.dados["host"], user=self.dados["user"], password=self.dados["password"], database=self.dados["database"]) as conexao:
                cursor = conexao.cursor()
                cursor.execute(sql)
                return True, ""
        except Exception as e:
            return False, e

    def cadastrar_item(self):
        try:
            with mysql.connector.connect(host=self.dados["host"], user=self.dados["user"], password=self.dados["password"], database=self.dados["database"]) as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    f'INSERT INTO ? (?) VALUES (?)', ())
                return True, ""
        except Exception as e:
            return False, e

    def atualizar_item(self):
        try:
            with mysql.connector.connect(host=self.dados["host"], user=self.dados["user"], password=self.dados["password"], database=self.dados["database"]) as conexao:
                cursor = conexao.cursor()
                return True, ""
        except Exception as e:
            return False, e

    def remover_item(self, tabela, id):
        try:
            with mysql.connector.connect(host=self.dados["host"], user=self.dados["user"], password=self.dados["password"], database=self.dados["database"]) as conexao:
                cursor = conexao.cursor()
                sql_delete_query = f"""
                    DELETE FROM {tabela}
                    WHERE ? = ?;
                    """
                cursor.execute(sql_delete_query, (id,))
                return True, ""
        except Exception as e:
            return False, e

    def consultar_item(self, tabela, id):
        try:
            with mysql.connector.connect(host=self.dados["host"], user=self.dados["user"], password=self.dados["password"], database=self.dados["database"]) as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    f'SELECT * FROM {tabela} WHERE ? = ?', (id,))
                registro = cursor.fetchone()
                return registro, ""
        except Exception as e:
            return False, e

    def listar_itens(self, tabela):
        try:
            with mysql.connector.connect(host=self.dados["host"], user=self.dados["user"], password=self.dados["password"], database=self.dados["database"]) as conexao:
                cursor = conexao.cursor()
                cursor.execute(f"SELECT * FROM {tabela}")
                resultados = cursor.fetchall()
                return resultados, ""

        except Exception as e:
            return [], e
