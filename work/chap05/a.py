def countdown(start):
    print('関数が受け取った値:',start)
    print('カウントダウンします')
    counter=start
    while counter >= 0:
        print(counter)
        count -= 1
        
countdown(3)
countdown(10)
