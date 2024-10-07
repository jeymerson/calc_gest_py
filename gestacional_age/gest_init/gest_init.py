
from datetime import datetime, timedelta
from __auxiliares import aux_data_dif, aux_dias_para_dias, aux_dias_para_semanas, aux_total_dias, aux_validacao_DPP, axu_para_40_sem

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
