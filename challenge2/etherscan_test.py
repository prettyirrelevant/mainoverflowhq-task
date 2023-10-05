import unittest
from .etherscan import print_transfers


class EtherscanTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tx_hash1 = '0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263'
        self.tx_hash2 = '0xc56a6d18907abc69f2f4557c8c5eef248f72659b8f449cdc78b3ed8b8a49c4e1'
        self.tx_hash3 = '0x4e9afd5052f75bfbef6c41f80ac1983ba345b2bb2ef025e9cdee07d471d90983'

        self.tx_hash1_result = [
            {
                'from': '0x3fc91a3afd70395cd496c647d5a6cc9d4b2b7fad',
                'to': '0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc',
                'amount': 49999900000000000,
            },
            {
                'from': '0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc',
                'to': '0x7c0b8a9716a00f8d13514c50e1282947dda5c395',
                'amount': 82212970,
            },
        ]
        self.tx_hash2_result = [
            {
                'from': '0xf52a212f746d1fed88d39d679f803bc473949d5f',
                'to': '0x74de5d4fcbf63e00296fd95d33236b9794016631',
                'amount': 2000000000000000000000,
            },
            {
                'from': '0x74de5d4fcbf63e00296fd95d33236b9794016631',
                'to': '0x47082a75bc16313ef92cfaca1feb885659c3c9b5',
                'amount': 2000000000000000000000,
            },
            {
                'amount': 18659286377218614,
                'to': '0x1111111254eeb25477b68fb85ed929f73a960582',
                'from': '0x47082a75bc16313ef92cfaca1feb885659c3c9b5',
            }
        ]
        self.tx_hash3_result = [
            {
                'from': '0x1bb76ed03299eccc507ad03e26435c6cb1cbd86a',
                'to': '0x9bed573a761c76a860a5712935c1c9b805a29327',
                'amount': 90220000,
            }
        ]

        self.etherscan_api_key = 'ZYYTNKHV2GQV6VPYVUF6Y1EMMU11NR7B4X'

    def test_print_transfers(self):
        self.assertEqual(print_transfers(self.tx_hash1, self.etherscan_api_key), self.tx_hash1_result)
        self.assertEqual(print_transfers(self.tx_hash2, self.etherscan_api_key), self.tx_hash2_result)
        self.assertEqual(print_transfers(self.tx_hash3, self.etherscan_api_key), self.tx_hash3_result)
