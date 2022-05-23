from hdwallet import HDWallet
from hdwallet.symbols import TRX as SYMBOL
from hexer import mHash
import requests
import json
from colorama import Fore, Style
from rich.console import Console

console = Console()

z = 1

while True:
	x = z
	block = requests.get("https://apilist.tronscan.org/api/fund?page_index=1&per_page=555")
	res = block.json()
	addr = dict(res)["data"]["data"][x]["address"]
	bal = dict(res)["data"]["data"][x]["balance"]
	mmdrza = str('[yellow]M[white]M[gold1]D[orange3]R[dark_orange3]Z[red1]A[dark_red].[red1]C[red]o[red3]M[/]')
	
	console.print(str(z) + '[blue]  Address:[white]' + str(addr) + '[/][gold1] --->[green] Balance[red1] =[white]' + str(bal) + ' | ' + str(mmdrza))
	linx = str('-[yellow]-[white]-[gold1]-[orange3]-[dark_orange3]-[red1]-[/]')
	
	console.print(linx * 11)
	z += 1
	f = open("trx.txt", "a")
	f.write('\n' + str(addr))
	f.close()
	continue
