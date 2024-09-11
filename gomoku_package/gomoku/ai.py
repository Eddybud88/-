import random

class GomokuAI:
    def __init__(self, board):
        self.board = board
        self.ai_player = 'O'
        self.human_player = 'X'

    def get_best_move(self):
        # 1. 优先检查是否需要阻挡对手的四连或活三
        block_move = self.block_opponent_threats()
        if block_move:
            return block_move

        # 2. 再检查AI是否可以形成五连或四连
        winning_move = self.find_winning_move(self.ai_player)
        if winning_move:
            return winning_move

        # 3. 如果没有发现防守或进攻的紧急情况，遍历所有空位并评估进攻与防守的综合分数
        best_score = -float('inf')
        best_move = None
        for x in range(self.board.board_size):
            for y in range(self.board.board_size):
                if self.board.board[x][y] == '.':
                    # 试探在空位下棋
                    self.board.board[x][y] = self.ai_player
                    offense_score = self.evaluate_board(x, y, self.ai_player)
                    self.board.board[x][y] = self.human_player
                    defense_score = self.evaluate_board(x, y, self.human_player)
                    self.board.board[x][y] = '.'  # 恢复棋盘

                    # 综合评分：防守分数（阻止对手获胜）+ 进攻分数
                    total_score = defense_score + offense_score

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
        count = 1  # 从当前棋子开始计算
        blocked_start = False
        blocked_end = False

        # 检查前向
        cur_x, cur_y = x + dx, y + dy
        while 0 <= cur_x < self.board.board_size and 0 <= cur_y < self.board.board_size:
            if self.board.board[cur_x][cur_y] == player:
                count += 1
            elif self.board.board[cur_x][cur_y] != '.':
                blocked_end = True
                break
            else:
                break
            cur_x += dx
            cur_y += dy

        # 检查后向
        cur_x, cur_y = x - dx, y - dy
        while 0 <= cur_x < self.board.board_size and 0 <= cur_y < self.board.board_size:
            if self.board.board[cur_x][cur_y] == player:
                count += 1
            elif self.board.board[cur_x][cur_y] != '.':
                blocked_start = True
                break
            else:
                break
            cur_x -= dx
            cur_y -= dy

        # 根据连珠长度和是否被堵来评分
        if count >= 5:
            return 100000  # 五连
        elif count == 4:
            if not blocked_start and not blocked_end:  # 四连
                return 10000
            else:  # 四连被堵的情况
                return 1000
        elif count == 3:
            if not blocked_start and not blocked_end:  # 活三
                return 5000
            elif blocked_start or blocked_end:  # 三连一端被堵住
                return 1000
            else:  # 三连两端都被堵住
                return 500
        elif count == 2:
            if not blocked_start and not blocked_end:  # 形成二连且未被堵
                return 300
            else:  # 二连被堵
                return 50
        elif count == 1:
            if not blocked_start and not blocked_end:  # 形成一连且未被堵
                return 10
            else:  # 一连被堵
                return 1
        return 0

    def find_winning_move(self, player):
        # 寻找AI是否可以形成五连或四连的移动
        for x in range(self.board.board_size):
            for y in range(self.board.board_size):
                if self.board.board[x][y] == '.':
                    self.board.board[x][y] = player
                    for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                        if self.evaluate_direction(x, y, dx, dy, player) >= 10000:  # 四连或更高
                            self.board.board[x][y] = '.'
                            return (x, y)
                    self.board.board[x][y] = '.'
        return None

    def block_opponent_threats(self):
        # 优先阻挡对手的四连或活三
        best_block_move = None
        best_block_score = -float('inf')  # 初始化为非常低的值，以便找到最优阻挡位置

        for x in range(self.board.board_size):
            for y in range(self.board.board_size):
                if self.board.board[x][y] == '.':
                    self.board.board[x][y] = self.human_player
                    block_found = False

                    # 检查是否阻挡成功
                    for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                        score = self.evaluate_direction(x, y, dx, dy, self.human_player)
                        if score >= 5000:  # 如果是四连或活三
                            block_found = True
                            break

                    # 恢复棋盘状态
                    self.board.board[x][y] = '.'

                    if block_found:
                        # 给阻挡的每个位置一个分数，作为优先级
                        block_score = self.evaluate_board(x, y, self.human_player)
                        if block_score > best_block_score:
                            best_block_score = block_score
                            best_block_move = (x, y)

        return best_block_move
