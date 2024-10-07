# 📅 GestInit - Cálculo de DPP e DUM

**GestInit** é um pacote simples em Python projetado para calcular a **Data Provável do Parto (DPP)** e a **Data da Última Menstruação (DUM)** com base na idade gestacional (semanas e dias). Ele fornece funções práticas e auxiliares para lidar com cálculos comuns no acompanhamento gestacional.

## 📋 Funcionalidades

- **Cálculo da DPP**: Calcula a Data Provável do Parto com base em semanas, dias e uma data de referência.
- **Cálculo da DUM**: Calcula a Data da Última Menstruação com base na idade gestacional fornecida e calcula a DPP de brinde! ❤

## 🛠️ Instalação

Clone este repositório ou faça o download diretamente:

```bash
git clone https://github.com/jeymerson/calc_gest_py.git
```

Navegue até o diretório do projeto e instale os pacotes necessários (se houver dependências):

```bash
cd gestinit
pip install -r requirements.txt
```

> **Nota:** O projeto não possui dependências externas além do Python padrão.

## 🚀 Como Usar

### 1. Importando o Pacote

Você pode importar as funções principais do pacote da seguinte forma:

```python
from gest_init import func_calcular_dpp, calc_DUM
```

### 2. Exemplo de Cálculo da DPP

```python
from datetime import datetime
from gest_init import func_calcular_dpp

# Definindo semanas e dias de gestação
semanas = 20
dias = 3
data_referencia = datetime(2024, 5, 10)  # data de referência

resultado_dpp = func_calcular_dpp(semanas, dias, data_referencia)
print(resultado_dpp)
```

### 3. Exemplo de Cálculo da DUM

```python
from datetime import datetime
from gest_init import calc_DUM

# Definindo semanas e dias de gestação
semanas = 12
dias = 5
data_referencia = datetime(2023, 8, 15)

resultado_dum = calc_DUM(semanas, dias, data_referencia)
print(resultado_dum)
```

## 📂 Estrutura principal do projeto 

```plaintext
gestinit/
│
├── __init__.py       # Inicializador do pacote
├── gest_init.py      # Funções principais: DPP e DUM
└── __auxiliares.py     # Funções auxiliares para cálculo e formatação
```

### Funções Principais

- `func_calcular_dpp(semanas, dias, data=datetime.today())`: Calcula a Data Provável do Parto (DPP) com base na idade gestacional.
- `calc_DUM(semanas, dias, data=datetime.today())`: Calcula a Data da Última Menstruação (DUM) com base na idade gestacional e aciona o cálculo da DPP.

### Observações

- `Pré-validação`: É feita uma breve validação para verificar se a data é válida.
- `Caso a data não seja passada`: O programa entende que a data é a atual.
- `Você poderá ter respostas diferentes dependendo da idade gestacional`: **(01)** Idade padrão / **(02)** DPP for no mesmo dia / **(03)** Quantos dias passaram da DPP.
- `Sobre o __auxiliares.py`: Contém mini-funções especializadas em atividades distintas que auxiliam nas funções principais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir _issues_ ou enviar _pull requests_ para melhorias.

1. Faça o _fork_ do projeto
2. Crie uma nova _branch_ para sua funcionalidade ou correção de bug: `git checkout -b minha-nova-funcionalidade`
3. Envie suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. _Push_ para a _branch_: `git push origin minha-nova-funcionalidade`
5. Abra um _pull request_!

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.