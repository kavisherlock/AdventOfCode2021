f = open("../input", "r")

contents = f.readlines()

drawn_numbers = contents[0].split(',')

boards = []
cur_board = []
for i in range(2, len(contents)):
  line = contents[i].strip()
  if len(line) == 0:
    boards.append(cur_board)
    cur_board = []
    continue

  cur_board += list(filter(lambda n : len(n.strip()) > 0, line.split(' ')))

def get_position_on_board(board, number_drawn):
  for i in range(0, len(board)):
    if board[i] == number_drawn:
      return i
  
  return -1

def check_board_for_bingo(board):
  for i in range(0, 5):
    row_check = 0
    for j in range(i * 5, (i + 1) * 5):
      if board[j].endswith('D'):
        row_check += 1
    if row_check == 5:
      return True

  for i in range(0, 5):
    col_check = 0
    for j in range(0, 5):
      if board[j * 5 + i].endswith('D'):
        col_check += 1
    if col_check == 5:
      return True
  
  return False

def bingo(boards, drawn_numbers):
  n_boards = len(boards)
  n_boards_won = 0
  bingos = [False] * n_boards
  for number in drawn_numbers:
    for n_board in range(len(boards)):
      if bingos[n_board]: continue

      board = boards[n_board]
      pos = get_position_on_board(board, number)
      if pos == -1: continue

      board[pos] += 'D'
      if check_board_for_bingo(board):
        bingos[n_board] = True
        n_boards_won += 1
        if n_boards_won == n_boards:
          unmarked_total = 0
          for n in board:
            if not n.endswith('D'):
              unmarked_total += int(n)
          
          print(unmarked_total * int(number))
          return

bingo(boards, drawn_numbers)
