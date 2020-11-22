<h1 align="center">Desafio Luiza Code 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/anageorgia/desafio_luiza_code/blob/main/LICENSE" target="_blank">
    <img alt="License: GPL--3.0" src="https://img.shields.io/badge/License-GPL--3.0-yellow.svg" />
  </a>
</p>

> Criação de um marketplace onde é possível um vendedor cadastrar, atualizar e buscar produtos. Além disso ele também será capaz de consultar seu estoque e sinalizar produtos inativos.

## Equipe - Las Paythonettes

👤 **Ana Geórgia Gama**

* Github: [@anageorgia](https://github.com/anageorgia)
* LinkedIn: [@anageorgia](https://linkedin.com/in/anageorgia)

👤 **Suellen Guimarães**

* Github: [@Suele](https://github.com/Suele)

👤 **Vânia Barbosa**

* Github: [@vaniapatriciab](https://github.com/vaniapatriciab)

👤 **Amanda Hellen Pereira Delgado**

* Github: [@](https://github.com/)

👤 **Elza Meira Puppo**

* Github: [@ElzaPuppo](https://github.com/ElzaPuppo)
* LinkedIn: [@elzapuppo](https://linkedin.com/in/elzapuppo)

👤 **Victória Simonetti Portella**

* Github: [@victoriasimonetti](https://github.com/victoriasimonetti)

## Rodando o projeto
1. Através do seu terminal, baixe o projeto através do comando:
  `git clone https://trello.com/c/4W15ZIMV/34-como-baixar-o-projeto-do-git-passo-a-passo`

2. Entre na pasta do projeto
  `cd desafio_luiza_code`

3. Crie um ambiente virtual

- No mac/linux:
  `python3 -m venv venv_LuizaCodeDesafioFinal`

- No windows:
  `python -m venv venv_LuizaCodeDesafioFinal`

4. Ative seu ambiente virtual

- No mac/linux:
`source venv_LuizaCodeDesafioFinal`

- No windows:
  - Se você estiver usando o terminal do Windows PowerShell o comando é:
  `venv_LuizaCodeDesafioFinal\Scripts\activate`

  - No CMD:
  `venv_LuizaCodeDesafioFinal\Scripts\activate.bat`

  - No terminal do VSCode
  `. myvenv\Scripts\activate.ps1`

5. Instale as dependências do projeto
- No mac/linux:
`pip3 install -r requirements.txt`

- No windows e algumas distribuições do linux:
`pip install -r requirements.txt`

6. Faça as migrações do banco de dados
`python manage.py migrate`

7. Crie seu usuário com poderes de administrador/superusuário:
  Forneça um nome, email e senha para este usuário

8. Entre na pasta luiza_code
`cd luiza_code`

9. Rode o servidor local
`python manage.py runserver`

Para acessar nossa plataforma de Marketplace da Lu, agora basta você abrir seu navegador e acessar através do endereço:
> http://localhost:8000

A página inicial mostra os produtos cadastrados, quem é o vendedor responsável, descrição, quantidade disponível em estoque e mais. Faça login com o nome de usuário e senha que você criou no passo 7 para ter acesso à área de vendedor, podendo adicionar, atualizar, inativar/ativar e excluir produtos.


## 📝 License

This project is [GPL--3.0](https://github.com/anageorgia/desafio_luiza_code/blob/main/LICENSE) licensed.

