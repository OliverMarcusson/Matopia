import random
import os

def main():
    names = ['Alfons', 'Fred', 'Sackarias', 'Hoppe', 'Noah', 'Johan', 'Oliver']

    rand_name = random.randint(0, len(names) -1)
    
    size = random.randint(1, 30)

    if rand_name == 5:
        size = random.randint(1, 5)

    if rand_name == 2 or rand_name == 6:
        size = random.randint(200, 300)
        
    os.system('cls')

    if rand_name == 3 or rand_name == 4:
        print(f'{names[rand_name]} har en kuk som är {str(size)} mm lång. Stackars tjejen.')
    else:
        print(f'{names[rand_name]} har en kuk som är {str(size)} mm lång. Fyfan.')

if __name__ == '__main__':
    main()