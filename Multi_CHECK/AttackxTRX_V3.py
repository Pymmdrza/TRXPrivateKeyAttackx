from rich.console import Console
from tronapi import Tron
from hexer import mHash

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io/'


console = Console()

filename = 'trx.txt'
with open(filename) as f:
    add = f.read().split()
add = set(add)

z = 0
w = 0
while True:
    xHash = mHash()
    private_key = str(xHash)
    
    tron = Tron(full_node=full_node,
                solidity_node=solidity_node,
                event_server=event_server)
    
    account = tron.create_account
    is_valid = bool(tron.isAddress(account.address.hex))
    addr = account.address.base58
    priv = account.private_key
    mmdrza = str('[yellow]M[white]M[gold1]D[orange3]R[dark_orange3]Z[red1]A[dark_red].[red1]C[red]o[red3]M[/]')
    if addr in add:
        w += 1
        console.print('[white on blue] Winnig Wallet Tron Details Saved On text File : Address:[white on red]' + str(addr) + '[/]')
        f = open("WinWallet__TRON-MMdrza.txt", "a")
        f.write('\n' + str(addr))
        f.write('\n' + str(priv))
        f.write('\n=================[Mmdrza.Com]===================\n')
        f.close()
       
        z += 1
    else:
        console.print('[black on gold1]' + str(z) + '[/][white] --- Win:' + str(w) + '[/] --- | [white on blue]Addr:[/][white on red1]' + str(addr) + '[/] | [white on blue]Priv:[/][white on dark_green]' + str(priv) + '[/][green] [isValid]=>[white]' + str(is_valid) + '[/] | ' + str(mmdrza) + '[/]')
        linx = str('-[yellow]-[white]-[gold1]-[orange3]-[dark_orange3]-[red1]-[/]')
        console.print(linx * 18)
        z += 1
        continue
