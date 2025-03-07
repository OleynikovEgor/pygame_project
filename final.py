import pygame


def final(winner, time):
    screen = pygame.display.set_mode((447, 248))
    pygame.font.init()
    pygame.display.set_caption('Поздравляем!')
    final_image = pygame.image.load("final.jpg")
    final_image = pygame.transform.scale(final_image, (447, 248))
    font = pygame.font.Font(None, 47)
    text = font.render(f'{winner}!', True, (255, 37, 37))
    text_rect = (100, 20)
    text_time_rect = (50, 80)
    text_time = font.render(f'Время: {time // 60} мин {time % 60} с', True, (255, 37, 37))
    rec_rect = (50, 140)
    if winner == 'Победил игрок':
        with open('record', 'r', encoding='utf-8') as file:
            content = file.readline().strip()
            rec_time = int(content)
            text_record = font.render(f'Рекорд: {int(rec_time) // 60} мин {int(rec_time) % 60} с', True, (255, 37, 37))
    running = True
    while running:
        screen.fill((51, 153, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(final_image, (0, 0))
        screen.blit(text_time, text_time_rect)
        screen.blit(text, text_rect)
        if winner == 'Победил игрок':
            screen.blit(text_record, rec_rect)
        pygame.display.flip()
