import re
from typing import Any, Dict

from bs4 import BeautifulSoup
import requests

ETHERSCAN_CONTRACT_URL = 'https://etherscan.io/token/{address}'
ETHERSCAN_ADDRESS_URL = 'https://etherscan.io/address/{address}'
ETHERSCAN_TRANSACTION_URL = 'https://etherscan.io/tx/{tx}'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def fetch_asset_information(asset_id: str) -> Dict[str, Any]:
    r = requests.get(f'https://api.coingecko.com/api/v3/coins/{asset_id}')
    data = r.json()

    if 'ethereum' in data["platforms"]:
        contract_addr = data['platforms']['ethereum']
        return {'contract': contract_addr}

def fech_etherscan_info(address: str):
    html = requests.get(ETHERSCAN_CONTRACT_URL.format(address=address), headers=headers).text
    soup = BeautifulSoup(html, features="html.parser")
    print(soup.findAll('div', text = re.compile('Decimals:')))
    print(soup.findAll('div', text = re.compile('Decimals:'))[0].findNext('div').text.strip())

if __name__ == '__main__':
    fech_etherscan_info('0x1f9840a85d5af5bf1d1762f925bdaddc4201f984')