import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Drawing Shapes")
screen.fill((255, 255, 255))

# Set default font size and color
font_size = 24
font_color = (255, 0, 0)

# Initialize the font
font = pygame.font.SysFont("Arial", font_size)

# Main loop
running = True
while running:
    # Get user input
    user_input = input("Enter command: ")

    # Check for valid input
    if user_input.startswith("change size"):
        try:
            new_font_size = int(user_input.split(" ")[2])
            font_size = new_font_size
            font = pygame.font.SysFont("Arial", font_size)
        except ValueError:
            print("Invalid font size")

    elif user_input.startswith("change color"):
        try:
            r, g, b = user_input.split(" ")[2:]
            font_color = (int(r), int(g), int(b))
        except ValueError:
            print("Invalid color")

    elif user_input.startswith("draw line"):
        try:
            x1, y1, x2, y2 = user_input.split(" ")[2:]
            text = font.render("Line", True, font_color)
            # Draw the text on the screen
            screen.blit(text, (0, 0))
            pygame.draw.line(screen, font_color, (int(x1), int(y1)), (int(x2), int(y2)))
        except ValueError:
            print("Invalid line coordinates")

    elif user_input.startswith("draw circle"):
        try:
            x, y, radius = user_input.split(" ")[2:]
            pygame.draw.circle(screen, font_color, (int(x), int(y)), int(radius))
        except ValueError:
            print("Invalid circle coordinates")

    elif user_input.startswith("draw polygon"):
        try:
            points = []
            for point_str in user_input.split(" ")[2:]:
                x, y = point_str.split(",")
                points.append((int(x), int(y)))
            pygame.draw.polygon(screen, font_color, points)
        except ValueError:
            print("Invalid polygon coordinates")

    elif user_input == "end drawing":
        # Save the drawing to a file
        pygame.image.save(screen, "draw.png")
        running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
