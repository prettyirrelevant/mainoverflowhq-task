import unittest

from .network_failure_point import Network, identify_router


class NetworkFailurePointTest(unittest.TestCase):
    def setUp(self) -> None:
        self.network_1 = Network()
        self.network_1.add_connection(1, 2)
        self.network_1.add_connection(2, 3)
        self.network_1.add_connection(3, 5)
        self.network_1.add_connection(5, 2)
        self.network_1.add_connection(2, 1)

        self.network_2 = Network()
        self.network_2.add_connection(1, 3)
        self.network_2.add_connection(3, 5)
        self.network_2.add_connection(5, 6)
        self.network_2.add_connection(6, 4)
        self.network_2.add_connection(4, 5)
        self.network_2.add_connection(5, 2)
        self.network_2.add_connection(2, 6)

        self.network_3 = Network()
        self.network_3.add_connection(2, 4)
        self.network_3.add_connection(4, 6)
        self.network_3.add_connection(6, 2)
        self.network_3.add_connection(2, 5)
        self.network_3.add_connection(5, 6)

    def test_identify_router(self) -> None:
        self.assertEqual(identify_router(self.network_1), [2])
        self.assertEqual(identify_router(self.network_2), [5])
        self.assertEqual(identify_router(self.network_3), [2, 6])
