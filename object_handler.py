from sprite_object import *
from npc import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # spawn npc
        self.enemies = 20  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # sprite map
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(5.3, 7.4)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'level 1/level 1.png', pos=(3.6, 7.45)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'level 2/level 2.png', pos=(11.8, 7.85)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'level 3/level 3.png', pos=(4.2, 20.9)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'baron/br.png', pos=(5.8, 3.33)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'baron/br1.png', pos=(5.8, 3.33)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'baron/br2.png', pos=(5.8, 3.33)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre2/cre.png', pos=(5.79, 3.83)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre2/cre1.png', pos=(5.79, 3.83)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre2/cre2.png', pos=(5.79, 3.83)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre2/cre3.png', pos=(5.79, 3.83)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre3/cre.png', pos=(5.79, 4.43)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre3/cre1.png', pos=(5.79, 4.43)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre3/cre2.png', pos=(5.79, 4.43)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'cre3/cre3.png', pos=(5.79, 4.43)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'sign/sig.png', pos=(5.8, 4.83)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'zom/zom.png', pos=(14.7, 7.56)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'zomdi/zom.png', pos=(10.54, 20.2)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'creature/cre.png', pos=(11.79, 3.23)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'paint1/pnt.png', pos=(1.3, 13.4)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'paint2/pnt.png', pos=(1.3, 19.6)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'paint3/pnt.png', pos=(9.3, 20.8)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'an.png', pos=(14.5, 1.5)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(13.2, 16.3)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(6.3, 24.2)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(2.7, 16.5)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'statue/stat.png', pos=(14.7, 12.3)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'statue2/stat.png', pos=(1.3, 24.5)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'eggs/eg.png', pos=(14.3, 24.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'eggs2/eg.png', pos=(14, 24.3)))




        


        # npc map
        # add_npc(SoldierNPC(game, pos=(11.0, 19.0)))
        # add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        # add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        # add_npc(SoldierNPC(game, pos=(2.0, 20.0)))
        # add_npc(SoldierNPC(game, pos=(4.0, 29.0)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        # add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))

    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)