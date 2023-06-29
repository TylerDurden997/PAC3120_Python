from PAC3120 import Medidor

if __name__ == '__main__':
    pac_3120_1 = Medidor("127.0.0.1","502",1)
    print(pac_3120_1.get_active_power())
    print(pac_3120_1.get_reactive_power())
    print(pac_3120_1.get_power_factor())