from brownie import accounts as _accounts, network as _network
import os as _os
from colorama import init as _init

_DEVELOPMENT = ["development", "mainnet-fork"]

_init(autoreset=True)

if _network.show_active() in _DEVELOPMENT:
    _accounts.default = _accounts[0]
    account = _accounts[0]
else:
    _accounts.default = _accounts.add(_os.environ.get("PRIVATE_KEY"))
    account = _accounts.add(_os.environ.get("PRIVATE_KEY"))
    if _accounts.load():
        for _account in _accounts.load():
            _accounts.load(_account, "123")
