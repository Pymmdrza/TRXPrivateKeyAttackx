import time
from rich.console import Console
from hexer import mHash
import logging
from tronapi import Tron
from hexer import mHash


sp = input('Insert Speed Number Here (float or int) : ')
xHash = mHash()
console = Console()

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io/'

z = 0
w = 0
while True:
    private_key = str(xHash)
    
    tron = Tron(full_node=full_node,
                solidity_node=solidity_node,
                event_server=event_server)
    
    account = tron.create_account
    is_valid = bool(tron.isAddress(account.address.hex))
    addr = account.address.base58
    priv = account.private_key
    mmdrza = str('[yellow]M[white]M[gold1]D[orange3]R[dark_orange3]Z[red1]A[dark_red].[red1]C[red]o[red3]M[/]')
    console.print('[black on gold1]'+str(z)+'[/] | [white on blue]Addr:[/][white on red1]'+str(addr)+'[/] | [white on blue]Priv:[/][white on dark_green]'+str(priv)+'[/][green] [isValid]=>[white]'+str(is_valid)+'[/] | '+str(mmdrza)+'[/]')
    time.sleep(float(sp))
    linx = str('-[yellow]-[white]-[gold1]-[orange3]-[dark_orange3]-[red1]-[/]')
    
    console.print(linx*18)
    z += 1
    
