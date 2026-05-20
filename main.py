import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup complete")


print("loop start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("loop end")
            exit()
