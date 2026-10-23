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