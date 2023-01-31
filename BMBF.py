import time
from rich.panel import Panel as basari
from rich import print as ganteng
try:
	warna_kolor = "#00C8FF"
except FileNotFoundError:
	warna_kolor = "#00C8FF"
ganteng(basari(f'[bold green] mohon maaf bagi para pengguna script bmbf karena script ini\n tidak bisa digunakan untuk sementara waktu tolong dimaafkan',width=70,title=f"[bold white] ◇ PEMBERITAHUAN ◇ ",style=f"{warna_kolor}"))
time.sleep(2)
exit()
