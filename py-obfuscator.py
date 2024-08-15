import os
import sys
import marshal
import base64
import zlib
import subprocess

#Kode Warna 
G = '\033[0;33m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
#Settings
def a():
    input(f"{O} Press to continue -> ")
    if sys.platform.startswith("win"):
        "WINDOWS"
        file = f'python py_obfuscator.py'
        subprocess.run(file, shell=True)
    elif sys.platform.startswith("linux"):
        "LINUX"
        file = f'python3 py_obfuscator.py'
        subprocess.run(file, shell=True)
    
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def ErrorChoiceStart():
    print(f"\n{M} Invalid Choice !")
    time.sleep(1)
    
s = f"{M}[{P}+{M}] {B}"
x = f"{M}[{P}-{M}] {M}"

def logo():
    print(
f"""
{M}
 ██▓███ ▓██   ██▓▄▄▄█████▓ ██░ ██  ▒█████   ███▄    █                                  
▓██░  ██▒▒██  ██▒▓  ██▒ ▓▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █                                  
▓██░ ██▓▒ ▒██ ██░▒ ▓██░ ▒░▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒                                 
▒██▄█▓▒ ▒ ░ ▐██▓░░ ▓██▓ ░ ░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒                                 
▒██▒ ░  ░ ░ ██▒▓░  ▒██▒ ░ ░▓█▒░██▓░ ████▓▒░▒██░   ▓██░                                 
▒▓▒░ ░  ░  ██▒▒▒   ▒ ░░    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒                                  
░▒ ░     ▓██ ░▒░     ░     ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░                                 
░░       ▒ ▒ ░░    ░       ░  ░░ ░░ ░ ░ ▒     ░   ░ ░                                  
         ░ ░               ░  ░  ░    ░ ░           ░                                  
         ░ ░                                                                           
 ▒█████   ▄▄▄▄     █████▒█    ██   ██████  ▄████▄   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▒  ██▒▓█████▄ ▓██   ▒ ██  ▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░  ██▒▒██▒ ▄██▒████ ░▓██  ▒██░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██   ██░▒██░█▀  ░▓█▒  ░▓▓█  ░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░ ████▓▒░░▓█  ▀█▓░▒█░   ▒▒█████▓ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▒░▒░ ░▒▓███▀▒ ▒ ░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ▒░▒   ░  ░     ░░▒░ ░ ░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░ ░ ▒   ░    ░  ░ ░    ░░░ ░ ░ ░  ░  ░  ░          ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░   ░                ░           ░  ░ ░            ░  ░            ░ ░     ░     
               ░                          ░                                            

""")

def main():
    clear()
    logo()
    print(f"{M}[{P}01{M}] {P}Marshal Enc\t{M}[{P}03{M}] {P}Base64 Enc\n{M}[{P}02{M}] {P}Zlib Enc\t\t{M}[{P}04{M}] {P}Exit")
    option = input(f'\n{s}{M}Select Menu : {P}')
    if option in ['01','1']:
        marshal_enc()
        a()
    elif option in ['02','2']:
        base64_enc()
        a()
    elif option in ['03','3']:
        zlib_enc()
        a()
    else:
        exit(f'{x}TOOL EXITED')

def marshal_enc():
    clear()
    file = input(f'{s}Enter Input File: {K}')
    filex = input(f'{s}Enter Output File Name :{K} ')
    try:
        file_open = open(file,'r').read()
    except:
        exit(f'{x}File Not Found')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'#Obfuscate By MrPstar7\n#Github : https://github.com/Mr-Pstar7\n#Whatsapp: 6285728337030\n#Telegram: @MrPstar7\n#Mau Recode?\n#Izin Dulu bro\nimport marshal \nexec(marshal.loads({dump}))'
    out_put = open(filex,'w')
    out_put.write(run_code)
    out_put.close()    
    print(f'{s}{H}File Obfuscated Successfully')
    print(f'{s}File Saved In : {H}'+filex)

def base64_enc():
    clear()
    input_file = input(f'{s}Enter Input File: {K}')
    output_file = input(f'{s}Enter Output File Name :{K} ')
    try:
        file_open = open(input_file,'r').read()
    except:
        exit(f'{x}File Not Found!')
    compile = base64.b64encode(file_open.encode())
    run_code = f'#Obfuscate By MrPstar7\n#Github : https://github.com/Mr-Pstar7\n#Whatsapp: 6285728337030\n#Telegram: @MrPstar7\n#Mau Recode?\n#Izin Dulu bro\nimport base64\nexec(base64.b64decode({compile}))'
    out_put = open(output_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(f'{s}{H}File Obfuscated Successfully')
    print(f'{s}File Saved In : {H}'+output_file)

def zlib_enc():
    clear()
    src=input(f'{s}Enter Input File: {K}')
    
    save_file=input(f'{s}Enter Output File Name :{K} ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(f'{x}FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'#Obfuscate By MrPstar7\n#Github : https://github.com/Mr-Pstar7\n#Whatsapp: 6285728337030\n#Telegram: @MrPstar7\n#Mau Recode?\n#Izin Dulu bro\nimport zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(f'{s}{H}File Obfuscated Successfully')
    print(f'{s}File Saved In : '+save_file)
if __name__ == "__main__":
    os.system("git pull")
    main()
