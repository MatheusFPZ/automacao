import subprocess
import os
import shutil
import time

# Verifica se o processo está rodando e mata, se necessário
def check_process_running(process_name):
    try:
        result = subprocess.run(['tasklist', '/fi', f'imagename eq {process_name}'], stdout=subprocess.PIPE, text=True)
        output = result.stdout.lower()

        if process_name.lower() in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao verificar o processo: {e}")
        return False

process_name = "outlook.exe"
is_running = check_process_running(process_name)

if is_running:
    subprocess.run(["taskkill", "/F", "/IM", process_name], stdout=subprocess.PIPE, text=True)
    print(f"O processo {process_name} foi finalizado.")
    time.sleep(5)

    
   #copiar 
def find_and_copy_psts(destination_folder):
    user_profile_folder = os.path.expandvars(r"C:\Users\%USERNAME%")
    outlook_folder = os.path.join(user_profile_folder, 'Documents', 'Arquivos do Outlook')

    

    if os.path.exists(outlook_folder):
     for root, _, files in os.walk(outlook_folder):
            for file in files:
                if file.lower().endswith('.pst'):
                    pst_file = os.path.join(root, file)
                    temp_pst_file = os.path.join(destination_path, f"{file}.temp")
                    try:
                        shutil.copy(pst_file, temp_pst_file)
                        print(f"Arquivo .pst copiado para {temp_pst_file}")
                    except Exception as e:
                        print(f"Erro ao copiar {pst_file} para {temp_pst_file}: {e}")

                    try:
                        # Renomear o arquivo temporário no servidor para substituir o original
                        os.replace(temp_pst_file, os.path.join(destination_path, file))
                        print(f"Arquivo .pst substituído no servidor: {file}")
                    except Exception as e:
                        print(f"Erro ao substituir {temp_pst_file} no servidor por {file}: {e}")
    else:
        print("Nenhum arquivo .pst encontrado.")

if __name__ == "__main__":
    destination_path = r"\\MICRO06\backupemails" 
    find_and_copy_psts(destination_path)
