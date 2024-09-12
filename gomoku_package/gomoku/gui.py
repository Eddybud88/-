import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageDraw, ImageTk

from SoftWareTrial.gomoku_package.gomoku.ai import GomokuAI
from SoftWareTrial.gomoku_package.gomoku.board import GomokuBoard


class GomokuGUI:
    def __init__(self, board_size=14):
        self.board = GomokuBoard(board_size)
        self.ai = GomokuAI(self.board)
        self.current_player = 'X'  # 玩家先手

        # 界面初始化
        self.root = tk.Tk()
        self.root.title("Gomoku")
        self.cell_size = 40
        self.padding = 20
        self.canvas = tk.Canvas(self.root, width=board_size * self.cell_size + self.padding * 2,
                                height=board_size * self.cell_size + self.padding * 2, bg='#f5deb3')  # 柔和木质背景
        self.canvas.pack()

        # 绘制棋盘背景和边框
        self.draw_board_background()
        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_star_points()
        self.status_text = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=("Arial", 14))
        self.status_text.pack(pady=10)

        # 保存棋子图像引用
        self.canvas.piece_images = []

        # 自定义样式
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))

    def draw_board_background(self):
        # 绘制棋盘背景线条
        for i in range(self.board.board_size):
            # 横线
            self.canvas.create_line(self.padding, self.padding + i * self.cell_size,
                                    self.padding + self.board.board_size * self.cell_size,
                                    self.padding + i * self.cell_size,
                                    fill="#a0522d", width=1)  # 使用更细的线条和木质色
            # 竖线
            self.canvas.create_line(self.padding + i * self.cell_size, self.padding,
                                    self.padding + i * self.cell_size,
                                    self.padding + self.board.board_size * self.cell_size,
                                    fill="#a0522d", width=1)

        # 绘制边框
        self.canvas.create_rectangle(self.padding - 1, self.padding - 1,
                                     self.padding + self.board.board_size * self.cell_size + 1,
                                     self.padding + self.board.board_size * self.cell_size + 1,
                                     outline='#8b4513', width=2)  # 边框颜色和粗细

    def draw_star_points(self):
        star_positions = [
            (3, 3), (3, 13),
            (13, 3), (13, 13),
            (8, 8)
        ]
        radius = 6  # 调整星点大小
        for x, y in star_positions:
            self.canvas.create_oval(self.padding + (x - 1) * self.cell_size - radius,
                                    self.padding + (y - 1) * self.cell_size - radius,
                                    self.padding + (x - 1) * self.cell_size + radius,
                                    self.padding + (y - 1) * self.cell_size + radius,
                                    fill='black', outline='black')

    def handle_click(self, event):
        # 计算点击位置对应的棋盘坐标
        x = (event.x - self.padding) // self.cell_size
        y = (event.y - self.padding) // self.cell_size
        # 确保点击在棋盘范围内
        if 0 <= x < self.board.board_size and 0 <= y < self.board.board_size:
            if self.board.make_move(x, y, self.current_player):
                self.draw_piece(x, y, self.current_player)
                if self.board.check_winner(x, y, self.current_player):
                    self.show_victory_message(f"Player {self.current_player} wins!",
                                              'green' if self.current_player == 'X' else 'blue')
                    self.canvas.unbind("<Button-1>")
                else:
                    self.current_player = 'O'  # AI 回合
                    self.ai_move()

    def ai_move(self):
        x, y = self.ai.get_best_move()
        if x is not None and y is not None:
            self.board.make_move(x, y, 'O')
            self.draw_piece(x, y, 'O')
            if self.board.check_winner(x, y, 'O'):
                self.show_victory_message("AI wins!", 'blue')
                self.canvas.unbind("<Button-1>")
            else:
                self.current_player = 'X'  # 玩家回合

    def draw_piece(self, x, y, player):
        # 根据玩家绘制黑白棋子，并添加3D效果
        color = 'black' if player == 'X' else 'white'

        # 计算棋子的中心位置，使其位于单元格的顶点
        x_vertex = self.padding + x * self.cell_size
        y_vertex = self.padding + y * self.cell_size
        radius = 15  # 棋子的半径

        # 创建一个临时Image对象，用来绘制3D棋子
        piece_image = Image.new('RGBA', (self.cell_size, self.cell_size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(piece_image)

        # 绘制棋子的渐变色和阴影效果
        gradient_color_start = (40, 40, 40) if player == 'X' else (220, 220, 220)
        gradient_color_end = (0, 0, 0) if player == 'X' else (255, 255, 255)

        for i in range(radius, 0, -1):
            step_color = tuple(
                int(gradient_color_start[j] + (gradient_color_end[j] - gradient_color_start[j]) * (i / radius))
                for j in range(3)
            )
            draw.ellipse([(self.cell_size // 2 - i, self.cell_size // 2 - i),
                          (self.cell_size // 2 + i, self.cell_size // 2 + i)],
                         fill=step_color, outline=step_color)

        # 绘制棋子边框
        border_color = 'black'
        draw.ellipse([(self.cell_size // 2 - radius, self.cell_size // 2 - radius),
                      (self.cell_size // 2 + radius, self.cell_size // 2 + radius)],
                     outline=border_color, width=2)

        # 将PIL图像转换为Tkinter可用的图像
        piece_image_tk = ImageTk.PhotoImage(piece_image)
        self.canvas.create_image(x_vertex - self.cell_size // 2, y_vertex - self.cell_size // 2,
                                 image=piece_image_tk, anchor='nw')

        # 需要保持对image的引用，否则图片无法显示
        self.canvas.piece_images.append(piece_image_tk)

    def show_victory_message(self, message, color='red'):
        victory_popup = tk.Toplevel(self.root)
        victory_popup.title("Victory!")
        victory_popup.geometry("300x200")

        victory_label = ttk.Label(victory_popup, text=message, font=("Arial", 24, "bold"), foreground=color)
        victory_label.pack(pady=20)

        close_button = ttk.Button(victory_popup, text="Close", command=victory_popup.destroy, style='TButton')
        close_button.pack(pady=10)

    def run(self):
        self.root.mainloop()

def main():
    game = GomokuGUI()
    game.run()
