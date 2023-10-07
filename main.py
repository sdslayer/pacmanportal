import pygame
from gameboard import board

pygame.init()
WIDTH, HEIGHT = 900, 950
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Portal")

FPS = 60
SPEED = 3
FONT = pygame.font.Font('emulogic.ttf', 20)
level = board # Set level to the tile-based game board we imported

# Load pacman frames
pacman_frames = []
for i in range(4):
    frame_path = f'images/player_images/{i}.png' # Path to the frames
    pacman_frame = pygame.image.load(frame_path).convert_alpha() # Load the frames
    pacman_frame = pygame.transform.scale(pacman_frame, (40, 40)) # Resize pacman frames
    pacman_frames.append(pacman_frame) # Add each resized frame to the array

PACMAN_FRAME_DURATION = 5  # Number of game frames to display each frame
current_frame = 0
frame_counter = 0

PACMAN = pygame.Rect(30, 30, 60, 60) # Draw pacman rectangle

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys_pressed = pygame.key.get_pressed()
        check_movement(keys_pressed, PACMAN)
        update_pacman_frame()  # Update pacman's frame every frame

        draw_screen(level) # Call draw screen and pass the level array to it

    pygame.quit()

def update_pacman_frame():
    global current_frame, frame_counter

    frame_counter += 1 # Increase frame counter (how long its been on screen for)
    if frame_counter >= PACMAN_FRAME_DURATION: # If frame counter > max length of a frame...
        frame_counter = 0 # Set frame counter to 0
        current_frame = (current_frame + 1) % len(pacman_frames) # Set the next frame

def draw_level(level):
     pieceheight = ((HEIGHT - 50) // 32)
     piecewidth = (WIDTH // 30)
     for i in range(len(level)):
          for j in range(len(level[i])):
               if level[i][j] == 1:
                    pygame.draw.circle(WIN, 'white', (j * piecewidth + (0.5 * piecewidth), (i * pieceheight + (0.5 * pieceheight))), 4) # Draw small pellet
               if level[i][j] == 2:
                    pygame.draw.circle(WIN, 'white', (j * piecewidth + (0.5 * piecewidth), (i * pieceheight + (0.5 * pieceheight))), 12) # Draw big pellet

def check_movement(keys_pressed, pacman):
    if keys_pressed[pygame.K_LEFT]:
            pacman.x -= SPEED
    if keys_pressed[pygame.K_RIGHT]:
            pacman.x += SPEED
    if keys_pressed[pygame.K_UP]:
            pacman.y -= SPEED
    if keys_pressed[pygame.K_DOWN]:
            pacman.y += SPEED

def draw_screen(level):
        WIN.fill((0, 0, 0)) # Fill screen with black
        current_pacman_frame = pacman_frames[current_frame] # Get current frame
        WIN.blit(current_pacman_frame, PACMAN.topleft) # Draw current frame to screen at the location of pacman rect
        draw_level(level) # Call draw level function, passes the array
        pygame.display.update()

if __name__ == "__main__":
    main()
