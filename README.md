# BotCity ENEM Top 10 Books Bot
### Descrição
Este bot foi desenvolvido com o BotCity e tem como objetivo identificar e listar os 10 livros que mais frequentemente aparecem nas provas do ENEM. Ele automatiza a coleta dessas informações de fontes confiáveis, o site que utilizei para fazer a coleta foi o  [Livros&Livros](https://www.livroselivros.com.br)

### Funcionalidades
- Gera alerta de inicio da automação no Orquestrador BotCity
- Extrai informações dos 10 livros
- Cria um log com as informações extraidas do site no Orquestrador BotCity

### Requisitos
  - Navegador Web (Firefox, Chrome ou qualquer outro)
  - Java
  - Python 3.7 ou superior
  - Pacotes Python
    - pip
    - setuptools
    - virtualenv
    - cookiecutter (apenas desenvolvimento)

### Instalação 
1. Clone este repositório para sua máquina local:
``` bash
git clone https://github.com/MatheeusPinheiro/bot_livros.git
cd bot_livros
```
2. Crie um ambiente virtual e ative-o:
``` bash
python -m venv venv
source venv/Scripts/activate # No Windows use `venv\Scripts\activate`
```
3. Instale as dependências necessárias:
``` bash
pip install -r requirements.txt
```

### Uso
Para executar o bot, use o comando:
``` bash
python bot.py
```



