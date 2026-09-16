while True:
    choice = int(input('Hello Welcome TO Your Future... tell us your weight please: '))
    
    if choice >= 50:
        print('bohot mote ho diting kero🐡 lagra hai ke 😋️🍔 yeh khana kaam hai tumhara sahi ka na hhahahahhaahh!!')
    elif choice >= 40:
        print('sahi hai tumhara waight zaida jio ge 👍️👏️') 
    else:
        print('yar sook gye ho thra khao piyo')
    final = input('or khelna hai (y/n): ')
    if final == 'y':
        continue
    elif final == 'n':
        print('jiska waight zaida tha voh diting kero. jiska theek hai voh aram kero. or jiska kam hai voh behosh hone se bacho!! bye...')
        break