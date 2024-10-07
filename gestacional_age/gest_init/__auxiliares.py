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

