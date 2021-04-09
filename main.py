import pygame
from menu import *
from player import *
from levels import *
from camera import *
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


class Game:
    def __init__(self):
        self.running = False
        self.playing = False
        self.window_width = 1280
        self.window_height = 720
        self.screen_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(
            self.screen_size,
            pygame.DOUBLEBUF | pygame.HWSURFACE
        )
        # self.font_name = pygame.font.get_default_font()
        self.font = 'resources/fonts/Pixeboy-z8XGD.ttf'
        pygame.display.set_caption("Shattered Cyberdude")
        self.clock = pygame.time.Clock()
        self.delta = self.clock.get_time() / 1000
        self.fps = 120

        self.JumpKey = False
        self.RightKey = False
        self.WrongKey = False

        self.Back_color = (0, 36, 36)
        self.Font_color = (60, 120, 120)

        self.main_menu = MainMenu(self)
        self.story = StoryMenu(self)
        self.curr_menu = self.main_menu

        self.level = Levels()
        self.lvl_n = 0
        self.level_completed = False


    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.curr_menu.display_menu()
            else:
                self.loop()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.main_menu.run_display = False
                self.story.run_display = False

            if e.type == pygame.KEYDOWN:
                # if e.key == pygame.K_ESCAPE:
                #    self.playing = False
                if e.key == pygame.K_w or e.key == pygame.K_w \
                        or e.key == pygame.K_s or e.key == pygame.K_DOWN \
                        or e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    self.WrongKey = True
                if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    self.RightKey = True
                if e.key == pygame.K_SPACE:
                    self.JumpKey = True
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_w or e.key == pygame.K_w \
                        or e.key == pygame.K_s or e.key == pygame.K_DOWN \
                        or e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    self.WrongKey = False
                if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    self.RightKey = False
                if e.key == pygame.K_SPACE:
                    self.JumpKey = False

    def reset_keys(self):
        self.JumpKey = False
        self.RightKey = False
        self.WrongKey = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, self.Font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def set_level(self, lvl_n):
        if lvl_n < len(self.level.levels):
            self.total_level_width = len(self.level.levels[self.lvl_n][0]) * SIZE
            self.total_level_height = len(self.level.levels[self.lvl_n]) * SIZE
            self.camera = Camera(camera_configure, self.total_level_width, self.total_level_height)
            self.entities = Levels.build_level(self.level, lvl_n)
            for e in self.entities:
                if isinstance(e, PlayerLeft):
                    self.player_left = e
                if isinstance(e, PlayerRight):
                    self.player_right = e
        else:
            self.screen.fill(self.Back_color)
            self.draw_text('You win', 120, self.window_width / 2, self.window_height / 2)
            pygame.display.flip()
            self.playing = False

    def loop(self):
        self.lvl_n = 0
        self.set_level(self.lvl_n)
        while self.playing:
            self.clock.tick(self.fps)
            self.delta = self.clock.get_time() / 1000
            self.events()

            if self.player_left.win:
                self.level_completed = True
                self.reset_keys()

            if self.level_completed:
                self.draw_text('Level completed', 120, self.window_width / 2, self.window_height / 2)
                pygame.display.flip()
                self.lvl_n += 1
                self.set_level(self.lvl_n)
                pygame.time.wait(1000)
                self.level_completed = False

            self.screen.fill(self.Back_color)
            self.player_left.update(self.RightKey, self.JumpKey, self.delta, self.entities)
            self.player_right.update(self.RightKey, self.JumpKey, self.delta, self.entities)
            self.camera.update(self.player_left)
            for e in self.entities:
                self.screen.blit(e.image, self.camera.apply(e))
            pygame.display.flip()


game = Game()
game.run()
