import random
from number_utils import * 

best = load_best('best.txt')
if best == 0:
    print('�븘吏� 理쒓퀬 湲곕줉�씠 �뾾�뒿�땲�떎.')
else:
    print('�쁽�옱 理쒓퀬 湲곕줉 :', best, '踰�')
 
answer = random.randint(1, 100)
tries = 0
while True:
    guess = get_number('1~100 �궗�씠�쓽 �닔 : ', 1, 100)
    tries += 1
    if guess < answer:
        print('UP!')
    elif guess > answer:
        print('DOWN!')
    else:
        print('�젙�떟!', tries, '踰� 留뚯뿉 留욏삍�뒿�땲�떎.')
        break
 
if best == 0 or tries < best:
    save_best('best.txt', tries)
    print('理쒓퀬 湲곕줉 媛깆떊! best.txt�뿉 ����옣�뻽�뒿�땲�떎.')
