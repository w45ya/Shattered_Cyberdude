import pygame
import pyganim
from blocks import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.window_width / 2
        self.mid_h = self.game.window_height / 2
        self.run_display = True
        self.menu_selector = pygame.image.load(resource_path('resources/menu/menu_selector.png'))
        self.menu_background = pygame.image.load(resource_path('resources/menu/menu_background.png'))
        self.menu_background_frame_1 = pygame.image.load(resource_path('resources/menu/menu_background_1.png'))
        self.menu_background_frame_2 = pygame.image.load(resource_path('resources/menu/menu_background_2.png'))
        self.menu_background_animation = [self.menu_background_frame_1, self.menu_background_frame_1,
                                               self.menu_background_frame_1, self.menu_background_frame_1,
                                               self.menu_background_frame_2, self.menu_background_frame_1,
                                               self.menu_background_frame_2, self.menu_background_frame_1,
                                               self.menu_background_frame_1, self.menu_background_frame_1]
        self.animation_delay = 200
        self.animation_array = []
        for a in self.menu_background_animation:
            self.animation_array.append((a, self.animation_delay))
        self.rect = self.menu_background.get_rect()
        self.animation = pyganim.PygAnimation(self.animation_array)
        self.cursor_rect = self.menu_selector.get_rect()
        self.offset = -54

    def draw_cursor(self):
        self.game.screen.blit(self.menu_selector, self.cursor_rect)

    def blit_screen(self):
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play"
        self.title_x = self.mid_w
        self.title_y = self.mid_h - 300
        self.start_x = self.mid_w
        self.start_y = self.mid_h - 120
        self.story_x = self.mid_w
        self.story_y = self.mid_h
        self.cursor_rect.midtop = (self.start_x, self.start_y + self.offset)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.events()
            self.check_input()
            self.game.screen.fill(self.game.Back_color)
            self.animation.play()
            self.game.screen.blit(self.menu_background, self.rect)
            self.animation.blit(self.menu_background, (0, 0))
            self.game.draw_text("Shattered Cyberdude", 130, self.title_x + 5, self.title_y + 5, self.game.Back_color)
            self.game.draw_text("Shattered Cyberdude", 130, self.title_x - 5, self.title_y - 5, self.game.Title_color)
            self.game.draw_text("Shattered Cyberdude", 130, self.title_x, self.title_y, self.game.Font_color)
            self.game.draw_text("Play", 120, self.start_x, self.start_y, self.game.Font_color)
            self.game.draw_text("Story", 120, self.story_x, self.story_y, self.game.Font_color)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.RightKey:
            if self.state == 'Play':
                self.cursor_rect.midtop = (self.story_x, self.story_y + self.offset)
                self.state = 'Story'
            elif self.state == 'Story':
                self.cursor_rect.midtop = (self.start_x, self.start_y + self.offset)
                self.state = 'Play'

    def check_input(self):
        self.move_cursor()
        if self.game.JumpKey:
            if self.state == 'Play':
                self.game.playing = True
            elif self.state == 'Story':
                self.game.curr_menu = self.game.story
            self.run_display = False


class StoryMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.events()
            if self.game.JumpKey or self.game.RightKey:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.screen.fill(self.game.Back_color)
            self.game.screen.blit(self.menu_background, self.rect)
            self.game.draw_text('Story', 150, self.game.window_width / 2 + 5, self.game.window_height / 2 - 295, self.game.Back_color)
            self.game.draw_text('Story', 150, self.game.window_width / 2 - 5, self.game.window_height / 2 - 305, self.game.Title_color)
            self.game.draw_text('Story', 150, self.game.window_width / 2, self.game.window_height / 2 - 300, self.game.Font_color)
            self.game.draw_text('Cyberdude lived in one peaceful cyberspace, but one day', 36, self.game.window_width / 2, self.game.window_height / 2 - 180, self.game.Title_color)
            self.game.draw_text('his home became a victim of an attack of wandering viruses.', 36, self.game.window_width / 2, self.game.window_height / 2 - 150, self.game.Title_color)
            self.game.draw_text('With the help of the intervention of the all-seeing firewall,', 36, self.game.window_width / 2, self.game.window_height / 2 - 120, self.game.Title_color)
            self.game.draw_text('the cyberspace was cleared of uninvited guests.', 36, self.game.window_width / 2, self.game.window_height / 2 - 90, self.game.Title_color)
            self.game.draw_text('Unfortunately, the cyber-bullies managed to thoroughly destroy', 36, self.game.window_width / 2, self.game.window_height / 2 - 60, self.game.Title_color)
            self.game.draw_text('the internal code of cyberspace and our character suffered the most.', 36, self.game.window_width / 2, self.game.window_height / 2 - 30, self.game.Title_color)
            self.game.draw_text('He was broken in half, and now he needs to find himself. Literally!', 36, self.game.window_width / 2, self.game.window_height / 2 + 0, self.game.Title_color)
            self.game.draw_text('By the way, one of the viruses turned out to have a code ', 36, self.game.window_width / 2, self.game.window_height / 2 + 60, self.game.Title_color)
            self.game.draw_text('breaking the fourth wall, so the controls are also broken.', 36, self.game.window_width / 2, self.game.window_height / 2 + 90, self.game.Title_color)
            self.game.draw_text('Now both halves of our hero are only able to move forward and jump. ', 36, self.game.window_width / 2, self.game.window_height / 2 + 120, self.game.Title_color)
            self.game.draw_text('And they can move only at the same time. Such a difficult fate.', 36, self.game.window_width / 2, self.game.window_height / 2 + 150, self.game.Title_color)
            self.blit_screen()
