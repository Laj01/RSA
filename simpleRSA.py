#Táblázatos módszer
def eeucl(a, b):
    u = 0; old_u = 1
    v = 1; old_v = 0                        #v : a táblázat v sora (nem számoljuk)
    r = b; old_r = a

    while r != 0:
        q = old_r // r                      #q : hányados
        old_r, r = r, old_r - q * r         #r : maradék
        old_u, u = u, old_u - q * u         #u : táblázat u sora 

    return old_u

def modularInv(a, b):
    x = eeucl(a, b)

    if x < 0:
        x += b

    return x

def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher

def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg

def main():
    print("------------------Program start------------------- \nÜdvözlöm!")

    p = 5003
    q = 2113
    N = p * q
    fiN = (p-1) * (q-1)

    e = 7
    d = modularInv(e, fiN)

    msg = input("Titkosítani kívánt üzenet : ")

    enc = encrypt(e, N, msg)
    dec = decrypt(d, N, enc)

    print(f"Titkosított üzenet: {enc}")
    print(f"Visszafejtett üzenet: {dec}\n")
    print(f"Publikus kulcs (N): {N}")
    print(f"Publikus kulcs (e): {e}")
    print(f"Privát kulcs (fiN): {fiN}") 
    print(f"Privát kulcs (d): {d}")

main()