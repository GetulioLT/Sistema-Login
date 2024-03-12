# 🚀 Configuração do Projeto

## 📚 Explicações
Seguindo agora na branch mvc, foi feita a separação do projeto em camadas, onde a camada de model é responsável por toda a lógica de negócio, a camada de view é responsável por toda a interação com o usuário e a camada de controller é responsável por intermediar a comunicação entre a camada de model e a camada de view.

O guia a seguir segue o mesmo da branch main, com a diferença de que agora o projeto está separado em camadas.

## 🛠️ Pré-requisitos
Certifique-se de ter o Python, pip e o git instalados em seu sistema.

## 📥 Download do Projeto
Primeiro, com o git instalado, você pode clonar o projeto com o seguinte comando:

```bash
git clone https://github.com/GetulioLT/Sistema-Login.git
```

## 🌐 Criação e Ativação do Ambiente Virtual
1. Com o projeto clonado, abra o terminal e navegue até a pasta do projeto. Em seguida, crie um ambiente virtual com o seguinte comando (substitua "version" pela versão do Python que você está utilizando):

```bash
python -version -m venv venv
```
2. Ative o ambiente virtual:

```bash
venv/bin/activate
```

## 📦 Instalação das Dependências
Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 🗄️ Configuração do Banco de Dados
Navegue até a pasta api e execute os seguintes comandos:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## 🚀 Execução da API e do Frontend
1. Com o banco de dados configurado, execute a API:

```bash
cd api
python app.py
```

2. Com a API em execução, abra um novo terminal, navegue até a pasta raiz e execute o frontend:

```bash
flask run
```

## 🌐 Acesso ao Sistema e à API

Com a API e o Frontend em execução, você pode acessar:

- O sistema de login e cadastro através do seguinte endereço:

```bash
http://localhost:5000
```

- A API através do seguinte endereço:

```bash
http://localhost:5001
```

## 📜 Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE.md) para obter detalhes.

## 👨‍💻 Autor
Feito por Getulio Vagner Miranda Santos. 
- GitHub: [GetulioLT](https://github.com/GetulioLT)
- LinkedIn: [Getulio Vagner](https://www.linkedin.com/in/getulio-vagner-117341186/)

