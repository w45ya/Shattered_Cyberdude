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
        self.resume = False
        self.window_width = 1280
        self.window_height = 720
        self.screen_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(
            self.screen_size,
            pygame.DOUBLEBUF | pygame.HWSURFACE
        )
        # self.font_name = pygame.font.get_default_font()
        self.font = resource_path('resources/fonts/Pixeboy-z8XGD.ttf')
        pygame.display.set_caption("Shattered Cyberdude 1.2")
        pygame.display.set_icon(pygame.image.load(resource_path("resources/icon/icon.ico")))
        self.clock = pygame.time.Clock()
        self.fps = 120

        self.JumpKey = False
        self.RightKey = False

        self.Back_color = (0, 70, 70)
        self.Font_color = (60, 120, 120)
        self.Title_color = (106, 186, 151)
        self.background = pygame.image.load(resource_path('resources/background/background.png'))
        self.background_01 = pygame.image.load(resource_path('resources/background/background_01.png'))
        self.background_02 = pygame.image.load(resource_path('resources/background/background_02.png'))
        self.background_03 = pygame.image.load(resource_path('resources/background/background_03.png'))
        self.background_04 = pygame.image.load(resource_path('resources/background/background_04.png'))
        self.background_05 = pygame.image.load(resource_path('resources/background/background_05.png'))
        self.background_06 = pygame.image.load(resource_path('resources/background/background_06.png'))
        self.background_07 = pygame.image.load(resource_path('resources/background/background_07.png'))
        self.background_08 = pygame.image.load(resource_path('resources/background/background_08.png'))
        self.background_09 = pygame.image.load(resource_path('resources/background/background_09.png'))
        self.background_10 = pygame.image.load(resource_path('resources/background/background_10.png'))
        self.background_11 = pygame.image.load(resource_path('resources/background/background_11.png'))
        self.background_12 = pygame.image.load(resource_path('resources/background/background_12.png'))
        self.background_13 = pygame.image.load(resource_path('resources/background/background_13.png'))
        self.background_14 = pygame.image.load(resource_path('resources/background/background_14.png'))
        self.background_15 = pygame.image.load(resource_path('resources/background/background_15.png'))
        self.background_16 = pygame.image.load(resource_path('resources/background/background_16.png'))
        self.background_animation = [self.background_01, self.background_02, self.background_03, self.background_04,
                                     self.background_05, self.background_06, self.background_07, self.background_08,
                                     self.background_09, self.background_10, self.background_11, self.background_12,
                                     self.background_13, self.background_14, self.background_15, self.background_16]
        self.animation_delay = 100
        self.animation_array = []
        for a in self.background_animation:
            self.animation_array.append((a, self.animation_delay))
        self.animation = pyganim.PygAnimation(self.animation_array)
        self.rect = self.background.get_rect()

        self.sound_wrong = pygame.mixer.Sound(resource_path('resources/sound/wrong.ogg'))
        self.sound_wrong.set_volume(0.3)
        self.sound_start = pygame.mixer.Sound(resource_path('resources/sound/start.ogg'))
        self.sound_noise = pygame.mixer.Sound(resource_path('resources/sound/noise.ogg'))
        self.sound_noise.set_volume(0.5)
        self.sound_level = pygame.mixer.Sound(resource_path('resources/sound/level.ogg'))
        self.sound_victory = pygame.mixer.Sound(resource_path('resources/sound/victory.ogg'))
        self.sound_menu_press = pygame.mixer.Sound(resource_path('resources/sound/menu_press.ogg'))
        self.sound_menu_select = pygame.mixer.Sound(resource_path('resources/sound/menu_select.ogg'))
        self.sound_jump = pygame.mixer.Sound(resource_path('resources/sound/jump.ogg'))
        self.sound_door = pygame.mixer.Sound(resource_path('resources/sound/door.ogg'))
        self.sound_tp = pygame.mixer.Sound(resource_path('resources/sound/tp.ogg'))
        self.sound_death = pygame.mixer.Sound(resource_path('resources/sound/death.ogg'))
        self.sound_tp.set_volume(0.5)
        self.sound_player = [self.sound_jump, self.sound_door, self.sound_tp, self.sound_death]

        self.main_menu = MainMenu(self)
        self.story = StoryMenu(self)
        self.curr_menu = self.main_menu

        self.level = Levels()
        self.lvl_n = 0
        self.level_completed = False

    def run(self):
        self.running = True
        self.sound_start.play()
        self.sound_noise.play(-1)
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
                if e.key == pygame.K_w or e.key == pygame.K_UP \
                        or e.key == pygame.K_s or e.key == pygame.K_DOWN \
                        or e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    self.sound_wrong.play()
                if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    self.RightKey = True
                    if not self.playing:
                        self.sound_menu_select.play()
                if e.key == pygame.K_SPACE:
                    self.JumpKey = True
                    if not self.playing:
                        self.sound_menu_press.play()
                if e.key == pygame.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                        self.sound_menu_press.play()
                        self.resume = True

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    self.RightKey = False
                if e.key == pygame.K_SPACE:
                    self.JumpKey = False

    def reset_keys(self):
        self.JumpKey = False
        self.RightKey = False

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
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
            pygame.time.wait(1000)
            self.sound_victory.play()
            self.screen.fill(self.Back_color)
            self.screen.blit(pygame.image.load(resource_path('resources/background/background.png')), self.rect)
            self.draw_text('You win', 120, self.window_width / 2 + 5, self.window_height / 2 + 5, self.Back_color)
            self.draw_text('You win', 120, self.window_width / 2 - 5, self.window_height / 2 - 5, self.Title_color)
            self.draw_text('You win', 120, self.window_width / 2, self.window_height / 2, self.Font_color)
            pygame.display.flip()
            pygame.time.wait(1000)
            self.playing = False
            self.resume = False

    def loop(self):
        if not self.resume:
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
                self.sound_level.play()
                self.draw_text('Level completed', 120, self.window_width / 2 + 5, self.window_height / 2 + 5, self.Back_color)
                self.draw_text('Level completed', 120, self.window_width / 2 - 5, self.window_height / 2 - 5, self.Title_color)
                self.draw_text('Level completed', 120, self.window_width / 2, self.window_height / 2, self.Font_color)
                pygame.display.flip()
                self.lvl_n += 1
                self.set_level(self.lvl_n)
                pygame.time.wait(1000)
                self.level_completed = False

            self.screen.fill(self.Back_color)
            self.animation.play()
            self.screen.blit(self.background, self.rect)
            self.animation.blit(self.background, (0, 0))
            self.player_left.update(self.RightKey, self.JumpKey, self.entities, self.sound_player)
            self.player_right.update(self.RightKey, self.JumpKey, self.entities, self.sound_player)
            for e in self.entities:
                self.screen.blit(e.image, self.camera.apply(e))
                if isinstance(e, DeathBlock) or isinstance(e, TeleportIn) or isinstance(e, TeleportOut):
                    e.update(game)
                    self.screen.blit(e.image, self.camera.apply(e))
            for e in self.entities:
                if isinstance(e, PlayerLeft) or isinstance(e, PlayerRight):
                    self.screen.blit(e.image, self.camera.apply(e))
            if self.level.lvl_camera_on[self.lvl_n]:
                self.camera.update(self.player_left)
            pygame.display.flip()


game = Game()
game.run()
