class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'

    def move(self):
        head = self.body[0]
        if self.direction == 'RIGHT':
            new_head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == 'UP':
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + BLOCK_SIZE)
        self.body.insert(0, new_head)

    def eat(self, food):
        if self.body[0] == food:
            return True
        else:
            self.body.pop()
            return False

class Food:
    def __init__(self):
        self.position = (400, 300)

    def generate(self):
        self.position = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                         random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)