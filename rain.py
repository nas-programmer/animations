import random, math, arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Rain"


class RainDrop:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.shapes = arcade.ShapeElementList()

        color1 = (10, 90, 120)
        color2 = (0, 20, 32)
        points = (0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)
        colors = (color1, color1, color2, color2)
        rect = arcade.create_rectangle_filled_with_colors(points, colors)
        self.shapes.append(rect)

        self.raindrop_list = None


    def start_rain(self):

        self.raindrop_list = []


        for i in range(500):
            raindrop = RainDrop()
            raindrop.x = random.randrange(SCREEN_WIDTH)
            raindrop.y = random.randrange(SCREEN_HEIGHT + 500)
            raindrop.speed = random.randrange(50, 120)
            raindrop.angle = random.uniform(math.pi, math.pi * 2)
            self.raindrop_list.append(raindrop)

        
        self.set_mouse_visible(False)


    def on_draw(self):
        arcade.start_render()

        self.shapes.draw()
        for raindrop in self.raindrop_list:
            arcade.draw_line(raindrop.x, raindrop.y,
                                      raindrop.x, raindrop.y + 10, arcade.color.LIGHT_CORNFLOWER_BLUE, 2)


    def on_update(self, delta_time):

        for raindrop in self.raindrop_list:
            raindrop.y -= raindrop.speed * delta_time * 20

            if raindrop.y < 0:
                raindrop.reset_pos()

            raindrop.x += raindrop.speed * math.cos(raindrop.angle) * delta_time
            raindrop.angle += 1 * delta_time


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_rain()
    arcade.run()


if __name__ == "__main__":
    main()