# API-Trabalho-de-Sistemas-Distribuidos
# Instruções para rodar a aplicação Django

## Requisitos iniciais
  1. Ter o Linux Ubuntu 20.04 ou superior na sua máquina
  2. Ter o Python instalado na máquina 
  3. Baixar uma IDE para trabalhar com o Django, sugerimos (Visual Studio Code)
  4. Baixar e configurar o git em seu computador
  5. Baixar e configurar o postgres em seu linux: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04
  
## Clonando o repositório
  Para clonar o repositório utilize o seguinte comando   
  
      git clone https://github.com/KarolAz22/API-Trabalho-de-Sistemas-Distribuidos.git
      
  Entre no diretório API-Trabalho-de-Sistemas-Distribuidos/ com o seguinte comando   
  
      cd API-Trabalho-de-Sistemas-Distribuidos/
      
  Agora crie uma virtual environment para instalar as dependencias  
  
      python3 -m venv env
      
  Agora ative sua virtual environment
  
      source env/bin/activate
      
  Após ativar você instala as depedencias que estão no arquivo requirements.txt com o seguinte comando:
  
      pip install -r requirements.txt
      
  E por ultimo abra seu projeto no Visual Studio Code
  
      code .
  
  Para fazer as migrações basta rodar o comando
      
      python3 manage.py makemigrations
  
  Logo depois:
      
      python3 manage.py migrate
