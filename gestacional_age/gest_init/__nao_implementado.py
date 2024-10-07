from datetime import datetime, timedelta

class gest():
    def __init__(self, day=(datetime.now()).day, month=(datetime.now()).month, year=(datetime.now()).year):
        self.day= day
        self.month= month
        self.year= year
        self.LPM = None
        self.week = None
        self.day = None
    
    def all_days(self):
        return (self.week * 7) + day


    def LPM_for_age(self):
        self.LPM = datetime.timetz()

    @property
    def LMP(self):
        return self.LPM
    @property
    def week(self):
        return self.week
    @property
    def day(self):
        return self.day
    

    
class baby:
    def __init__(self, week, day):
        self.week = week
        self.day = day
    
    def all_day(self):
        return (self.week * 7) + day
    



def calc_DPP(week, day,date = datetime.now()):
    # date = datetime(date)
    print(date)
    total_days = (week*7)+day
    para_40_sem = 280 - total_days 
    data_dpp = (date + timedelta(days=(para_40_sem))).strftime("%d/%m/%y")

    if para_40_sem > 0:
        return f"\tA data do parto é {data_dpp}\n\tsemanas: {week} e {day} dias"
    elif para_40_sem == 0:
        return f"A data do parto é hoje! {data_dpp}"
    else:  
        return f"Foi passado {para_40_sem} da DPP ({data_dpp})"
    
#FIXME: Usado como base da função atual
def calcular_DPP_hoje(semanas, dias,data=datetime.now()):
    para_40_sem = axu_para_40_sem(aux_total_dias(semanas, dias)) 
    data_dpp = aux_formatar_data((data + timedelta(days=(para_40_sem))))
    if data != datetime.now():
        pass
    return aux_validacao_DPP(para_40_sem,data_dpp,semanas,dias)


day = (datetime.now()).day
month = (datetime.now()).month
year = (datetime.now()).year




def aux_data_objeto(*dia,mes,ano):   #cria um objeto data e hora ou dá um false
    data_validacao = validacao_data(dia,mes,ano)
    if data_validacao:
        ano = aux_validacao(ano)
        objeto_data = datetime(ano,mes,dia)
        return objeto_data
    return False
    

#FIXME: deverá ser implementado futurmente 
def validacao_data(dia,mes,ano): #válida se o usuário quer criar um objeto date e hora com parâmetros inválidos
    if dia > 31:
        return False
    if mes > 13:
        return False
    if (ano > 99) or (ano < 2000):
        return False
    return True

def aux_validacao(ano):
    if ano < 99:
        ano += 2000
    return ano