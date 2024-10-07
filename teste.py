from datetime import datetime
from gestacional_age import gest_init 
# from gestacional_age import func_calcular_dpp
# Definindo semanas e dias de gestação
semanas = 20
dias = 3
data_referencia = datetime(2024, 5, 10)  # data de referência

resultado_dpp = gest_init.func_calcular_dpp(semanas, dias, data_referencia)
print(resultado_dpp)