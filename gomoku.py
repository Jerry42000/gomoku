

def is_empty(board):
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] != " ":
                return False
    return True

def is_subsequence(board,y_end,x_end,length,d_y,d_x):
    col = board[y_end][x_end]
    if d_y == 0 and d_x == 1:
        if x_end+1 == 8 and x_end-(length-1) == 0:
            return False
        elif x_end+1 == 8:
            if board[y_end][x_end-length] == col:
                return True
        elif x_end-(length-1) == 0:
            if board[y_end][x_end+1] == col:
                return True
        else:
            if board[y_end][x_end - length] == col or board[y_end][x_end+1] == col:
                return True
        return False
    if d_y == 1 and d_x == 0:
        if y_end+1 == 8 and y_end-(length-1) == 0:
            return False
        elif y_end+1 == 8:
            if board[y_end - length][x_end] == col:
                return True
        elif y_end-(length-1) == 0:
            if board[y_end+1][x_end] == col:
                return True
        else:
            if board[y_end - length][x_end] == col or board[y_end+1][x_end] == col:
                return True
        return False
    if d_y == 1 and d_x == 1:
        if (y_end + 1 == 8 or x_end + 1 == 8) and (y_end-(length-1)==0  or x_end-(length-1)==0):
            return False
        elif y_end + 1 == 8 or x_end + 1 == 8:
            if board[y_end - length][x_end - length] == col:
                return True
        elif y_end-(length-1)==0  or x_end-(length-1)==0:
            if board[y_end+1][x_end+1] == col:
                return True
        else:
            if board[y_end - length][x_end - length] == col or board[y_end+1][x_end+1] == col:
                return True
        return False
    if d_y == 1 and d_x == -1:
        if (y_end+1 == 8 or x_end ==0) and (y_end-(length-1)==0 or x_end+(length-1)==7):
            return False
        elif y_end+1 == 8 or x_end ==0:
            if board[y_end-length][x_end+length] == col:
                return True
        elif y_end-(length-1)==0 or x_end+(length-1)==7:
            if board[y_end+1][x_end-1] == col:
                return True
        else:
            if board[y_end - length][x_end + length] == col or board[y_end+1][x_end-1] == col:
                return True
        return False



def is_bounded(board, y_end, x_end, length, d_y, d_x):
    num = 0
    if is_subsequence(board, y_end, x_end, length, d_y, d_x):
        return "SUBSEQUENCE"
    if d_y == 0 and d_x == 1:
        if x_end+1 == 8 or (board[y_end][x_end+1] !=" "):
            num+=1
        if x_end-(length-1)==0 or (board[y_end][x_end-length] !=" "):
            num+=1
        if num == 0:
            return "OPEN"
        elif num == 1:
            return "SEMIOPEN"
        else:
            return "CLOSED"
    if d_y == 1 and d_x == 0:
            if y_end+1 == 8 or (board[y_end+1][x_end] !=" "):
                num+=1
            if y_end-(length-1)==0 or (board[y_end-length][x_end] !=" "):
                num+=1
            if num == 0:
                return "OPEN"
            elif num == 1:
                return "SEMIOPEN"
            else:
                return "CLOSED"
    if d_y == 1 and d_x == 1:
        if y_end+1 == 8 or x_end+1==8 or (board[y_end+1][x_end+1] !=" "):
            num+=1
        if y_end-(length-1)==0  or x_end-(length-1)==0 or (board[y_end-length][x_end-length] !=" "):
            num+=1
        if num == 0:
            return "OPEN"
        elif num == 1:
            return "SEMIOPEN"
        else:
            return "CLOSED"
    if d_y == 1 and d_x == -1:
        if y_end+1 == 8 or x_end ==0 or (board[y_end+1][x_end-1]!=" "):
            num+=1
        if y_end-(length-1)==0 or x_end+(length-1)==7 or(board[y_end-length][x_end+length]!=" "):
            num+=1
        if num == 0:
            return "OPEN"
        elif num == 1:
            return "SEMIOPEN"
        else:
            return "CLOSED"


