import pygame
import blocks
from player import *


class Levels:
    def __init__(self):
        self.levelT = ["----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "X          D   -------           --    X",
                       "X          D    -----   B              X",
                       "X     - -  D    -----   --       -     X",
                       "X     - -  D            ---      -     X",
                       "-------X---------------X----------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------",
                       "----------------------------------------"]
        self.level1 = ["----------------------------------------",
                       "-6   X      ----------------          8-",
                       "-    X      ----------------           -",
                       "-    X       --------------            -",
                       "---  X       --------------            -",
                       "-             ------------             -",
                       "-                 ----                 -",
                       "-                 ----                 -",
                       "-         -X-     ----     -X-  -X-    -",
                       "--------------    ----    --------------",
                       "-2    D      -    ----    -           4-",
                       "-     D      -    ----    -            -",
                       "-     D      --   ----   --            -",
                       "-     D      -X    db    X-     B      -",
                       "-------XX---5--------------7------XX----",
                       "-              ------XXXX              -",
                       "-               -----XXXX              -",
                       "-                ------                -",
                       "-                 ----    -            -",
                       "-          -  -   ----    -            -",
                       "-         --XX--  ----     -           -",
                       "-        ---XX--- 1--3     -           -",
                       "------XX---------------------------XX---"]
        self.level2 = ["----------------------------------------",
                       "-             d  -        --------------",
                       "-            Bd  -        --------------",
                       "-          ----  -        --------------",
                       "-         -----           --XX--       -",
                       "-        ------           -XXXX-   -   -",
                       "---------------                  - - -3-",
                       "---------------  --XX--XX---------------",
                       "------       --  -XXXXXXXXX-4-         -",
                       "-----        ---------------           -",
                       "----         -6-   --   -8--           -",
                       "---          -     --     --           -",
                       "--    -     ----   --   ----           -",
                       "-7    -     2-X          X------XX-X--5-",
                       "----------------------------------------",
                       "-----------------XXXXX------------------",
                       "-               --XXX--        ---------",
                       "- -              -XXX-         D       -",
                       "- --             -XXX-         D       -",
                       "- --X                   -      D       -",
                       "- ----                  --     D       -",
                       "-1-----   -  -         b---    --XX-----",
                       "---------------------------XX----XX-----"]
        self.level3 = ["----------------------------------------",
                       "-               --------              8-",
                       "-               --------              --",
                       "-               --------              --",
                       "-               d  --  D           -----",
                       "-           X   d  --  D        -- -----",
                       "-              Bd  --  Db           ----",
                       "-             ---  --  ---X--        ---",
                       "-        -X------- -- ------          --",
                       "-6      X--------- -- ----             -",
                       "--XX--X----------- -- ---              -",
                       "-          ------- -- -                -",
                       "-          ---  -- -- -               --",
                       "-         ---    - -- -              ---",
                       "-         XXX    - -- -             ----",
                       "-           X    - -- -            -----",
                       "-       --  X    - -- -     -     ------",
                       "--    -X--       - -- -  -    -   XXXX--",
                       "-4  - ----      5- -- -7 --     -     2-",
                       "----- --------  -- -- --XXXXX-X---------",
                       "-                - -- -                -",
                       "-                - -- -                -",
                       "-                - -- -                -",
                       "-                - -- -             --3-",
                       "-                -    -              ---",
                       "-  -X-           -    -           --   -",
                       "-1-    ---       ------                -",
                       "---         ---               --       -",
                       "-                         --           -",
                       "-XXXXXXXXXXXXXXX--------XXXXXXXXXXXXXXX-"]
        self.playerT = [32, 400, 1216, 400]
        self.player1 = [32, 600, 1216, 600]
        self.player2 = [100, 100, 1200, 600]
        self.player3 = [650, 890, 600, 890]
        self.levels = [self.levelT, self.level1, self.level2, self.level3]
        self.players = [self.playerT, self.player1, self.player2, self.player3]
        self.lvl_camera_on = [False, False, False, True]

    def build_level(self, n):
        entities = pygame.sprite.Group()
        player_left = PlayerLeft(self.players[n][0], self.players[n][1])
        player_right = PlayerRight(self.players[n][2], self.players[n][3])
        entities.add(player_left, player_right)
        x = y = 0
        for row in self.levels[n]:
            for col in row:
                if col == "-":
                    block = Block(x, y)
                    entities.add(block)
                if col == "X":
                    block = DeathBlock(x, y)
                    entities.add(block)
                if col == "1":
                    block = TeleportIn(x, y, 1)
                    entities.add(block)
                if col == "2":
                    block = TeleportOut(x, y, 1)
                    entities.add(block)
                if col == "3":
                    block = TeleportIn(x, y, 2)
                    entities.add(block)
                if col == "4":
                    block = TeleportOut(x, y, 2)
                    entities.add(block)
                if col == "5":
                    block = TeleportIn(x, y, 3)
                    entities.add(block)
                if col == "6":
                    block = TeleportOut(x, y, 3)
                    entities.add(block)
                if col == "7":
                    block = TeleportIn(x, y, 4)
                    entities.add(block)
                if col == "8":
                    block = TeleportOut(x, y, 4)
                    entities.add(block)
                if col == "B":
                    block = Button(x, y, 1)
                    entities.add(block)
                if col == "D":
                    block = Door(x, y, 1)
                    entities.add(block)
                if col == "b":
                    block = Button(x, y, 2)
                    entities.add(block)
                if col == "d":
                    block = Door(x, y, 2)
                    entities.add(block)
                x += blocks.SIZE
            y += blocks.SIZE
            x = 0
        return entities
