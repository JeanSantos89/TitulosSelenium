## 📃 Resumo
Este projeto automatiza a coleta de títulos de livros do site [Books to Scrape](http://books.toscrape.com/) com Selenium, de acordo com uma categoria escolhida. 
Após a coleta, os títulos são enviados automaticamente por e-mail via Gmail, utilizando um perfil já logado no navegador.

## 🛠 Tecnologias Utilizadas

  - 🐍 Python 3
  - 🌐 Selenium  
  - 🧭 Chrome WebDriver  
  - 📧 Gmail (perfil logado no navegador)  
  - 🗝️ python-dotenv 

## 📁 Estrutura do Projeto
Projeto_Scraping/ 
    - Captar_titulos.py # Recebe o gênero desejado, coleta da categoria e chama a função de envio de e-mail 
    - Enviar_email.py # Função para abrir o Gmail no Chrome e enviar o e-mail automaticamente 
    - env # (opcional) Armazena variáveis sensíveis, como email do destinatário 
    - README.md 

## 
⁉️ Como utilizar?
    - 1. Instale os pacotes necessários:
        1. pip install selenium
        2. pip install python-dotenv
        3. Baixe o ChromeDriver e transfira o drive para a pasta: Windows
        4. .env: adicione suas informações - login e senha do aplicativo gmail (do aplicativo, não da conta).
    - 2. Siga a ordem de execução:
        1. python Captar_titulos.py
        2. Digite o gênero que você deseja saber os títulos
        3. Digite o e-email para quem deseja enviar

## 📃 Licença
Este projeto é de uso livre para fins de estudo e aprendizado.
