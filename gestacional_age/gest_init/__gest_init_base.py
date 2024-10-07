
from datetime import datetime, timedelta

def aux_dias(dia): #função que auxiliar que formata uma saída dependendo do dia atual da gestação
    if dia == 0: # caso não tenha dias ou seja = 0 / não exibirá nada
        return ""
    if (dia == 1) or (dia == -1): # caso o dia seja 1, será exibido 1 dia / para questões de plural
        if (dia == -1):
            return " 01 dia"
        return " e 01 dia"
    if (dia > 1) or (dia < -1): #para para caso o dia for maior que um / caso de plural
        if (dia < 1):
            return f"{abs(dia)} dias" #ABS FAZ O número positivo
        return f" e 0{dia} dias"

def aux_formatar_data(objeto_data): #função para formatar o objeto datetime de forma adequada / para dia/mes/ano
    return objeto_data.strftime("%d/%m/%y")

def aux_total_dias(semanas, dias): # função que converte semanas em dias e soma com o dia passado, resultando em total de dias absoluto.
    return (semanas*7) + dias # obs, como uma semana tem 7 dias então cada semana vale 7 dias

def aux_resumo(semanas,dias): #devolve semanas e dias formatado  / para formatação de idade gestacional
    return f"Idade gestacional: {semanas} semanas{aux_dias(dias)}."

#Função auxiiar que válida, formata e devolve o resultado de um cálculo gestacional
def aux_validacao_DPP(relacao_40_semanas,data_dpp,semanas,dias): # função para validação sobre o resultado das 40 semanas

    # se a idade gestacional foi até 39 semanas e 6 dias, então será exibida a idade gestacional
    if relacao_40_semanas > 0 and relacao_40_semanas < 280: #validação se stá na data correta
        return f"\tA data do parto é {aux_formatar_data(data_dpp)}\n\t{aux_resumo(semanas,dias)}"
    # se for exatamente igual a 280, quer dizer que está na data atual do parto
    elif relacao_40_semanas == 280:
        return f"A data do parto é hoje! {data_dpp}"
    # se entrar aqui, quer dizer que passou da data das 40 semanas
    else:  
        return f"Foi passado {aux_dias(axu_para_40_sem(relacao_40_semanas))} da DPP ({aux_formatar_data(data_dpp)})"
   

def aux_data_dif(data1,data2): #cálcula a diferença entre duas datas
    dias = data1 - data2
    return dias.days

def aux_dias_para_semanas(dias_base): # converta o total de dias em semanas
    semanas = int(dias_base / 7)
    return semanas

def aux_dias_para_dias(dias_base): #converte o resto da divisão de total de dias em semanas
    dias = dias_base % 7
    return dias

def axu_para_40_sem(total_dias): # 280 dias sáo 40 semanas em ig
    return 280 - total_dias



def func_calcular_dpp(semanas,dias,data=datetime.today()):
    # Verifica se o objeto passado é do tipo datetime
    if not isinstance(data, datetime):
        raise ValueError("O parâmetro 'data' deve ser um objeto datetime.")
    #----- Parte que cálcula o tempo passo até o momento da gestação 
    dias_corrido = aux_data_dif(datetime.now(), data) + aux_total_dias(semanas, dias) # cálcula a diferença de dias da date e de agora e soma com os dias passados da semana
    #----- Parte que cálcula a DPP com base na data passada os dias que faltam para 40 semanas subtraidos de função passada
    DPP = data + timedelta(days=axu_para_40_sem(aux_total_dias(semanas, dias)))
    # ---- essa parte devolve a semana atual da gestação
    semanas_atual = aux_dias_para_semanas(dias_corrido)
    # essa parte devolve o dia atual da gestação
    dias_atual = aux_dias_para_dias(dias_corrido)
    # essa parte formata todo o trabalho feito e retorna de forma organizada os resultados.
    return aux_validacao_DPP(dias_corrido,DPP,semanas_atual,dias_atual)
  
def calc_DUM(semanas, dias, data=datetime.today()):
    # Verifica se o objeto passado é do tipo datetime
    if not isinstance(data, datetime):
        raise ValueError("O parâmetro 'data' deve ser um objeto datetime.")
    total_dias = aux_total_dias(semanas, dias)

    if data != datetime.today(): # verifica se uma data diferente da data atual foi passada 
        # ---- esta parte cálcula a idade gestacional atual
        dias_corrido = aux_data_dif(datetime.now(), data) + aux_total_dias(semanas, dias)
        # ---- essa parte devolve a semana atual da gestação
        semanas = aux_dias_para_semanas(dias_corrido)
        # ----essa parte devolve o dia atual da gestação
        dias = aux_dias_para_dias(dias_corrido)
        # esta parte cálcula a dum
        data_dum = data - timedelta(days=(total_dias))

    else: # caso o dia for o mesmo, entrará aqui e retornará a DUM
        data_dum = data - timedelta(days=(total_dias))
    # o retorno será modificado para sair visualmente agradável        
    return f"\tA data da últuma menstruação é {(data_dum).strftime("%d/%m/%y")}\n{func_calcular_dpp(semanas,dias,data)}"

data_exemplo = datetime(2024,10,1) 

print(calc_DUM(22,4,))
