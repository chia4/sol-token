from brownie import config as _config, network

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def config(key):
    return _config["networks"][network.show_active()][key]
