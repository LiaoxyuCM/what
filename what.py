import webbrowser,sys,time,random
#PLEASE DON'T F**K THIS. BECAUSE THIS MODULE'S AUTHER IS STUDENT. MAKING IS NOT EASY. LIKE=UPDATE

def version():
    print('Module what  --version 0.7.6 (beta)')

def Update_content():
    print('0.7.6 Update content\nRepair : --rock-paper scissors bug')

def statement():
    print("PLEASE DON'T F**K THIS. BECAUSE THIS MODULE'S AUTHER IS STUDENT. MAKING IS NOT EASY. LIKE=UPDATE")

def ChineseAI():
    print('AI:'+input("我:").strip('吗？?')+'!')

def xPrint(i,num1):
    if isinstance(num1, (int, float)):
        for count in range(num1):
            print(i)
    else:
        print('what.xPrint(1,2) but second text should is number')

def BaiduSearth(word):
    webbrowser.open(f'https://www.baidu.com/s?ie=utf-8&word={word}')

def BilibiliSearth(bbs):
    webbrowser.open(f'https://search.bilibili.com/all?keyword={bbs}')

def BilibiliVideo(bbvc):
    webbrowser.open(f'https://www.bilibili.com/video/{bbvc}')

def SystemIf(system):
    if sys.platform == system:
        return True
    else:
        return False

def unix_time():
    return int(time.time())

def calc():
    string = input("calc>")
    try:
        num = eval(string)
    except:
        num = "Not a real equation"
    print(num)

def text(txt):
    return txt

def rock_paper_scissors():
    d= {
        0: "rock",
        1: "paper",
        2: "scissors"
    }
    scorepc = 0
    scoremy = 0
    scoretie = 0
    def pc():
        num = random.randint(0, 2)
        return d[num]
    print('rock-paper-scissors Winning and losing principle:\n'
          + "paper    vs rock     -> “paper”   win\n"
          + "rock     vs scissors -> “rock”    win\n"
          + "scissors vs paper    -> “scissors”win\n")
    print("You can select: \n 1 - rock \n 2 - paper \n 3 - scissors \n")
    while True:
        xuan=str(input("Please enter your select , enter other string to quit: "))
        if xuan == '1' or xuan == 'rock':
            player= 'rock'
        elif xuan == '2' or xuan == 'paper':
            player= 'paper'
        elif xuan == '3' or xuan == 'scissors':
            player= 'scissors'
        else:
            break
        computer=pc()
        if player == computer:
            print(f"Tie! you select {player} , computer select {computer}")
            scoretie += 1
        elif player == "rock" and computer == "paper":
            print(f"Computer win! you select {player} computer select {computer}")
            scorepc += 1
        elif player == "rock" and computer == "scissors":
            print(f"You win! you select {player} computer select {computer}")
            scoremy += 1
        elif player == "paper" and computer == "rock":
            print(f"You win! you select {player} computer select {computer}")
            scoremy += 1
        elif player == "paper" and computer == "scissors":
            print(f"Computer win! you select {player} computer select {computer}")
            scorepc += 1
        elif player == "scissors" and computer == "rock":
            print(f"Computer win! you select {player} computer select {computer}")
            scorepc += 1
        elif player == "scissors" and computer == "paper":
            print(f"You win! you select {player} computer select {computer}")
            scoremy += 1
    print("Game over! You win ",scoremy," times, Computer win ",scorepc," times, Tie: ",scoretie)

def Tic_Tac_Toe():
    board = [' ' for x in range(10)]
    def insert_letter(letter, pos):
        board[pos] = letter
    def space_is_free(pos):
        return board[pos] == ' '
    def print_board(board):
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
    def is_winner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)
    def player_move():
        run = True
        while run:
            move = input("Select a location(1-9):")
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if space_is_free(move):
                        run = False
                        insert_letter('X', move)
                    else:
                        print("This location has been occupied!")
                else:
                    print("Please enter the correct number!")
            except:
                print("Please enter the number!")
    def comp_move():
        possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0
        for let in ['O', 'X']:
            for i in possible_moves:
                board_copy = board[:]
                board_copy[i] = let
                if is_winner(board_copy, let):
                    move = i
                    return move
        corners_open = []
        for i in possible_moves:
            if i in [1, 3, 7, 9]:
                corners_open.append(i)
        if len(corners_open) > 0:
            move = select_random(corners_open)
            return move
        if 5 in possible_moves:
            move = 5
            return move
        edges_open = []
        for i in possible_moves:
            if i in [2, 4, 6, 8]:
                edges_open.append(i)
        if len(edges_open) > 0:
            move = select_random(edges_open)
        return move
    def select_random(li):
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]
    def is_board_full(board):
        if board.count(' ') > 1:
            return False
        else:
            return True
    def main():
        print_board(board)
        while not (is_board_full(board)):
            if not (is_winner(board, 'O')):
                player_move()
                print_board(board)
            else:
                print("Sorry, you lose!")
                break
            if not (is_winner(board, 'X')):
                move = comp_move()
                if move == 0:
                    print("Tie!")
                else:
                    insert_letter('O', move)
                    print("Computer in", move, "Got an O:")
                    print_board(board)
            else:
                print("Congratulations, you win!")
                break
        if is_board_full(board):
            print("Tie!")
    main()

def gameSelect():
    a = str(input('Please select a game , enter game code\ncode : name\n1    : rock-paper-scissors\n2    : Tic-Tac-Toe\nother: Quit\nenter: '))
    if a == '1':
        rock_paper_scissors()
    elif a == '2':
        Tic_Tac_Toe()
    else:
        pass

def draw_for_a_prize():
    a = str(input("Select a number(1-10) :"))
    b = str(random.randint(1,10))
    c = str(random.randint(1,10))
    if a == b or a == c:
        print(f'Congratulations, you draw a prize-winning ticket in a lottery\nPrize number : {b} , {c}')
    else:
        print(f'Sorry, you draw a prize-losing ticket in a lottery\nPrize number : {b} , {c}')

def aJoke():
    d = str(input('Is this program running? \n1 : Yes\n2 : no \nother : quit\nenter number:'))
    if d == '1':
        print('As it turns out, this program has been opened.')
    elif d == '2':
        print('Then how did you open this program?')
    else:
        pass