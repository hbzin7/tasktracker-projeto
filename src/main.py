<<<<<<< HEAD
def menu():
    while True:
        print("\n=== TASKTRACKER CLI ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opcao: ")
        
        if opcao == "1":
            tarefa = input("Digite o nome da tarefa: ")
            print(f"-> Tarefa '{tarefa}' adicionada com sucesso!")
        elif opcao == "2":
            print("-> Lista de tarefas: [1. Estudar Docker]")
        elif opcao == "0":
            print("Saindo do TaskTracker...")
            break
        else:
            print("Opcao invalida, tente novamente.")

if __name__ == "__main__":
    menu()
=======
import sys

def validar_titulo() -> str:
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: O título não pode ser vazio ou conter apenas espaços. Tente novamente.\n")

def validar_prioridade() -> str:
    opcoes_validas = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa"
    }
    while True:
        prioridade_input = input("Digite a prioridade (Alta, Média, Baixa): ").strip().lower()
        if prioridade_input in opcoes_validas:
            return opcoes_validas[prioridade_input]
        print("Erro: Prioridade inválida! Escolha entre 'Alta', 'Média' ou 'Baixa'.\n")

def cadastrar_tarefa(tarefas: list):
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    titulo = validar_titulo()
    descricao = input("Digite a descrição da tarefa (opcional): ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não definida",
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")

def listar_tarefas(tarefas: list):
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for idx, t in enumerate(tarefas, start=1):
        print(f"\n[Tarefa #{idx}]")
        print(f"  Título:      {t['titulo']}")
        print(f"  Descrição:   {t['descricao']}")
        print(f"  Prioridade:  {t['prioridade']}")
        print(f"  Data Limite: {t['data_limite']}")
        print(f"  Status:      {t['status']}")
        print("-" * 25)

def main():
    tarefas = []
    while True:
        print("\n==============================")
        print("       TASKTRACKER - CLI      ")
        print("==============================")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando a aplicação TaskTracker. Até logo!")
            sys.exit(0)
        else:
            print("Opção inválida! Escolha uma opção entre 1 e 3.")

if __name__ == "__main__":
    main()
>>>>>>> fb997318e491d2cacae5465aa32216b23239fdcd
