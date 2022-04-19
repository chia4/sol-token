from scripts.init import *
from scripts.tools import config
from brownie import interface
from colorama import Fore

dai_eth = interface.AggregatorV3Interface(config("dai_eth"))
lending_pool = interface.ILendingPool(config("lending_pool"))
weth = interface.IWETH9(config("weth_token"))
dai = interface.IERC20(config("dai_token"))


def get_weth(amount):
    weth.deposit({"amount": amount})
    print(Fore.RED + "Swapped Eth for Weth.\n")


def get_data(_print=True):
    collateral, debt, avaliable, _, _, _ = lending_pool.getUserAccountData.call(account.address)
    if _print:
        print(Fore.RED +
              f"You have deposited {collateral / 1e18:.2f} worth of Eth.\n"
              f"You have borrowed {debt / 1e18:.2f} worth of Eth.\n"
              f"You have {avaliable / 1e18:.2f} worth of Eth avaliable to borrow.\n")
    return collateral, debt, avaliable


def deposit_weth(amount):
    weth.approve(lending_pool.address, amount)
    lending_pool.deposit(weth.address, amount, account.address, 0)
    print(Fore.RED + "Deposited Weth.\n")


def lend_dai():
    _, _, avaliable = get_data(False)

    _, price, _, _, _ = dai_eth.latestRoundData.call()
    print(Fore.RED + f"Now the DAI/ETH is {price / 1e18:.8f}\n")

    lending_pool.borrow(
        config("dai_token"), avaliable / price * 0.95 * 1e18, 1, 0, account.address
    )


def repay_dai(symbol):
    pass


def main():
    get_weth(0.2e18)

    deposit_weth(0.2e18)

    get_data()

    lend_dai()

    get_data()
