# Dicionario para armazenar todas as movimentacoes financeiras em memoria
lista_de_transacoes_e_despesas = {}

# Variavel global para rastrear o saldo atual da conta
saldo = 0.0

def adicionar_transacoes():
    global saldo # Permite a modificacao da variavel global 'saldo'
    
    print('\n--- ADICIONAR RECEITA ---')
    try:
        nome_da_transacao = input('Digite o titulo da receita: ')
        valor_da_transacao = float(input('Digite o valor da receita (R$): '))
        saldo += valor_da_transacao
        print('\n[+] Receita adicionada com sucesso!')
        input('Aperte ENTER para voltar ao Menu Inicial...')
    except ValueError:
        print('\n[!] Erro: Por favor, digite um valor numerico valido.')
        return # Interrompe a funcao para nao registrar dados vazios ou invalidos

    # Verifica se o dicionario possui itens para gerar um ID sequencial
    if lista_de_transacoes_e_despesas:
        novo_id = max(lista_de_transacoes_e_despesas.keys()) + 1
    else:
        novo_id = 1
    
    # Armazena a transacao no formato de dicionario aninhado
    lista_de_transacoes_e_despesas[novo_id] = {
        'categoria': 'Receita', 
        'nome': nome_da_transacao, 
        'valor': valor_da_transacao
    }

def adicionar_despesas():
    global saldo
    
    print('\n--- ADICIONAR DESPESA ---')
    try:
        nome_da_despesa = input('Digite o titulo da despesa: ')
        valor_da_despesa = float(input('Digite o valor da despesa (R$): '))
        saldo -= valor_da_despesa
        print('\n[-] Despesa adicionada com sucesso!')
        input('Aperte ENTER para voltar ao Menu Inicial...')
    except ValueError:
        print('\n[!] Erro: Por favor, digite um valor numerico valido.')
        return

    # Logica de auto-incremento do ID
    if lista_de_transacoes_e_despesas:
        novo_id = max(lista_de_transacoes_e_despesas.keys()) + 1
    else:
        novo_id = 1
    
    lista_de_transacoes_e_despesas[novo_id] = {
        'categoria': 'Despesa', 
        'nome': nome_da_despesa, 
        'valor': valor_da_despesa
    }

def listar_transacoes():
    print('\n--- EXTRATO DE MOVIMENTACOES ---')
    
    # Checa se o dicionario nao esta vazio antes de iterar
    if lista_de_transacoes_e_despesas:
        for id_item, dados in lista_de_transacoes_e_despesas.items():
            categoria = dados['categoria']
            nome = dados['nome']
            valor = dados['valor']
            
            # Define o sinal de exibicao baseado na categoria
            sinal = "+" if categoria == 'Receita' else "-"
            
            # Utiliza f-strings com formatacao de espacamento para criar uma tabela alinhada
            print(f"ID: {id_item:02d} | {categoria:<8} | {nome:<15} | {sinal} R$ {valor:.2f}")
    else:
        print('Nenhuma movimentacao registrada ate o momento.')
    input('Aperte ENTER para voltar ao Menu Inicial...')
        
    print('--------------------------------')

def visualizar_saldo():
    print('\n--- SALDO ATUAL ---')
    print(f'Disponivel: R$ {saldo:.2f}')
    print('-------------------')
    input('Aperte ENTER para voltar ao Menu Inicial...')

# Loop principal de execucao do programa
while True:
    print('\n=======================================')
    print('   GERENCIADOR FINANCEIRO NO TERMINAL  ')
    print('=======================================')
    print('1. Adicionar nova Receita')
    print('2. Adicionar nova Despesa')
    print('3. Listar movimentacoes')
    print('4. Visualizar Saldo')
    print('5. Sair')
    print('=======================================')
    
    try:
        escolha_do_usuario = int(input('\nEscolha uma opcao: '))
        
        # Estrutura de controle para direcionar as acoes do menu
        if escolha_do_usuario == 1:
            adicionar_transacoes()
        elif escolha_do_usuario == 2:
            adicionar_despesas()
        elif escolha_do_usuario == 3:
            listar_transacoes()
        elif escolha_do_usuario == 4:
            visualizar_saldo()
        elif escolha_do_usuario == 5:
            print('\nEncerrando o programa. Ate logo!\n')
            break # Quebra o loop while e finaliza o script
        else:
            print(f'\n[!] Opcao invalida ({escolha_do_usuario}). Escolha um numero entre 1 e 5.')
            
    except ValueError:
        # Captura o erro caso o usuario digite uma letra ou simbolo em vez de numero no menu
        print('\n[!] Erro: Entrada invalida. Por favor, digite apenas o numero da opcao desejada.')