def has_five_in_a_row(board, color):
    size = len(board)
    target = 5

    for y in range(size):
        for x in range(size):
            if x <= size-target and all(board[y][x+i] == color for i in range(target)):
                return True
            if y <= size-target and all(board[y+i][x] == color for i in range(target)):
                return True
            if x <= size-target and y <= size - target and all(board[y+i][x+i] == color for i in range(target)):
                return True
            if x >= target-1 and y <= size - target and all(board[y+i][x-i] == color for i in range(target)):
                return True

    return False


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0
    reached = 0
    if d_y == 0 and d_x == 1:
        i = 0
        consec = -1
        for j in range(0,8):
            if board[y_start][x_start+j] == col:
                i+=1
                consec+=1
            else:
                i = 0
                consec+=1
            if i == length:
                reached += 1
                if is_bounded(board, y_start, x_start+consec, length, d_y, d_x) == "OPEN":
                    open_seq_count += 1
                elif is_bounded(board, y_start, x_start+consec, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
    if d_y == 1 and d_x == 0:
        i = 0
        consec = -1
        for j in range(0,8):
            if board[y_start+j][x_start] == col:
                i+=1
                consec+=1
            else:
                i=0
                consec+=1
            if i == length:
                reached += 1
                if is_bounded(board, y_start+consec, x_start, length, d_y, d_x) == "OPEN":
                    open_seq_count += 1
                elif is_bounded(board, y_start+consec, x_start, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
    if d_y == 1 and d_x == 1:
        i = 0
        consec = -1
        for j in range(0,8):
            if y_start+j >= 8 or x_start+j >= 8:
                break
            if board[y_start+j][x_start+j] == col:
                i+=1
                consec+=1
            else:
                i=0
                consec+=1
            if i == length:
                reached+= 1
                if is_bounded(board, y_start+consec, x_start+consec, length, d_y, d_x) == "OPEN":
                    open_seq_count += 1
                elif is_bounded(board, y_start+consec, x_start+consec, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
    if d_y == 1 and d_x == -1:
        i = 0
        consec = -1
        for j in range(0,8):
            if y_start+j >= 8 or x_start-j <= -1:
                break
            if board[y_start+j][x_start-j] == col:
                i+=1
                consec+=1
            else:
                i=0
                consec+=1
            if i == length:
                reached += 1
                if is_bounded(board, y_start+consec, x_start-consec, length, d_y, d_x) == "OPEN":
                    open_seq_count += 1
                elif is_bounded(board, y_start+consec, x_start-consec, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1




    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(0,8):
        open_seq_count += detect_row(board, col, i,0, length, 0, 1)[0]
        semi_open_seq_count += detect_row(board, col, i,0, length, 0, 1)[1]
    for i in range(0,8):
        open_seq_count += detect_row(board, col, 0,i, length, 1, 0)[0]
        semi_open_seq_count += detect_row(board, col, 0,i, length, 1, 0)[1]
    for i in range(0,8):
        open_seq_count += detect_row(board, col, 0,i, length, 1, 1)[0]
        semi_open_seq_count += detect_row(board, col, 0,i, length, 1, 1)[1]
    for i in range(1, 8):
        open_seq_count += detect_row(board, col, i,0, length, 1, 1)[0]
        semi_open_seq_count += detect_row(board, col, i,0, length, 1, 1)[1]
    for i in range(0, 8):
        open_seq_count += detect_row(board, col, 0,i, length, 1, -1)[0]
        semi_open_seq_count += detect_row(board, col, 0,i, length, 1, -1)[1]
    for i in range(1,8):
        open_seq_count += detect_row(board, col, i,7, length, 1, -1)[0]
        semi_open_seq_count += detect_row(board, col, i,7, length, 1, -1)[1]
    return (open_seq_count, semi_open_seq_count)


def search_max(board):
    maxscore = -10000
    move_y = 0
    move_x = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == " ":
                board[i][j] = "b"
                if score(board)>maxscore:
                    maxscore = score(board)
                    move_y = i
                    move_x = j
                board[i][j]=" "



    return move_y, move_x



def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def isFull(board):
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == " ":
                return False
    return True

def is_win(board):
    if has_five_in_a_row(board,"w"):
        return "White won"
    elif has_five_in_a_row(board,"b"):
        return "Black won"
    elif isFull(board):
        return "Draw"
    else:
        return "Continue playing"




def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])

        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print(game_res)
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print(game_res)
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 2;
    y = 2;
    d_x = 0;
    d_y = 1;
    length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    put_seq_on_board(board,1,2,1,0,1,"w")
    put_seq_on_board(board, 7, 2, 1, 0, 1, "w")
    print_board(board)

    y_end = 6
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 1;
    y = 1;
    d_x = 1;
    d_y = 1;
    length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board,3,3,1,1,1,"b")
    put_seq_on_board(board, 5, 5, 1, 1, 2, "w")
    print_board(board)
    if detect_row(board, "w", 0, 0, 3, d_y, d_x) == (0, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3;
    x = 5;
    d_x = -1;
    d_y = 1;
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     

    y = 5;
    x = 3;
    d_x = -1;
    d_y = 1;
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


def test_detect_row1():
    # Test case 1: Horizontal sequence (0,1) with an open end
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[2][0:4] = ["w", "w", "w", "w"]  # A sequence of 4 whites with an open end on the left
    board[2][4] = " "  # Right side is open
    print("Testing horizontal sequence with open end:")
    print_board(board)
    assert detect_row(board, "w", 2, 0, 4, 0, 1) == (0, 1), "Horizontal test failed"

    # Test case 2: Vertical sequence (1,0) with one side blocked (semi-open)
    board = [[" " for _ in range(8)] for _ in range(8)]
    for i in range(4):
        board[i][5] = "b"  # A sequence of 4 blacks
    board[4][5] = "w"  # A white stone immediately after the sequence, blocking it on one side
    print("Testing vertical sequence with one blocked end (semi-open):")
    print_board(board)
    assert detect_row(board, "b", 0, 5, 4, 1, 0) == (0, 0), "Vertical test failed"

    # Test case 3: Diagonal top-left to bottom-right (1,1) completely open
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[0][0] = "w"
    board[1][1] = "w"
    board[2][2] = "w"
    board[3][3] = "w"  # A sequence of 4 whites, both ends are open
    print("Testing diagonal (top-left to bottom-right) fully open sequence:")
    print_board(board)
    assert detect_row(board, "w", 0, 0, 4, 1, 1) == (0, 1), "Diagonal top-left to bottom-right test failed"

    # Test case 4: Diagonal top-right to bottom-left (1,-1) with both ends blocked (closed)
    board = [[" " for _ in range(8)] for _ in range(8)]

    board[1][6] = "b"
    board[2][5] = "b"
    board[3][4] = "b"  # A sequence of 4 blacks, with white stones on both sides

    board[0][6] = "w"
    board[5][2]=board[6][1]=board[7][0]="b"
    print("Testing diagonal (top-right to bottom-left) with both ends blocked (closed):")
    print_board(board)
    assert detect_row(board, "b", 0, 7, 3, 1, -1) == (1, 1), "Diagonal top-right to bottom-left test failed"

    print("TEST CASE for detect_row1 PASSED")

def test_detect_rows2():
    # Test case 1: Horizontal sequence with mixed states
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[0][1:5] = ["w", "w", "w", "w"]  # A sequence of 4 whites, open on one side
    board[0][5] = "b"                     # Right end blocked
    print("Testing horizontal semi-open sequence:")
    print_board(board)
    assert detect_rows(board, "w", 4) == (0, 1), "Horizontal semi-open test failed"

    # Test case 2: Vertical open sequence of length 3 for black
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[0][3] = "b"
    board[1][3] = "b"
    board[2][3] = "b"  # A complete open sequence of 3 blacks
    print("Testing vertical open sequence:")
    print_board(board)
    assert detect_rows(board, "b", 3) == (0, 1), "Vertical open test failed"

    # Test case 3: Diagonal top-left to bottom-right with both ends open
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[2][2] = "w"
    board[3][3] = "w"
    board[4][4] = "w"  # A complete open sequence of 3 whites
    print("Testing diagonal (top-left to bottom-right) open sequence:")
    print_board(board)
    assert detect_rows(board, "w", 3) == (1, 0), "Diagonal top-left to bottom-right open test failed"

    # Test case 4: Diagonal top-right to bottom-left semi-open
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[0][7] = "b"
    board[1][6] = "b"
    board[2][5] = "b"
    board[3][4] = "b"  # Complete sequence with blocked left end
    board[4][3] = "w"  # Blocked by a white stone
    print("Testing diagonal (top-right to bottom-left) semi-open sequence:")
    print_board(board)
    assert detect_rows(board, "b", 4) == (0, 0), "Diagonal top-right to bottom-left semi-open test failed"

    # Test case 5: Random board with multiple sequences
    board = [[" " for _ in range(8)] for _ in range(8)]
    board[7][0:5] = ["w", "w", "w", "w", "w"]  # A closed sequence of 5 whites
    board[2][0] = board[3][1] = board[4][2] = board[5][3] = "b"  # Diagonal of 4 blacks with open ends
    board[0][3:7]= ["b","b","b","b"]
    print("Testing multiple sequences:")
    print_board(board)
    assert detect_rows(board, "w", 5) == (0, 1), "Closed sequence of 5 whites not counted"
    assert detect_rows(board, "b", 4) == (1, 1), "Open sequence of 4 blacks not detected"

    print("TEST CASE for detect_rows2 PASSED")

if __name__ == '__main__':
    easy_testset_for_main_functions()
    test_detect_row1()
    test_detect_rows2()
    some_tests()
    #play_gomoku(8)
