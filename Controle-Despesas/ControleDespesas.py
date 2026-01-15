import sqlite3
from datetime import datetime

# -------------------------
# Controle de Despesas
# -------------------------

# Conectar ou criar o banco
conn = sqlite3.connect("despesas.db")
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS despesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    categoria TEXT,
    data TEXT
)
""")
conn.commit()

def adicionar_despesa():
    descricao = input("Descrição: ")
    valor = float(input("Valor (R$): "))
    categoria = input("Categoria (Ex: Alimentação, Transporte, Lazer...): ")
    data = datetime.now().strftime("%d/%m/%Y")
    
    cursor.execute("INSERT INTO despesas (descricao, valor, categoria, data) VALUES (?, ?, ?, ?)",
                   (descricao, valor, categoria, data))
    conn.commit()
    print("✅ Despesa adicionada!\n")

def listar_despesas():
    cursor.execute("SELECT * FROM despesas")
    despesas = cursor.fetchall()
    
    if not despesas:
        print("⚠️ Nenhuma despesa registrada.\n")
        return
    
    total = 0
    for d in despesas:
        print(f"ID: {d[0]} | {d[1]} - R${d[2]:.2f} | Categoria: {d[3]} | Data: {d[4]}")
        total += d[2]
    print(f"\n💰 Total gasto: R${total:.2f}\n")

def filtrar_por_categoria():
    categoria = input("Digite a categoria para filtrar: ")
    cursor.execute("SELECT * FROM despesas WHERE categoria=?", (categoria,))
    despesas = cursor.fetchall()
    
    if not despesas:
        print("⚠️ Nenhuma despesa nessa categoria.\n")
        return
    
    total = sum(d[2] for d in despesas)
    for d in despesas:
        print(f"ID: {d[0]} | {d[1]} - R${d[2]:.2f} | Data: {d[4]}")
    print(f"\n💸 Total em {categoria}: R${total:.2f}\n")

def excluir_despesa():
    listar_despesas()
    id_despesa = input("Digite o ID da despesa a excluir: ")
    cursor.execute("DELETE FROM despesas WHERE id=?", (id_despesa,))
    conn.commit()
    print("🗑️ Despesa excluída!\n")

def menu():
    while True:
        print("📊 Controle de Despesas")
        print("1 - Adicionar Despesa")
        print("2 - Listar Despesas")
        print("3 - Filtrar por Categoria")
        print("4 - Excluir Despesa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_despesa()
        elif opcao == "2":
            listar_despesas()
        elif opcao == "3":
            filtrar_por_categoria()
        elif opcao == "4":
            excluir_despesa()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
    conn.close()
