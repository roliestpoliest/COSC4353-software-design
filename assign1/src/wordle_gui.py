from enum import Enum
import pygame, sys
import threading as th
from wordle import TallyMatch, play, GameStatus, GamePlay
globals().update(TallyMatch.__members__)
globals().update(GameStatus.__members__)
globals().update(GamePlay.__members__)

class Dimension(Enum):
  SCREEN_WIDTH = 450
  SCREEN_HEIGHT = 540
  GRID__WIDTH = 300
  GRID__HEIGHT = 360
  CELL_GAP = 8
  CELL_SIZE = 50
  PADDING = 4
  OUTLINE_THICKLINE = 2
  SUBMIT_BUTTON_WIDTH = 120
  SUBMIT_BUTTON_HEIGHT = 50

class Color(Enum):
  BLACK = "#121213"
  WHITE = "#F8F8F8"
  GREEN = "#538D4E"
  YELLOW = "#B59F3B"
  LIGHT_GREY = "#808384"
  DARK_GREY = "#39393B"

class WordleUI:
  def __init__(self, target = "FAVOR"):
    pygame.init()

    self.target = target
    self.guess = ""
    self.font = pygame.font.Font(None, 36)
    self.clear_message_flag = False

    self.game_play = {
      GamePlay.ATTEMPTS: 0,
      GamePlay.TALLY_RESPONSE: [],
      GamePlay.GAME_STATUS: GameStatus.IN_PROGRESS,
      GamePlay.MESSAGE: ""
    }
  
  def draw_screen(self):
    self.screen = pygame.display.set_mode([Dimension.SCREEN_WIDTH.value, Dimension.SCREEN_HEIGHT.value])
    self.screen.fill(Color.BLACK.value)
    pygame.display.set_caption("Wordle")

    self.draw_grid_div()
    self.draw_grid()
    self.draw_submit_button()
    self.draw_message()

  def draw_grid_div(self):
    total_height = Dimension.GRID__HEIGHT.value + Dimension.SUBMIT_BUTTON_HEIGHT.value + Dimension.PADDING.value
    grid__top_y = (Dimension.SCREEN_HEIGHT.value - total_height) // 2

    self.grid_ = pygame.Surface((Dimension.GRID__WIDTH.value, Dimension.GRID__HEIGHT.value))
    self.grid_.fill(Color.BLACK.value)

    self.grid__rect = self.grid_.get_rect(midtop=(Dimension.SCREEN_WIDTH.value // 2, grid__top_y))
    self.screen.blit(self.grid_, self.grid__rect)

  def draw_grid(self):
    start_x, start_y = self.calculate_cell_position()

    for row in range(6):
      for col in range(5):
        self.draw_cell(start_x, start_y, row, col)

  def draw_message_div(self):
    message_bg_width = Dimension.GRID__WIDTH.value
    message_bg_height = 30

    message_x = self.grid__rect.left
    message_y = self.grid__rect.top - message_bg_height - Dimension.PADDING.value

    self.message_rect = pygame.Rect(message_x, message_y, message_bg_width, message_bg_height)
    pygame.draw.rect(self.screen, Color.BLACK.value, self.message_rect)

  def draw_message(self, text=""):
    self.draw_message_div()
    self.draw_text(text)

  def message_delay(self, text, delay):
    def message_delay_helper():
      self.clear_message_flag = True

    self.draw_message(text)
    pygame.display.update()
    timer = th.Timer(delay / 1000, message_delay_helper)
    timer.start()

  def draw_text_bg(self, text):
    if text:
      text_bg_width = self.text_rect.width + Dimension.PADDING.value * 2
      text_bg_height = self.text_rect.height + Dimension.PADDING.value * 2
      text_bg_x = self.text_rect.centerx - text_bg_width // 2
      text_bg_y = self.text_rect.centery - text_bg_height // 2

      text_bg_rect = pygame.Rect(text_bg_x, text_bg_y, text_bg_width, text_bg_height)
      pygame.draw.rect(self.screen, Color.WHITE.value, text_bg_rect)

  def draw_text(self, text=""):
    font = pygame.font.Font(None, 25)

    text_surface = font.render(text, True, Color.BLACK.value)
    self.text_rect = text_surface.get_rect(center=self.message_rect.center)

    self.draw_text_bg(text)
    self.screen.blit(text_surface, self.text_rect)

  def draw_submit_button(self, bg_color = Color.DARK_GREY.value):
    button_y = self.grid__rect.bottom + Dimension.PADDING.value
    button_x = self.grid__rect.left + (self.grid__rect.width - Dimension.SUBMIT_BUTTON_WIDTH.value) // 2

    self.button_rect = pygame.Rect(button_x, button_y, Dimension.SUBMIT_BUTTON_WIDTH.value, Dimension.SUBMIT_BUTTON_HEIGHT.value)
    pygame.draw.rect(self.screen, bg_color, self.button_rect)
    
    text_surface = self.font.render("SUBMIT", True, Color.WHITE.value)
    self.text_rect = text_surface.get_rect(center=(button_x + Dimension.SUBMIT_BUTTON_WIDTH.value // 2, button_y + Dimension.SUBMIT_BUTTON_HEIGHT.value // 2))
    self.screen.blit(text_surface, self.text_rect)

  def draw_cell(self, start_x, start_y, row, col, text="", outline_color = Color.DARK_GREY.value, fill_color = Color.BLACK.value):
    cell_x = start_x + (Dimension.CELL_SIZE.value + Dimension.CELL_GAP.value) * col
    cell_y = start_y + (Dimension.CELL_SIZE.value + Dimension.CELL_GAP.value) * row
    self.outline_cell(cell_x, cell_y, outline_color)
    self.fill_cell(cell_x, cell_y, fill_color)

    if text:
      self.draw_letter(text, cell_x, cell_y)

  def draw_letter(self, text, cell_x, cell_y):
    text_surface = self.font.render(text, True, Color.WHITE.value)
    text_rect = text_surface.get_rect(center=(cell_x + Dimension.CELL_SIZE.value // 2, cell_y + Dimension.CELL_SIZE.value // 2))
    self.screen.blit(text_surface, text_rect)

  def outline_cell(self, cell_x, cell_y, outline_color = Color.DARK_GREY.value):
    outline_thickness = Dimension.OUTLINE_THICKLINE.value
    pygame.draw.rect(self.screen, outline_color, (cell_x - outline_thickness, cell_y - outline_thickness, Dimension.CELL_SIZE.value + outline_thickness * 2, Dimension.CELL_SIZE.value + outline_thickness * 2), outline_thickness)

  def fill_cell(self, cell_x, cell_y, fill_color):
    pygame.draw.rect(self.screen, fill_color, (cell_x, cell_y, Dimension.CELL_SIZE.value, Dimension.CELL_SIZE.value))
  
  def update_guess_row(self):
    start_x, start_y = self.calculate_cell_position()

    for cell in range(5):
      self.draw_cell(start_x, start_y, self.game_play[GamePlay.ATTEMPTS], cell, self.guess[cell] if cell < len(self.guess) else "")

  def calculate_cell_position(self):
    grid_width = 5 * Dimension.CELL_SIZE.value + 4 * Dimension.CELL_GAP.value
    grid_height = 6 * Dimension.CELL_SIZE.value + 5 * Dimension.CELL_GAP.value

    start_x = self.grid__rect.left + (self.grid_.get_width() - grid_width) // 2
    start_y = self.grid__rect.top + (self.grid_.get_height() - grid_height) // 2

    return start_x, start_y

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.process_quit_event()
      elif event.type == pygame.KEYDOWN:
        self.handle_keydown(event)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        self.process_mouse_click(event)

  def handle_keydown(self, event):
    if event.key == pygame.K_RETURN:
      self.process_submit_button()
    elif event.key == pygame.K_BACKSPACE:
      self.process_backspace_key()
    else:
      self.process_alpha_key(event)

  def process_submit_button(self):
    if len(self.guess) == 5:
      self.game_play = play(self.game_play[GamePlay.ATTEMPTS], self.target, self.guess)
      self.deactivate_button()
      self.display_guess_result()
      self.guess = ""

      self.draw_message(self.game_play[GamePlay.MESSAGE])
    else:
      self.message_delay("Not enough letters", 1000)
  
  def display_guess_result(self):
    start_x, start_y = self.calculate_cell_position()

    for cell in range(5):
      cell_color = self.get_cell_color(cell)
      self.draw_cell(start_x, start_y, self.game_play[GamePlay.ATTEMPTS] - 1, cell, self.guess[cell], cell_color, cell_color)
      pygame.display.update()
      pygame.event.wait(300)

  def get_cell_color(self, cell):
    color_map = {
      EXACT_MATCH: Color.GREEN.value,
      DIFFERENT_POSITION: Color.YELLOW.value,
      NOT_IN_WORD: Color.DARK_GREY.value
    }
    return color_map.get(self.game_play[GamePlay.TALLY_RESPONSE][cell])

  def process_backspace_key(self):
    if len(self.guess) > 0:
      self.delete_letter()
    
    self.activate_button() if len(self.guess) == 5 else self.deactivate_button()

  def process_alpha_key(self, event):
    key_input = event.unicode.upper()
    if key_input.isalpha() and len(self.guess) < 5:
      self.add_letter(key_input)
    
    self.activate_button() if len(self.guess) == 5 else self.deactivate_button()

  def process_mouse_click(self, event):
    if self.button_rect.collidepoint(event.pos):
      self.process_submit_button()

  def activate_button(self):
    self.draw_submit_button(Color.LIGHT_GREY.value)
 
  def deactivate_button(self):
    self.draw_submit_button(Color.DARK_GREY.value)

  def delete_letter(self):
    self.guess = self.guess[:-1]
    self.update_guess_row()

  def add_letter(self, key_input):
    self.guess += key_input
    self.update_guess_row()

  def check_hover_over_submit_button(self):
    mouse_pos = pygame.mouse.get_pos()

    if self.button_rect.collidepoint(mouse_pos):
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
      self.reset_cursor()
  
  def reset_cursor(self):
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

  def reset_clear_message_flag(self):
    self.draw_message("")
    pygame.display.update()
    self.clear_message_flag = False

  def process_quit_event(self):
    pygame.quit()
    sys.exit()
  
  def clear_ending_message(self, delay):
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < delay:
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.process_quit_event()

    self.reset_clear_message_flag()

  def game_loop(self):
    while self.game_play[GamePlay.GAME_STATUS] == IN_PROGRESS:
      if self.clear_message_flag:
        self.reset_clear_message_flag()
      pygame.display.update()

      self.handle_events()
      self.check_hover_over_submit_button()

    self.reset_cursor()
    self.clear_ending_message(1500)
    self.wait_to_quit()

  def wait_to_quit(self):
    waiting_for_user_to_quit = True
    while waiting_for_user_to_quit:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          waiting_for_user_to_quit = False
          pygame.quit()

  def start_game(self):
    self.draw_screen()
    self.game_loop()    

if __name__ == "__main__":
  wordle = WordleUI()
  wordle.start_game()
