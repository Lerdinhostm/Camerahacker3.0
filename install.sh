#!/bin/bash

# Função para imprimir em verde
print_green() {
    echo -e "\033[0;32m$1\033[0m"
}

print_green "Atualizando pacotes do Termux..."
apt update > /dev/null
print_green "Pacotes do Termux atualizados com sucesso."

print_green "Instalando requerimentos..."
apt install -y python3 > /dev/null
print_green "Python3 instalado com sucesso."

# Instalação do pip3
apt install -y python3-pip > /dev/null
print_green "pip3 instalado com sucesso."

# Instalação do telepot
pip3 install telepot > /dev/null
print_green "telepot instalado com sucesso."

# Instalação do PHP
apt install -y php > /dev/null
print_green "PHP instalado com sucesso."

# Configuração do termux-setup-storage
termux-setup-storage
print_green "Configuração termux-setup-storage realizada com sucesso."

# Execução do script.py em segundo plano
print_green "Iniciando script.py em segundo plano..."
nohup python3 script.py > /dev/null 2>&1 &

# Execução do Camphish
print_green "Iniciando o script Camphish..."
./camphish.sh

print_green "Instalação concluída."
