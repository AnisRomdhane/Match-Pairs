import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Set up game variables
width, height = 800, 600
card_size = 100
background_color = (255, 255, 255)
card_back_color = (200, 200, 200)
# Image File
images_folder = 'ImagePairs'
images = ['spongebob1.gif', 'sponge.jpg', 'dog.png', 'squid.jpg', 'sponge.jpg', 'spongebob1.gif']
cards = images * 2
random.shuffle(cards)

# Initialize the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Memory Game")

# Load images
card_back = pygame.transform.scale(pygame.image.load(os.path.join(images_folder, 'dog.png')), (card_size, card_size))
card_images = [pygame.transform.scale(pygame.image.load(os.path.join(images_folder, image)), (card_size, card_size)) for image in cards]

# Define cards
revealed_cards = [False] * len(cards)
selected_cards = []
pairs_found = 0

# Set up fonts
font = pygame.font.Font(None, 36)

# Function to draw the cards on the screen
def draw_cards():
    for i in range(len(cards)):
        if not revealed_cards[i]:
            pygame.draw.rect(screen, card_back_color, (i % 4 * card_size, i // 4 * card_size, card_size, card_size))
        else:
            screen.blit(card_images[i], (i % 4 * card_size, i // 4 * card_size))

# Function to check if two cards are identical
def are_identical(index1, index2):
    return cards[index1] == cards[index2]

# Main game loop
attempts = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and len(selected_cards) < 2:
            x, y = event.pos
            card_index = x // card_size + (y // card_size) * 4

            if not revealed_cards[card_index]:
                revealed_cards[card_index] = True
                selected_cards.append(card_index)

    screen.fill(background_color)
    draw_cards()

    if len(selected_cards) == 2:
        pygame.time.delay(500)  # Delay to show the selected cards
        attempts += 1
        if are_identical(selected_cards[0], selected_cards[1]):
            pairs_found += 1
            if pairs_found == len(images):
                score_text = font.render(f"Congratulations! You found all pairs in {attempts} attempts.", True, (0, 0, 0))
                screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()
        else:
            revealed_cards[selected_cards[0]] = False
            revealed_cards[selected_cards[1]] = False

        selected_cards = []

    # Display attempts
    attempts_text = font.render(f"Attempts: {attempts}", True, (0, 0, 0))
    screen.blit(attempts_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(1)
