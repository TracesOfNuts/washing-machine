import unittest
from washing_machine import WashingMachine, WashType, Coin

class TestWashingMachine(unittest.TestCase):
    def setUp(self):
        self.wm = WashingMachine()

    def test_accept_coins(self):
        coins = [Coin(10), Coin(20), Coin(50), Coin(100)]
        for coin in coins:
            initial_balance = self.wm.total_credited
            self.wm.accept_coin(coin)
            self.assertEqual(self.wm.total_credited, initial_balance + coin.value)
        self.assertEqual(self.wm.coins_credited["10-cent"], 1)
        self.assertEqual(self.wm.coins_credited["20-cent"], 1)
        self.assertEqual(self.wm.coins_credited["50-cent"], 1)
        self.assertEqual(self.wm.coins_credited["1-dollar"], 1)

    def test_accept_invalid_coin(self):
        with self.assertRaises(ValueError):
            coin = Coin(5)
            self.wm.accept_coin(coin)

    def test_select_quick_wash(self):
        wash_type = "Quick"
        coins = [Coin(10) for _ in range(20)]  # 2 dollars
        for coin in coins:
            self.wm.accept_coin(coin)
        is_selected = self.wm.select_wash_type(wash_type)
        self.assertTrue(is_selected)
        self.assertEqual(self.wm.current_wash_type, self.wm.wash_types[wash_type])

    def test_select_mild_wash(self):
        wash_type = "Mild"
        coins = [Coin(50) for _ in range(5)] # 2.5 dollars
        for coin in coins:
            self.wm.accept_coin(coin)
        is_selected = self.wm.select_wash_type(wash_type)
        self.assertTrue(is_selected)
        self.assertEqual(self.wm.current_wash_type, self.wm.wash_types[wash_type])

    def test_select_medium_wash(self):
        wash_type = "Medium"
        coins = [Coin(20) for _ in range(21)]  # 4.2 dollars
        for coin in coins:
            self.wm.accept_coin(coin)
        is_selected = self.wm.select_wash_type(wash_type)
        self.assertTrue(is_selected)
        self.assertEqual(self.wm.current_wash_type, self.wm.wash_types[wash_type])

    def test_select_heavy_wash(self):
        wash_type = "Heavy"
        coins = [Coin(100) for _ in range(6)] # 6 dollars
        for coin in coins:
            self.wm.accept_coin(coin)
        is_selected = self.wm.select_wash_type(wash_type)
        self.assertTrue(is_selected)
        self.assertEqual(self.wm.current_wash_type, self.wm.wash_types[wash_type])
        
    def test_select_wash_type_insufficient_funds(self):
        wash_type = "Heavy"
        coin = Coin(10)
        self.wm.accept_coin(coin)
        is_selected = self.wm.select_wash_type(wash_type)
        self.assertFalse(is_selected)

    def test_select_invalid_wash_type(self):
        wash_type = "Invalid"
        with self.assertRaises(ValueError):
            self.wm.select_wash_type(wash_type)

    def test_refund(self):
        self.wm.accept_coin(Coin(50))
        self.wm.accept_coin(Coin(100))
        self.wm.refund()
        self.assertEqual(self.wm.total_credited, 0)

    def test_start_quick_wash(self):
        wash_type = "Quick"
        coins = [Coin(10) for _ in range(20)]  # 2 dollars
        for coin in coins:
            self.wm.accept_coin(coin)
        self.wm.select_wash_type(wash_type)
        self.wm.start_wash()
        self.assertEqual(self.wm.total_earned, self.wm.wash_types[self.wash_type_index].cost)
        self.assertEqual(self.wm.total_time_on, self.wm.wash_types[self.wash_type_index].duration)

    

    def test_display_statistics(self):
        self.wm.display_statistics()  # Just calling to ensure no exceptions are raised

    def test_reset_statistics(self):
        wash_type = "Quick"
        coins = [Coin(20) for _ in range(20)]
        for coin in coins:
            self.wm.accept_coin(coin)
        self.wm.select_wash_type(wash_type)
        self.wm.start_wash()
        self.wm.reset_statistics()
        self.assertEqual(self.wm.total_time_on, 0)
        self.assertEqual(self.wm.total_earned, 0)

if __name__ == "__main__":
    unittest.main()