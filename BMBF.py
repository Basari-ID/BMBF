import time,os
from rich.panel import Panel as ganteng
from rich import print as basari
try:
	warna_kolor = "#00C8FF"
except FileNotFoundError:
	warna_kolor = "#00C8FF"
os.system('clear')
basari(ganteng(f'[bold green] mohon maaf bagi para pengguna script bmbf karena script ini\n tidak bisa digunakan untuk sementara waktu tolong dimaafkan',width=70,title=f"[bold white] ◇ PEMBERITAHUAN ◇ ",style=f"{warna_kolor}"))
time.sleep(4)
exit()
