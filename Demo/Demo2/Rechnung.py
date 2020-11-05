def hundert_franken_rabatt(preis)
    neuer_preis = 0

    if preis >= 100:
        neuer_preis = preis * 0.05
    else:
        neuer_preis = preis

    print (preis)