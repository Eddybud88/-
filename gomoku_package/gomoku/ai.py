import random


class GomokuAI:
    def __init__(self, board):
        self.board = board
        self.ai_player = 'O'
        self.human_player = 'X'

    def get_best_move(self):
        best_score = -float('inf')
        best_move = None

        # 遍历所有空位
        for x in range(self.board.board_size):
            for y in range(self.board.board_size):
                if self.board.board[x][y] == '.':
                    # 试探在空位下棋
                    self.board.board[x][y] = self.ai_player
                    offense_score = self.evaluate_board(x, y, self.ai_player)
                    self.board.board[x][y] = self.human_player
                    defense_score = self.evaluate_board(x, y, self.human_player)
                    self.board.board[x][y] = '.'  # 恢复棋盘

                    # 综合评分：进攻分数 + 防守分数（防止玩家获胜）
                    total_score = offense_score + defense_score

                    # 如果该位置的得分更高，则选择该位置
                    if total_score > best_score:
                        best_score = total_score
                        best_move = (x, y)

        # 如果没有找到更好的移动，选择随机移动（保险起见）
        return best_move if best_move else self.get_random_move()

    def get_random_move(self):
        empty_cells = [(x, y) for x in range(self.board.board_size)
                       for y in range(self.board.board_size)
                       if self.board.board[x][y] == '.']
        return random.choice(empty_cells) if empty_cells else None

    def evaluate_board(self, x, y, player):
        # 计算该位置的进攻或防守评分
        score = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            score += self.evaluate_direction(x, y, dx, dy, player)
            score += self.evaluate_direction(x, y, -dx, -dy, player)
        return score

    def evaluate_direction(self, x, y, dx, dy, player):
        # 计算在某个方向上连续相同颜色棋子的评分
        count = 0
        block = False  # 用来判断连珠是否被堵住（不能形成五连）

        cur_x, cur_y = x, y
        while 0 <= cur_x < self.board.board_size and 0 <= cur_y < self.board.board_size:
            if self.board.board[cur_x][cur_y] == player:
                count += 1
            elif self.board.board[cur_x][cur_y] != '.':  # 被对手棋子挡住
                block = True
                break
            else:
                break
            cur_x += dx
            cur_y += dy

        # 根据连珠长度和是否被堵来评分
        if count >= 4 and not block:  # 形成五子连珠
            return 10000
        elif count == 3 and not block:  # 形成四连且未被堵
            return 500
        elif count == 2 and not block:  # 形成三连且未被堵
            return 100
        elif count == 1 and not block:  # 形成二连
            return 10
        return 0

