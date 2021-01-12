

def solve1(a, b, c):
    """Rozwiązanie równania liniowego a x + b y + c = 0"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Parametry muszą być liczbami")

    if a == 0 and b == 0:
        # jeśli 'a' i 'b' są zerami, a 'c' jest różne od zera, to równanie jest speczne (np. 4 = 0 jest sprzeczne)
        if c != 0:
            print("Równanie jest sprzeczne")
            return
        # gdy wszystkie trzy parametry są zerami dostajemy 0 = 0, równanie opisuje całą płaszczyznę (jest postaci 0 = 0, zawsze prawdziwe)
        else:
            print("Równanie opisuje całą powierzchnię, jest zawsze prawidzwe")
            return
    # gdy żadne z powyższych nie zachodzi, to równanie opisuje prostą 
    # jeśli b jest różne od zera, możemy przez nie podzielić i otrzymać prostą w postaci y = ...
    if b != 0:
        a1 = -(a/b)
        c1 = -(c/b)
        print(f"Równanie opisuje prostą postaci: y = ({a1})x + ({c1})")
        return
    # jeśli b jest zerem, to równanie przyjmie postać x = ...
    elif b == 0:
        c1 = -(c/a)
        print(f"Równanie opisuje prostą postaci: x = {c1}")
        return


if __name__ == "__main__":
    solve1(1, 2, 3)         # Równanie opisuje prostą postaci: y = (-0.5)x + (-1.5)
    solve1(0, 2, 3)         # Równanie opisuje prostą postaci: y = (-0.0)x + (-1.5)
    solve1(1, 0, 3)         # Równanie opisuje prostą postaci: x = -3.0
    solve1(1, 2, 0)         # Równanie opisuje prostą postaci: y = (-0.5)x + (-0.0)
    solve1(0, 0, 3)         # Równanie jest sprzeczne
    solve1(0, 0, 0)         # Równanie opisuje całą powierzchnię, jest zawsze prawidzwe
