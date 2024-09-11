class GomokuBoard:
    def __init__(self, board_size=15):
        self.board_size = board_size
        self.board = [['.' for _ in range(board_size)] for _ in range(board_size)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()  # 增加换行以便输出更清晰

    def is_valid_move(self, x, y):
        return (0 <= x < self.board_size and
                0 <= y < self.board_size and
                self.board[x][y] == '.')

    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            self.board[x][y] = player
            return True
        return False

    def check_winner(self, x, y, player):
        # 检查所有四个方向是否有五子连珠
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            if self.count_stones(x, y, dx, dy, player) + \
               self.count_stones(x, y, -dx, -dy, player) - 1 >= 5:
                return True
        return False

    def count_stones(self, x, y, dx, dy, player):
        count = 0
        cur_x, cur_y = x, y
        while (0 <= cur_x < self.board_size and
               0 <= cur_y < self.board_size and
               self.board[cur_x][cur_y] == player):
            count += 1
            cur_x += dx
            cur_y += dy
        return count

    def get_empty_cells(self):
        return [(x, y) for x in range(self.board_size)
                for y in range(self.board_size) if self.board[x][y] == '.']


