import unittest


def BalancedAB(st):
    endString = end = len(st)
    if(st.find("A") == -1):
        if(st.find("B") == -1):
            return True
        if(st.find("B") != -1):
            return True
    else:
        locationA = st.rindex("A", 0, endString)
        locationB = st.rindex("B", 0, endString)
        if(locationB > locationA):
            return True
        elif(locationB < locationA):
            return False


class TestBalancedAB(unittest.TestCase):
    def test_BalancedAB1(self):
        self.assertTrue(challenge.BalancedAB("AAZZBB"))
        self.assertTrue(challenge.BalancedAB("AAAXXXXYB"))
        self.assertFalse(challenge.BalancedAB("BBYYYXXXAXX"))
        self.assertTrue(challenge.BalancedAB(""))
        self.assertTrue(challenge.BalancedAB("XXXXXYYYYZZZZB"))
        self.assertTrue(challenge.BalancedAB("    XXXXXYYYYZZZZ"))
        self.assertTrue(challenge.BalancedAB("XXXXX   YYYY   ZZZZB"))
        self.assertFalse(challenge.BalancedAB("YYYBABYYYXXXAXX"))
        self.assertFalse(challenge.BalancedAB("ABABABA"))


if __name__ == '__main__':
    unittest.main()
