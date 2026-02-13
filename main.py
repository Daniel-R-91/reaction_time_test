import pygame
from random import randint

def main():
    pygame.init()

    screen_height = 600
    screen_width = 800

    screen = pygame.display.set_mode((screen_width, screen_height))

    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Reaction Time Test")

    clock = pygame.time.Clock()

    font_1 = pygame.font.SysFont("verdana", 60)
    font_2 = pygame.font.SysFont("verdana", 25)

    menu_text_1_surface = font_1.render("Reaction Time Test", True, (255, 255, 255))
    menu_text_1_rect = menu_text_1_surface.get_rect(center=(screen_width / 2, 225))

    menu_text_2_surface = font_2.render("When the red box turns green, click as quickly as you can.", True, (255, 255, 255))
    menu_text_2_rect = menu_text_2_surface.get_rect(center=(screen_width / 2, 300))

    menu_text_3_surface = font_2.render("Click anywhere to start.", True, (255, 255, 255))
    menu_text_3_rect = menu_text_3_surface.get_rect(center=(screen_width /2, 335))

    menu_text_4_surface = font_1.render("Too soon!", True, (255, 255, 255))
    menu_text_4_rect = menu_text_4_surface.get_rect(center=(screen_width / 2, 250))

    menu_text_5_surface = font_2.render("Click to try again!", True, (255, 255, 255))
    menu_text_5_rect = menu_text_5_surface.get_rect(center=(screen_width / 2, 325))

    icon_2_surface = pygame.image.load("images/icon_2.png").convert_alpha()
    icon_2_surface.set_colorkey((0, 0, 0))
    icon_2_rect = (icon_2_surface.get_rect(center=(375, 100)))

    running = True
    game_active = False
    too_soon = False
    result = False

    reaction_time = 0

    start_time = pygame.time.get_ticks()
    wait_time = randint(1000, 5000)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if not game_active and not too_soon and not result:
                    game_active = True
                    start_time = pygame.time.get_ticks()
                    wait_time = randint(1000, 5000)

                elif game_active:
                    current_time = pygame.time.get_ticks()
                    if current_time - start_time < wait_time:
                        too_soon = True
                        game_active = False
                        result = False
                    else:
                        too_soon = False
                        game_active = False
                        result = True
                        reaction_time = current_time - (start_time + wait_time)

                elif too_soon or result:
                    too_soon = False
                    result = False
                    game_active = True
                    start_time = pygame.time.get_ticks()
                    wait_time = randint(1000, 5000)

        if running:
            pygame.display.update()
            clock.tick(60)

            if too_soon:
                screen.fill((0, 150, 255))
                screen.blit(menu_text_4_surface, menu_text_4_rect)
                screen.blit(menu_text_5_surface, menu_text_5_rect)

            elif result:
                screen.fill((0, 150, 255))

                reaction_text_surface = font_1.render(f"{reaction_time} ms", True, (255, 255, 255))
                reaction_text_rect = reaction_text_surface.get_rect(center=(screen_width / 2, 250))
                screen.blit(reaction_text_surface, reaction_text_rect)
                screen.blit(menu_text_5_surface, menu_text_5_rect)

            elif game_active:
                current_time = pygame.time.get_ticks()
                if current_time - start_time >= wait_time:
                    screen.fill((0, 255, 0))
                else:
                    screen.fill((180, 0, 0))

            else:
                screen.fill((0, 150, 255))
                screen.blit(menu_text_1_surface, menu_text_1_rect)
                screen.blit(menu_text_2_surface, menu_text_2_rect)
                screen.blit(menu_text_3_surface, menu_text_3_rect)
                screen.blit(icon_2_surface, icon_2_rect)

    pygame.quit()

if __name__ == "__main__":
    main()