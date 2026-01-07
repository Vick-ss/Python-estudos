import random
import time

print("Aguarde...")
time.sleep(4)
print("Pronto!")


num_aleatorio = random.randint(1, 50)
print(num_aleatorio)


while True:
    num_aleatorio = random.randint(1, 50)
    print(num_aleatorio)
    time.sleep(1)
    break


#randint pegue um num aleatório de 1 a 50

import qrcode

img = qrcode.make("https://www.linkedin.com/in/vit%C3%B3ria-de-santana-silveira-a0a7b735b/")
img.save("qr_linkdln.png")

