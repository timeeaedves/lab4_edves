try:
    # 1. Citirea din fisier
    f = open("lab4.txt", "r")
    # am folosit readline pentru a citi de pe fiecare linie
    # asa fiecare variabila va avea cate un numar din fisier
    s1 = f.readline()
    s2 = f.readline()
    f.close()

    # Curatare primitiva de caractere invizibile / sfarsit de rand (\n, spatii)
    curat1 = ""
    for ch in s1:
        if ch >= "0" and ch <= "9":
            curat1 = curat1 + ch
    s1 = curat1

    curat2 = ""
    for ch in s2:
        if ch >= "0" and ch <= "9":
            curat2 = curat2 + ch
    s2 = curat2

    # Eliminare zerouri de la inceput (ex: "005" -> "5")
    i = 0
    # len - lungimea unui sir de caractere
    # sir[0] - prima pozitie dintr-un sir de caractere
    # s1[i:] - taie sirul de caractere de la pozitia i
    # ex din 0503 va rezulta 503
    while i < len(s1) - 1 and s1[i] == "0":
        i = i + 1
    s1 = s1[i:]

    i = 0
    while i < len(s2) - 1 and s2[i] == "0":
        i = i + 1
    s2 = s2[i:]

    # 2. Adunare cifra cu cifra (de la coada la cap)
    i = len(s1) - 1
    j = len(s2) - 1
    transport = 0
    suma = "" # acesta este definit ca un sir de caractere

    while i >= 0 or j >= 0 or transport > 0:
        if i >= 0:
            c1 = int(s1[i])
        else:
            c1 = 0

        if j >= 0:
            c2 = int(s2[j])
        else:
            c2 = 0

        total = c1 + c2 + transport
        cifra = total % 10
        transport = total // 10

        suma = str(cifra) + suma
        i = i - 1
        j = j - 1

    # 3. Inmultire in coloana
    if s1 == "0" or s2 == "0":
        produs = "0"
    else:
        produs = "0"
        zerouri = ""

        j = len(s2) - 1
        while j >= 0:
            c2 = int(s2[j])

            i = len(s1) - 1
            transport = 0
            rand = ""

            # Inmultim s1 cu o singura cifra c2
            while i >= 0 or transport > 0:
                if i >= 0:
                    c1 = int(s1[i])
                else:
                    c1 = 0

                p = c1 * c2 + transport
                cifra = p % 10
                transport = p // 10

                rand = str(cifra) + rand
                i = i - 1

            # Decalam randul cu zerouri
            rand = rand + zerouri

            # Adunam randul la produsul total
            u1 = len(produs) - 1
            u2 = len(rand) - 1
            t_adunare = 0
            nou_produs = ""

            while u1 >= 0 or u2 >= 0 or t_adunare > 0:
                if u1 >= 0:
                    d1 = int(produs[u1])
                else:
                    d1 = 0

                if u2 >= 0:
                    d2 = int(rand[u2])
                else:
                    d2 = 0

                tot = d1 + d2 + t_adunare
                nou_produs = str(tot % 10) + nou_produs
                t_adunare = tot // 10

                u1 = u1 - 1
                u2 = u2 - 1

            produs = nou_produs
            zerouri = zerouri + "0"
            j = j - 1

    # Afisare rezultate
    print("Numerele citite:")
    print("a =", s1)
    print("b =", s2)
    print("Suma =", suma)
    print("Produs =", produs)

except:
    print("Fisierul nu exista")