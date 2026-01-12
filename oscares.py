"""
SISTEMA DE GESTÃO DOS ÓSCARES - MELHOR FILME
Trabalho Prático de Fundamentos de Programação
Licenciatura em Engenharia Informática - ISLA Gaia

Autor: CARLOS RASGADO
Data: Janeiro 2026
"""

import csv
import os
import random

# ============================================================
# VARIÁVEIS GLOBAIS
# ============================================================

lista_filmes = []
lista_pontuacoes = []
FICHEIRO_CSV = "oscares_dados.csv"

# ============================================================
# FUNÇÕES DE INTERFACE
# ============================================================

def limpar_ecra():
    """Limpa o ecrã da consola."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """Pausa a execução até o utilizador pressionar ENTER."""
    input("\nPressione ENTER para continuar...")


def mostrar_cabecalho(titulo: str):
    """
    Apresenta um cabeçalho formatado.

    Parâmetros:
        titulo (str): Título a apresentar
    """
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60)

# ============================================================
# FUNÇÕES DE VALIDAÇÃO
# ============================================================

def validar_pontuacao(pontuacao: float) -> bool:
    """
    Valida se a pontuação está no intervalo [0, 20].

    Parâmetros:
        pontuacao (float): Pontuação a validar

    Retorna:
        bool: True se válida, False caso contrário
    """
    return 0 <= pontuacao <= 20


def validar_indice(indice: int, tamanho: int) -> bool:
    """
    Valida se o índice está dentro dos limites da lista.

    Parâmetros:
        indice (int): Índice a validar
        tamanho (int): Tamanho da lista

    Retorna:
        bool: True se válido, False caso contrário
    """
    return 0 <= indice < tamanho

# ============================================================
# FUNÇÕES DE GESTÃO DE DADOS
# ============================================================

def introducao_dados():
    """Permite a introdução manual de 10 filmes e pontuações."""
    global lista_filmes, lista_pontuacoes

    limpar_ecra()
    mostrar_cabecalho("📝 INTRODUÇÃO DE DADOS")

    print("\nIntroduza os dados dos 10 filmes candidatos:\n")

    # Limpar listas existentes
    lista_filmes = []
    lista_pontuacoes = []

    for i in range(10):
        print(f"--- FILME {i + 1} ---")

        # Ler nome do filme
        while True:
            nome = input("Nome do filme: ").strip()
            if nome:
                break
            print("⚠️  O nome não pode estar vazio!")

        # Ler e validar pontuação
        while True:
            try:
                pontuacao = float(input("Pontuação (0-20): "))
                if validar_pontuacao(pontuacao):
                    break
                else:
                    print("⚠️  A pontuação deve estar entre 0 e 20!")
            except ValueError:
                print("⚠️  Por favor, introduza um número válido!")

        # Adicionar às listas
        lista_filmes.append(nome)
        lista_pontuacoes.append(pontuacao)
        print("✅ Filme registado!\n")

    mostrar_cabecalho("✅ DADOS INTRODUZIDOS COM SUCESSO!")
    print(f"   Total de filmes: {len(lista_filmes)}")
    print("=" * 60)
    pausar()


def geracao_automatica():
    """Gera automaticamente dados de exemplo para testes."""
    global lista_filmes, lista_pontuacoes

    limpar_ecra()
    mostrar_cabecalho("🎲 GERAÇÃO AUTOMÁTICA DE DADOS")

    print("\nGerando dados de exemplo...\n")

    # Filmes de exemplo (Óscares 2024)
    filmes_exemplo = [
        "Oppenheimer",
        "Killers of the Flower Moon",
        "Poor Things",
        "The Holdovers",
        "Barbie",
        "Past Lives",
        "Anatomy of a Fall",
        "American Fiction",
        "The Zone of Interest",
        "Maestro",
    ]

    # Copiar filmes para a lista global
    lista_filmes = filmes_exemplo.copy()

    # Gerar pontuações aleatórias entre 10.0 e 20.0
    lista_pontuacoes = []
    for _ in range(10):
        pontuacao = round(random.uniform(10.0, 20.0), 1)
        lista_pontuacoes.append(pontuacao)

    print("✅ Dados gerados com sucesso!\n")
    pausar()

    # Mostrar os dados gerados
    consultar_dados()


def alterar_dados():
    """Permite alterar a pontuação de um filme."""
    global lista_pontuacoes

    limpar_ecra()
    mostrar_cabecalho("✏️ ALTERAR PONTUAÇÃO DE FILME")

    # Verificar se há dados
    if not lista_filmes:
        print("\n❌ Não há dados para alterar!")
        pausar()
        return

    # Mostrar lista de filmes
    print()
    consultar_dados_simples()

    # Pedir número do filme
    try:
        numero = int(input("\nDigite o número do filme (1-10): "))
        indice = numero - 1

        if not validar_indice(indice, len(lista_filmes)):
            print("\n⚠️  Número inválido!")
            pausar()
            return

        # Mostrar filme selecionado
        print(f"\nFilme selecionado: {lista_filmes[indice]}")
        print(f"Pontuação atual: {lista_pontuacoes[indice]}")

        # Pedir nova pontuação
        while True:
            try:
                nova_pontuacao = float(input("\nNova pontuação (0-20): "))
                if validar_pontuacao(nova_pontuacao):
                    break
                else:
                    print("⚠️  A pontuação deve estar entre 0 e 20!")
            except ValueError:
                print("⚠️  Por favor, introduza um número válido!")

        # Atualizar pontuação
        pontuacao_antiga = lista_pontuacoes[indice]
        lista_pontuacoes[indice] = nova_pontuacao

        print("\n✅ Pontuação alterada com sucesso!")
        print(f"   {lista_filmes[indice]}: {pontuacao_antiga} → {nova_pontuacao}")

    except ValueError:
        print("\n⚠️  Por favor, introduza um número válido!")

    pausar()


def eliminar_dados():
    """Permite eliminar um filme da lista."""
    global lista_filmes, lista_pontuacoes

    limpar_ecra()
    mostrar_cabecalho("🗑️ ELIMINAR FILME")

    # Verificar se há dados
    if not lista_filmes:
        print("\n❌ Não há dados para eliminar!")
        pausar()
        return

    # Mostrar lista de filmes
    print()
    consultar_dados_simples()

    # Pedir número do filme
    try:
        numero = int(input("\nDigite o número do filme a eliminar (1-10): "))
        indice = numero - 1

        if not validar_indice(indice, len(lista_filmes)):
            print("\n⚠️  Número inválido!")
            pausar()
            return

        # Mostrar filme selecionado
        filme = lista_filmes[indice]
        pontuacao = lista_pontuacoes[indice]
        print(f"\nFilme selecionado: {filme}")
        print(f"Pontuação: {pontuacao}")

        # Confirmar eliminação
        confirmacao = input(
            "\n⚠️  Tem a certeza que deseja eliminar este filme? (S/N): "
        ).upper()

        if confirmacao == "S":
            # Remover das listas
            lista_filmes.pop(indice)
            lista_pontuacoes.pop(indice)

            print("\n✅ Filme eliminado com sucesso!")
            print(f"   Total de filmes: {len(lista_filmes)}")
        else:
            print("\n❌ Operação cancelada!")

    except ValueError:
        print("\n⚠️  Por favor, introduza um número válido!")

    pausar()

# ============================================================
# FUNÇÕES DE CONSULTA
# ============================================================

def consultar_dados_simples():
    """Apresenta a lista de filmes de forma simples (para uso interno)."""
    print("Nº  | Filme                          | Pontuação")
    print("--  +------------------------------+----------")
    for i in range(len(lista_filmes)):
        print(f"{i + 1:<4}| {lista_filmes[i]:<30} | {lista_pontuacoes[i]}")


def consultar_dados():
    """Apresenta todos os filmes e pontuações registados."""
    limpar_ecra()
    mostrar_cabecalho("📊 LISTA DE TODOS OS FILMES")

    if not lista_filmes:
        print("\n❌ Não há dados para consultar!")
        print("\n💡 Sugestões:")
        print("   - Use a opção 1 para introduzir dados manualmente")
        print("   - Use a opção 2 para gerar dados automaticamente")
        print("   - Use a opção 9 para carregar dados de ficheiro")
        pausar()
        return

    print()
    consultar_dados_simples()
    print("=" * 60)
    print(f"Total de filmes: {len(lista_filmes)}")

    # Calcular e mostrar média
    if lista_pontuacoes:
        media = sum(lista_pontuacoes) / len(lista_pontuacoes)
        print(f"Pontuação média: {media:.2f} pontos")

    print("=" * 60)
    pausar()


def pesquisar_filme():
    """Permite pesquisar um filme pelo nome."""
    limpar_ecra()
    mostrar_cabecalho("🔍 PESQUISAR FILME")

    if not lista_filmes:
        print("\n❌ Não há dados para pesquisar!")
        pausar()
        return

    # Pedir termo de pesquisa
    termo = input("\nDigite o nome do filme (ou parte dele): ").strip().lower()

    if not termo:
        print("\n⚠️  Por favor, digite um termo de pesquisa!")
        pausar()
        return

    print("\n🔎 Procurando...")

    # Procurar filme
    encontrado = False
    for i in range(len(lista_filmes)):
        if termo in lista_filmes[i].lower():
            if not encontrado:
                print("\n✅ Filme(s) encontrado(s)!")
                print("-" * 60)
            print(f"\nNome: {lista_filmes[i]}")
            print(f"Pontuação: {lista_pontuacoes[i]} pontos")
            print(f"Posição na lista: {i + 1}")
            print("-" * 60)
            encontrado = True

    if not encontrado:
        print("\n❌ Nenhum filme encontrado com esse termo!")
        print("💡 Dica: Tente usar apenas parte do nome")

    pausar()

# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def apresentar_podio():
    """Apresenta o pódio com os 3 melhores filmes."""
    limpar_ecra()
    mostrar_cabecalho("🏆 PÓDIO DOS ÓSCARES 🏆")
    print("Melhor Filme".center(60))
    print("=" * 60)

    if not lista_filmes:
        print("\n❌ Não há dados para apresentar!")
        pausar()
        return

    # Criar cópias das listas para ordenar
    filmes_ordenados = lista_filmes.copy()
    pontuacoes_ordenadas = lista_pontuacoes.copy()

    # Ordenar por pontuação (decrescente) usando Bubble Sort
    n = len(pontuacoes_ordenadas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pontuacoes_ordenadas[j] < pontuacoes_ordenadas[j + 1]:
                # Trocar pontuações
                pontuacoes_ordenadas[j], pontuacoes_ordenadas[j + 1] = (
                    pontuacoes_ordenadas[j + 1],
                    pontuacoes_ordenadas[j],
                )
                # Trocar filmes correspondentes
                filmes_ordenados[j], filmes_ordenados[j + 1] = (
                    filmes_ordenados[j + 1],
                    filmes_ordenados[j],
                )

    # Apresentar TOP 3
    medalhas = [
        "🥇 1º LUGAR - OURO 🥇",
        "🥈 2º LUGAR - PRATA 🥈",
        "🥉 3º LUGAR - BRONZE 🥉",
    ]

    for i in range(min(3, len(filmes_ordenados))):
        print(f"\n{medalhas[i].center(60)}")
        print("         ╔══════════════════════════╗")
        print(f"         ║ {filmes_ordenados[i][:24]:<24} ║")
        print(f"         ║ Pontuação: {pontuacoes_ordenadas[i]:<13} ║")
        print("         ╚══════════════════════════╝")

    # Apresentar restantes filmes
    if len(filmes_ordenados) > 3:
        print("\n" + "-" * 60)
        print("🎬 OUTROS FILMES NOMINADOS 🎬".center(60))
        print("-" * 60)
        for i in range(3, len(filmes_ordenados)):
            print(
                f"{i + 1}. {filmes_ordenados[i]:<35} - "
                f"{pontuacoes_ordenadas[i]} pontos"
            )

    print("=" * 60)
    pausar()

# ============================================================
# FUNÇÕES DE PERSISTÊNCIA (FICHEIROS CSV)
# ============================================================

def guardar_ficheiro():
    """Guarda os dados num ficheiro CSV."""
    limpar_ecra()
    mostrar_cabecalho("💾 GUARDAR DADOS EM FICHEIRO")

    if not lista_filmes:
        print("\n❌ Não há dados para guardar!")
        pausar()
        return

    print(f"\nGuardando dados em: {FICHEIRO_CSV}\n")

    try:
        # Abrir ficheiro para escrita
        with open(FICHEIRO_CSV, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            # Escrever cabeçalho
            escritor.writerow(["Filme", "Pontuacao"])

            # Escrever dados
            for i in range(len(lista_filmes)):
                escritor.writerow([lista_filmes[i], lista_pontuacoes[i]])

        print("✅ Dados guardados com sucesso!")
        print(f"   - {len(lista_filmes)} filmes salvos")
        print(f"   - Ficheiro: {FICHEIRO_CSV}")
        print("   - Localização: pasta atual do programa")
        print("\n💡 Dica: Pode abrir este ficheiro no Excel ou Bloco de Notas")

    except Exception as e:
        print(f"\n❌ Erro ao guardar ficheiro: {e}")

    pausar()


def carregar_ficheiro():
    """Carrega dados de um ficheiro CSV."""
    global lista_filmes, lista_pontuacoes

    limpar_ecra()
    mostrar_cabecalho("📂 CARREGAR DADOS DE FICHEIRO")

    print(f"\nProcurando ficheiro: {FICHEIRO_CSV}\n")

    # Verificar se o ficheiro existe
    if not os.path.exists(FICHEIRO_CSV):
        print("❌ Ficheiro não encontrado!")
        print(f"\n💡 Certifique-se que o ficheiro '{FICHEIRO_CSV}' existe")
        print("   na mesma pasta do programa.")
        pausar()
        return

    print("✅ Ficheiro encontrado!\n")
    print("Carregando dados...\n")

    try:
        # Limpar listas atuais
        lista_filmes = []
        lista_pontuacoes = []

        # Abrir e ler ficheiro
        with open(FICHEIRO_CSV, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            # Ignorar cabeçalho
            next(leitor, None)

            # Ler dados
            for linha in leitor:
                if len(linha) >= 2 and linha[0].strip():
                    filme = linha[0].strip()
                    pontuacao = float(linha[1])

                    lista_filmes.append(filme)
                    lista_pontuacoes.append(pontuacao)

        print("✅ Dados carregados com sucesso!")
        print(f"   - {len(lista_filmes)} filmes carregados")
        print("   - Dados anteriores substituídos")

        # Mostrar preview
        if lista_filmes:
            print("\nFilmes carregados:")
            for i in range(min(3, len(lista_filmes))):
                print(f"{i + 1}. {lista_filmes[i]} - {lista_pontuacoes[i]}")
            if len(lista_filmes) > 3:
                print(f"... e mais {len(lista_filmes) - 3} filmes")

    except Exception as e:
        print(f"\n❌ Erro ao carregar ficheiro: {e}")
        lista_filmes = []
        lista_pontuacoes = []

    pausar()

# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():
    """Apresenta o menu principal do sistema."""
    limpar_ecra()
    print("=" * 60)
    print("🎬 SISTEMA DE GESTÃO DOS ÓSCARES 🏆".center(60))
    print("Categoria: Melhor Filme".center(60))
    print("=" * 60)
    print("\n📋 MENU PRINCIPAL")
    print("-" * 60)
    print("1.  Introduzir dados manualmente")
    print("2.  Gerar dados automaticamente (teste)")
    print("3.  Alterar pontuação de um filme")
    print("4.  Eliminar um filme")
    print("5.  Consultar todos os filmes")
    print("6.  Pesquisar filme específico")
    print("7.  Apresentar pódio (TOP 3)")
    print("8.  Guardar dados em ficheiro")
    print("9.  Carregar dados de ficheiro")
    print("10. Sair")
    print("-" * 60)


def menu_principal():
    """Função principal que gere o menu e as opções."""
    while True:
        mostrar_menu()

        try:
            opcao = input("\nEscolha uma opção (1-10): ").strip()

            if opcao == "1":
                introducao_dados()
            elif opcao == "2":
                geracao_automatica()
            elif opcao == "3":
                alterar_dados()
            elif opcao == "4":
                eliminar_dados()
            elif opcao == "5":
                consultar_dados()
            elif opcao == "6":
                pesquisar_filme()
            elif opcao == "7":
                apresentar_podio()
            elif opcao == "8":
                guardar_ficheiro()
            elif opcao == "9":
                carregar_ficheiro()
            elif opcao == "10":
                limpar_ecra()
                print("\n" + "=" * 60)
                print("👋 Obrigado por utilizar o Sistema de Gestão dos ÓSCARES!")
                print("=" * 60)
                break
            else:
                print("\n⚠️  Opção inválida! Por favor, escolha entre 1 e 10.")
                pausar()

        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrompido pelo utilizador.")
            break
        except Exception as e:
            print(f"\n⚠️  Erro inesperado: {e}")
            pausar()

# ============================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================

if __name__ == "__main__":
    menu_principal()

