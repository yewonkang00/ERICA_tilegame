import random
player = []
computer = []

def make_tile():
    color = {"red","orange", "blue", "black"}
    number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    tile = []
    for i in color:
        for j in number:
            ap = {'color':i, 'number':j}
            tile.append(ap)
    for i in color:
        for j in number:
            ap = {'color':i, 'number':j}
            tile.append(ap)
    random.shuffle(tile)
    return tile

def dist_tile(tile):
    for i in range(13):
        a = random.choice(tile)
        player.append(a)
        tile.remove(a)
        b = random.choice(tile)
        computer.append(b)
        tile.remove(b)

def show_tile(player):
    print("my tile is")
    for tile in player:
        print(str(tile['color']) + ' '+ str(tile['number']), end = ' ')
    print()

def show_tile(board):
    print("Register tile is")
    for tile in board:
        print(str(tile['color']) + ' ' + str(tile['number']), end = ' ')
    print()


def  more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    if answer =='y':
        return True
    else:
        return False

def register(player,tile) :
    if more("Do you want to register?(y/n) ") == True:
        answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        answer1 = int(answer1)
        sum = 0
        board = [[0 for i in range(13)]for j in range(13)]
        for i in range(answer1):
            realcard()
            for j in range(answer2):
                a,b= input().split()
                b = int(b)
                c = {'color': a, 'number': b}
                if (c in player):
                    board[i][j] = c
                    player.remove(c)
                    judge = True
                else:
                    if tile != []:
                        a = random.choice(tile)
                        player.append(a)
                        tile.remove(a)
                        show_tile(player)
                    else:
                        print("There are no tiles")
                    judge = False
                    break
        row = len(board)
        col = len(board[0])       
        a = []
        for i in range(row):
            for j in range(col):
                if (board[i][j] != 0):
                    a.append(board[i][j])
        for i in range(len(a)):
            sum += a[i]['number']
        if (judge == True):
            if (sum <= 30):
                print("Sum is not over 30")
                print("You get 1 tile.")
                emptytile()
            else:
                print("You success to register.")
    else :
        print("You get 1 tile.")
        emptytile()

def realcard():
    answer2 = input("How many tiles do you want to enter?")
    answer2 = int(answer2)
    print("Please enter tiles")
    card = []
    card = input()
    if (card in player):
        pass
    else:
        print("This tile is not yours")
        print("You get 1 tile")

def emptytile():
    if tile != []:
        a = random.choice(tile)
        player.append(a)
        tile.remove(a)
        show_tile(player)
    else:
        print("There are no tile.")

def arrange_tile(player):
    answer = input("Do you want sort? (789/777/NO)")
    while not (answer == '789' or answer == '777' or answer == 'NO') :
        answer == input("Do you want sort? (789/777/NO)")
    if answer == '777':
        player.sort(key=lambda x: x['number'])
    elif answer == '789':
        player.sort(key=lambda x: (x['color'], x['number']))

def tilegame():
    tile = make_tile()
    dist_tile(tile)
    show_tile(player)
    arrange_tile(player)
    show_tile(player)
    register(player,tile)

tilegame()

