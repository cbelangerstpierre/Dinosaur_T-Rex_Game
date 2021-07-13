import pygame
import MainVar


class Events:
    @staticmethod
    def jump_pressed(events):
        click_event = False
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                click_event = True
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN] or click_event:
            return True
        else:
            return False

    @staticmethod
    def quit_pressed(events):
        quit_event = False
        for event in events:
            if event.type == pygame.QUIT:
                quit_event = True
        return quit_event

    @staticmethod
    def dino_jump(events, dino, fps):
        if dino.onSurface():
            dino.setSpeed(dino.getInitialSpeed())
            if Events.jump_pressed(events):
                dino.jump()
        else:
            dino.finish_jump(fps)

    @staticmethod
    def quit_game(events):
        if Events.quit_pressed(events):
            MainVar.MainVar.run = False
