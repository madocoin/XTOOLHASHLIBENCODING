#!/use/bin/python3
import time
import hashlib
import os , sys
from platform import system
#!/use/bin/pip3
# install library colorama

try:
    import colorama 
except:
        os.system("pip3 install colorama")
finally:
    from colorama import Fore
    
#clear cmd termux ....
def clear_sys():
    
    if system() == 'Linux':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')
    else:
        pass;
        
#logo
logo = f'''{Fore.GREEN}
FOR HELPED YOU ...

                                                     ___FONCTIONS_HASHLIB___
{hashlib.__all__}

                            {Fore.YELLOW}_TIPES_HASH
 {Fore.BLUE}algorithms_guaranteed✓
{hashlib.algorithms_guaranteed}
{Fore.RED}algorithms_available!?
{hashlib.algorithms_available}

{Fore.YELLOW}???????????????? Hidden fonction. ?????????????????????
 [`scrypt']                 
{Fore.CYAN}                    
      ___           ___           ___           ___           ___      
     /\  \         /\  \         /\__\         /\  \         /|  |     
     \:\  \       /::\  \       /:/ _/_        \:\  \       |:|  |     
      \:\  \     /:/\:\  \     /:/ /\  \        \:\  \      |:|  |     
  ___ /::\  \   /:/ /::\  \   /:/ /::\  \   ___ /::\  \   __|:|__|     
 /\  /:/\:\__\ /:/_/:/\:\__\ /:/_/:/\:\__\ /\  /:/\:\__\ /::::\__\_____
 \:\/:/  \/__/ \:\/:/  \/__/ \:\/:/ /:/  / \:\/:/  \/__/ ~~~~\::::/___/
  \::/__/       \::/__/       \::/ /:/  /   \::/__/          |:|~~|    
   \:\  \        \:\  \        \/_/:/  /     \:\  \          |:|  |    
    \:\__\        \:\__\         /:/  /       \:\__\         |:|__| {Fore.GREEN}XToolHashlibEncoding
     \/__/         \/__/         \/__/         \/__/         |/__/     

'''

#encrypto data
def encrypted (text:str ,type_hash:str)->hash:
     
     text = text.encode('utf-8')
     x = hashlib.new(type_hash)
     x.update(text)
     return x.hexdigest()
     
#For your inputs 
def main():
       print(logo)
       x = 0
       while True:
           
           Text = input(f"{Fore.RED}enter text strings ==>> ")
           
           Tipe_Hash = input(f"{Fore.BLUE} enter tipe hash ==>> ")
           if not Tipe_Hash:
               clear_sys()
               main()
           
           if Tipe_Hash == 'scrypt':
               print(f'pleas go to python.org/3/hashlib for {Fore.YELLOW}{Tipe_Hash}')
           
           elif Tipe_Hash == "pbkdf2_hmac":
               print(f'pleas go to python.org/3/hashlib for {Fore.YELLOW}{Tipe_Hash}')
                    
           else:
               hashx = encrypted(Text,Tipe_Hash)
               print(f"{Fore.RED}your text strings => {Text} ; {Fore.GREEN} Hash==> {hashx} ; {Fore.BLUE}Tipe Hash==> {Tipe_Hash} ")       
               
           x+= 1
           #for clean cmd termux shell......
           if x >= 10:
                 print(input ('click entre to clear system.'))
                 print('pleaze Wait For clearing the system.....')
                 time.sleep(2)
                 clear_sys()
                 main()
                      
#run the tool'
main()