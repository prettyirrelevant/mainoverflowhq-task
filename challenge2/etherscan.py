import urllib.request
import json

TRANSFER_TOPIC = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'


def print_transfers(tx_hash: str, api_key: str):
    transfers = []

    url = f'https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={tx_hash}&apikey={api_key}'
    response = urllib.request.urlopen(url, timeout=10)
    json_data = json.loads(response.read())

    if 'result' not in json_data:
        return transfers

    for log in json_data['result']['logs']:
        if log['topics'][0] != TRANSFER_TOPIC:
            continue

        transfers.append({
            'amount': hexstr_to_int(log['data']),
            'to': hexstr_to_address(log['topics'][2]),
            'from': hexstr_to_address(log['topics'][1]),
        })

    return transfers


def hexstr_to_address(hexstr: str) -> str:
    hexstr = hexstr.removeprefix('0x')
    return f'0x{hexstr[24:]}'


def hexstr_to_int(hexstr: str) -> int:
    hexstr = hexstr.removeprefix('0x')
    int_value = int(hexstr, 16)
    return int_value

