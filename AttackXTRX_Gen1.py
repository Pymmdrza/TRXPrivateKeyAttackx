import time
from hexer import mHash
import logging
from tronapi import Tron
from hexer import mHash

xHash = mHash()
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
    print(str(z)+' - Addr:'+str(addr)+'\nPriv:'+str(priv)+' [isValid]=>'+str(is_valid))
    time.sleep(0.1)
    print('------------------------[ M m d r z a . C o M ]-----------------------------')
    z += 1
    
