import consts

class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        new_head = (self.get_head()[0] + self.dx[self.direction], self.get_head()[1] + self.dy[self.direction])
        if new_head in self.cells or not (0 <= new_head[0] < consts.width and 0 <= new_head[1] < consts.height):
            self.game.game_over()
            return
        self.cells.append(new_head)
        if new_head != self.game.food:
            self.cells.pop(0)
        else:
            self.game.food = self.game.get_random_cell()
            self.game.score += 1

    def handle(self, keys):
        if keys[self.keys[0]]:
            self.direction = 'UP'
        elif keys[self.keys[1]]:
            self.direction = 'DOWN'
        elif keys[self.keys[2]]:
            self.direction = 'LEFT'
        elif keys[self.keys[3]]:
            self.direction = 'RIGHT'
