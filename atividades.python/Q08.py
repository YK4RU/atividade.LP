n = 6
print('Contagem regressiva até o fim do mundo')
import time
while 1:
    n -= 1
    print(n)
    time.sleep(1)
    if n == 0:
        break
print('*💣* o mundo acabou :)')