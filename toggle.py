class ToggleButton:
    def __init__(self, x, y, image_on, image_off):
        self.x = x
        self.y = y
        self.image_on = image_on
        self.image_off = image_off
        self.image = self.image_off
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.state = False  # Button starts in the "off" state

    def toggle(self):
        self.state = not self.state
        self.image = self.image_on if self.state else self.image_off

    def draw(self, screen):
        screen.blit(self.image, self.rect)