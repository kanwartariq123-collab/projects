while True:
    intro = str(input('Hello this is a pakistani finder game do you want to play (y/n): '))
    
    if intro == 'n':
        print('ok bye')
        break
        
    elif intro == 'y':
        q1 = str(input('do you like desi khana or not (yes/no): '))
        if q1 == 'yes':
            q2 = str(input('do you like old punjabi songs (yes/no): '))
            if q2 == 'yes':
                q3 = input('do you like suit or pant shirts (a/b): ')
                if q3 == 'a':
                    q4 = input('do you like dollars or orange wale baba ji (a/b): ')
                    if q4 == 'b':
                        print('🎉 You are Pakistani!')
                    else:
                        print('❌ You are not a Pakistani!')
                else:
                    print('❌ You are not a Pakistani!')
            else:
                print('❌ You are not a Pakistani!')
        else:
            print('❌ You are not a Pakistani!')
            
        a = input('want to play again (y/n): ')
        if a == 'n':
            print('ok bye bye')
            break  
        elif a == 'y':
            continue