import json
import random
import os

GRID_LENGTH, GRID_HEIGHT = 7, 7
debug = False


def update_horizontal_options(horizontal_option=[],
                              cords='',
                              Grid_LENGTH=7,
                              already_fired=[]):
  '''
    update horizontal option if applicable
    :param horizontal_option: all current horizontal option ship cord
    :param cords: current cordinates
    :param Grid_LENGTH: grid length
    :param already_fired: list of cordinate thats already fired
    :return: horizontal option
    '''
  if debug:
    print("updating horizontal!!!")
  temp = cords
  i = int(str(ord(cords[0].upper()) - 65))  # convert index 0 to uppercase char
  j = int(cords[1:]) - 1  # get index 1 as integer

  # left
  if j - 1 >= 0:
    position = [i, j - 1]
    letter = temp[0].upper()
    cords = letter + str(position[1] + 1)

    # print("left", cords)
    if cords not in already_fired and cords not in horizontal_option:
      option = [cords, position]
      horizontal_option.append(option)

  # right
  if j + 1 <= Grid_LENGTH - 1:
    position = [i, j + 1]
    letter = temp[0].upper()
    cords = letter + str(position[1] + 1)

    # print("right", cords)
    if cords not in already_fired and cords not in horizontal_option:
      option = [cords, position]
      horizontal_option.append(option)

  return horizontal_option


def update_vertical_options(vertical_option=[],
                            cords='',
                            Grid_LENGTH=7,
                            already_fired=[]):
  '''
    update vertical option if applicable
    :param vertical_option: all vertical_option
    :param cords: cord its checking verticle on
    :param Grid_LENGTH: Grid length
    :param already_fired: spot thats already fired
    :return: vertical option
    '''

  if debug:
    print("updating vertical!!!")
  temp = cords
  i = int(str(ord(cords[0].upper()) - 65))  # convert index 0 to uppercase char
  j = int(cords[1:]) - 1  # get index 1 as integer
  if debug:
    print("vertical option", vertical_option)
    print("already fire", already_fired)
  # top
  if i - 1 >= 0:
    position = [i - 1, j]
    letter = chr(ord(temp[0].upper()) - 1)
    cords = letter + str(position[1] + 1)

    if cords not in already_fired and cords not in vertical_option:

      if debug:
        print('added:', cords)
      option = [cords, position]
      vertical_option.append(option)
  # bot
  if i + 1 <= Grid_LENGTH - 1:
    position = [i + 1, j]
    letter = chr(ord(temp[0].upper()) + 1)
    cords = letter + str(position[1] + 1)

    if cords not in already_fired and cords not in vertical_option:
      if debug:
        print('added:', cords)
      option = [cords, position]
      vertical_option.append(option)

  return vertical_option


def find_all_avaliable_options(cords='', Grid_LENGTH=7, already_fired=[]):
  '''
    finds possible coordinate positions that are valid and not repeated
    :param cords:ex 'a1' str input of cord to check
    :param Grid_LENGTH:length of grid
    :param already_fired: list of option already fired
    :return: list of vertical and horizontal option
    '''

  temp = cords
  i = int(str(ord(cords[0].upper()) - 65))  # convert index 0 to uppercase char
  j = int(cords[1:]) - 1  # get index 1 as integer

  vertical_option = []
  horizontal_option = []
  # top
  if i - 1 >= 0:
    position = [i - 1, j]
    letter = chr(ord(temp[0].upper()) - 1)
    cords = letter + str(position[1] + 1)

    if cords not in already_fired:
      option = [cords, position]
      vertical_option.append(option)
  # bot
  if i + 1 <= Grid_LENGTH - 1:
    position = [i + 1, j]
    letter = chr(ord(temp[0].upper()) + 1)
    cords = letter + str(position[1] + 1)

    if cords not in already_fired:
      option = [cords, position]
      vertical_option.append(option)

  # left
  if j - 1 >= 0:
    position = [i, j - 1]
    letter = temp[0].upper()
    cords = letter + str(position[1] + 1)

    # print("left", cords)
    if cords not in already_fired:
      option = [cords, position]
      horizontal_option.append(option)

  # right
  if j + 1 <= Grid_LENGTH - 1:
    position = [i, j + 1]
    letter = temp[0].upper()
    cords = letter + str(position[1] + 1)

    # print("right", cords)
    if cords not in already_fired:
      option = [cords, position]
      horizontal_option.append(option)

  return [vertical_option, horizontal_option]


def print_mirror_grid(
  grid,
  grid2,
  Row,
  Col,
):
  '''
    print both grids
    :param grid: first grid
    :param grid2: second grid
    :param Row: Row of grids
    :param Col: Col of gird
    :return:
    '''
  # change the number if u want more tabs <---
  tabs = "\t" * 6

  print(" ", end=' ')
  for i in range(Col):
    print(f"{i + 1}", end=" ")

  print(tabs, end="")
  print(" ", end=' ')
  for i in range(Col):
    print(f"{i + 1}", end=" ")

  print()

  for i in range(Row):
    y_label = chr(ord("A") + i)
    print(y_label, end=" ")
    for j in range(Col):
      print(grid[i][j], end=" ")

    print(tabs, end="")
    print(y_label, end=" ")
    for k in range(len(grid[i])):
      print(grid2[i][k], end=" ")

    print()


def make_grid(Row, Col):
  '''
    creates one grid of dimensions Row x Col
    :param Row: Row
    :param Col: Size
    :return: grid
    '''
  grid = []

  for i in range(Row):
    grid.append([' '] * Col)

  return grid


def is_valid_cord(str):
  '''
    return valid is character is [a-g][1-6]
    :param str: str is validing
    :return: True or False
    '''
  if len(str) != 2:
    return False

  if str[0].isalpha() and str[1].isdigit():
    char = str[0]
    num = int(str[1])
    if ord('A') <= ord(char.upper()) <= ord('G') and 1 <= num <= 7:
      return True


def deploy_ship(grid, ship_data, ship_name):
  '''
    deploys ship on grid
    :param grid: grid it deploying
    :param ship_data: ship data that is a dictionary
    :param ship_name: ship_name
    :return:
    '''
  x = ord(ship_data['starting_pos'][0].upper()) - 65
  y = ship_data['starting_pos'][1] - 1
  orientation = ship_data['orientation']

  if ship_name == 'carrier':
    ship_letter = 'c'
  else:
    ship_letter = ship_name[0].upper()

  for i in range(ship_data['size']):
    if orientation == 'h':
      grid[x][y + i] = ship_letter

    else:
      grid[x + i][y] = ship_letter


class ship:
  """
    Objective: This the base class that battleship class will inherit from it will have
    getter and setter for name and location
    """

  def __init__(self):
    # initialize class with empty ship name and location
    self._name = ""
    self._location = ""

  def set_name(self, name):
    # initialize ship name with param: name
    self._name = name

  def set_location(self, location):
    # initialize location name with param: location
    self._location = location

  def get_location(self):
    # accessor for location
    return self._location

  def get_name(self):
    # accessor for name
    return self._name

  def __repr__(self):
    # printable representation for ship name and location
    return "name:" + str(self._name) + " " + "location:" + str(
      self._location) + ' '


class battleship(ship):
  """
    Objective: Battleship class is the class that each player will have list of.
    The ship should know where it is, is it hit , and if it sunk.
    """

  def __init__(self, length, orientation, sunk=False):
    '''
        instantiate a single ship with its length, orientation, and sunk status
        '''
    super().__init__()

    self._length = length
    self._hp = length
    self._ori = orientation
    self._sunk = sunk

  def get_length(self):
    '''
        :return: int for ship length
        '''
    return self._length

  def get_orientation(self):
    '''
        :return: string for ship orientation (horizontal or vertical)
        '''
    return self._ori

  def is_hit(self):
    '''
        decreases ship health if hit
        :return: True if hit, False if not hit
        '''
    if self._hp == 0:
      raise Exception("length is 0")
      return
    self._hp -= 1

    if self._hp == 0:
      self._sunk = True

  def is_sunk(self):
    '''
        checks if ship health is zero
        :return: True if sunk or False if not
        '''
    return self._hp == 0

  def __repr__(self):
    '''
        printable representation for ship length, orientation, health, and sunk status
        '''
    info = super().__repr__() + "Length:" + str(
      self._length) + " " + "orientaion:" + str(self._ori) + " hp:" + str(
        self._hp)
    if self._sunk:
      info += " sunk:T"
    else:
      info += " sunk:F"

    return info


class player:
  """
    Objective: The player class load json will the player's json file and put all set ship and initalize it       hidden board and it own list of ship.
    -it can select a target on board
    -check it own hidden at specific cordinate
    -update its list of ship it one of them is hit
    -check it still has any ship that arent sunk
    -print its own hidden grid
    """

  def __init__(self, json_file_name):
    '''
        instantiate player with hidden board and list of ships (read from json file)
        '''
    file_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))

    data_path = os.path.join(project_path, 'player_ships.json')

    self._hidden_board = make_grid(GRID_HEIGHT, GRID_LENGTH)
    self._list_of_ship = []

    # f = open(data_path)

    # original open
    f = open(json_file_name)

    data = json.load(f)
    f.close()

    #deploy the ship on grid
    for ship_name in data:
      ship_data = data[ship_name]

      bship = battleship(ship_data['size'], ship_data['orientation'])

      bship.set_name(ship_name)
      bship.set_location(ship_data['starting_pos'])

      self._list_of_ship.append(bship)
      deploy_ship(self._hidden_board, ship_data, ship_name)

  def select_target(self):
    '''
        :return: cord of 'a1',[x,y] and thats corresponding to it
        '''

    target = input("Select a coordinate to shoot: ")

    while not is_valid_cord(target):
      print(f"['{target}'] was an invalid input")
      target = input("Select a coordinate to shoot: ")

    x = int(str(ord(target[0].upper()) - 65))
    y = int(target[1:]) - 1

    cord = [target, [x, y]]

    return cord

  def check_hidden(self, cord):
    '''
        :param cord: check cordinates in own board
        :return: string of data in hidden board
        '''
    i = int(str(ord(cord[0].upper()) - 65))
    j = int(cord[1:]) - 1

    return self._hidden_board[i][j]

  def is_hit(self, ship_name):
    '''
        :param ship_name: checks if ship name in own board is hit
        '''
    for s in self._list_of_ship:
      if s.get_name() == ship_name:
        s.is_hit()

  def is_sunk(self, ship_name):
    '''
        :param ship_name: checks if ship_name is in list of ships
        :return: True if ship is sunk, False if ship is not sunk
        '''
    for a_ship in self._list_of_ship:
      if a_ship.get_name() == ship_name:

        return a_ship.is_sunk()

    return False

  def has_ship(self):
    '''
        :return: True if list contains ship, False if list does not have ship
        '''
    for ship in self._list_of_ship:
      # if any ship not sunk return true
      if not ship.is_sunk():
        return True
    # return false otherwise
    return False

  def print_board(self):
    '''
        printable representation of board
        '''
    print(" ", end=' ')
    for i in range(GRID_LENGTH):
      print(f"{i + 1}", end=" ")
    print()

    for i in range(GRID_LENGTH):
      print(chr(ord("A") + i), end=" ")
      for j in range(GRID_LENGTH):
        print(self._hidden_board[i][j], end=" ")

      print()

  def get_list_of_ship(self):
    '''
        :return: list of player ships
        '''
    return list(self._list_of_ship)


class ai:
  """
    Objective:The ai class is player 2 and it will randomly fire until ship is hit and if ship is hit
    it will turn on hunt to finish of the ship
    -it has list of random option it can fire and will remove option if need
    -it can randomly select a target on board
    -check it own hidden at specific cordinate
    -update its list of ship it one of them is hit
    -check it still has any ship that arent sunk
    -print its own hidden grid
    """

  def __init__(self, json_file_name):
    '''
        read ai ship placement from json file
        '''
    file_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))

    data_path = os.path.join(project_path, 'enemy_ships.json')

    self._hidden_board = make_grid(GRID_HEIGHT, GRID_LENGTH)
    self._list_of_ship = []
    self._option = []

    f = open(json_file_name)

    # f = open(data_path)
    data = json.load(f)

    f.close()

    #initalize players own board
    for ship_name in data:
      ship_data = data[ship_name]

      bship = battleship(ship_data['size'], ship_data['orientation'])

      bship.set_name(ship_name)
      bship.set_location(ship_data['starting_pos'])

      self._list_of_ship.append(bship)
      deploy_ship(self._hidden_board, ship_data, ship_name)

    #make options
    for i in range(GRID_LENGTH):
      x = chr(ord('A') + i)
      for j in range(GRID_LENGTH):
        y = j + 1
        self._option.append([x, y])
    #debug
    # for op in self._option:
    #     print(op)

  def remove_option(self, option):
    '''
        prevent repeating coordinates to be chosen
        '''
    cord = [str(option[0]).upper(), int(option[1])]
    if debug:
      print('removing option:', cord)
    self._option.remove(cord)

  def select_random(self):
    '''
        select a random coordinate from a 7x7 grid
        :return: string of coordinate 
        '''
    size = len(self._option)

    option = self._option[random.randint(0, size - 1)]

    x = int(str(ord(option[0].upper()) - 65))
    y = int(option[1]) - 1

    option = str(option[0]) + str(option[1])
    cord = [option, [x, y]]

    #cord is list of values related to postion [cord ex: 'a1', 'b2' postion related to cord[0,0] for a1]

    return cord

  def is_hit(self, ship_name):
    '''
        :param ship_name: check if name is in list of ships and calls is_hit()
        '''
    for ele in self._list_of_ship:
      if ele.get_name() == ship_name:
        ele.is_hit()

  def is_sunk(self, ship_name):
    '''
        :param ship_name: check if name is sunk (health of zero)
        :return: True if sunk, False if not sunk
        '''
    for a_ship in self._list_of_ship:
      if a_ship.get_name() == ship_name:
        return a_ship.is_sunk()

    return False

  def has_ship(self):
    '''
        :return: True if ship is in list, False if not
        '''
    for ship in self._list_of_ship:
      # if any ship not sunk return true
      if not ship.is_sunk():
        return True
    # return false otherwise
    return False

  def check_hidden(self, cord):
    '''
        :param cord: converts string coord to int coord
        :return: data in hidden_board at coord
        '''
    i = int(str(ord(cord[0].upper()) - 65))
    j = int(cord[1:]) - 1
    return self._hidden_board[i][j]

  def print_board(self):
    '''
        printable representation of board
        '''
    print(" ", end=' ')
    for i in range(GRID_LENGTH):
      print(f"{i + 1}", end=" ")
    print()

    for i in range(GRID_LENGTH):
      print(chr(ord("A") + i), end=" ")
      for j in range(GRID_LENGTH):
        print(self._hidden_board[i][j], end=" ")

      print()

  def get_list_of_ship(self):
    '''
        :return: list of ships
        '''
    return list(self._list_of_ship)


class battleship_game:
  """
    Objective:The main game loop and it initalize the player and ai
    the game loop will alternate player's turn and it ai hit a ship it turn on hunt mode for p2
    """

  def __init__(self):
    '''
        instantiate battleship_game with data from both player and enemy json ships
        '''
    self._p1 = player('player_ships.json')
    self._p2 = ai('enemy_ships.json')
    self._p1_display_board = make_grid(GRID_HEIGHT, GRID_HEIGHT)
    self._p2_display_board = make_grid(GRID_HEIGHT, GRID_HEIGHT)

  def hit_ship(self, character):
    '''
        :param character: beginning letter of ship name
        :return: full name of ship
        '''
    if character == 'B':
      return 'battleship'
    elif character == "S":
      return 'submarine'
    elif character == 'c':
      return 'carrier'
    elif character == "D":
      return 'destroyer'
    elif character == "C":
      return 'cruiser'

  def print_display_board(self):
    '''
        prints one 7x7 board
        '''
    print('  A.I. BOARD', "\t" * 7, " PLAYER BOARD")
    print(" ", end="")
    for i in range(GRID_LENGTH):
      print("--", end='')
    print("\t" * 7, end="")
    print(" ", end="")
    for i in range(GRID_LENGTH):
      print("--", end='')
    print()

    print_mirror_grid(self._p1_display_board, self._p2_display_board,
                      GRID_HEIGHT, GRID_LENGTH)

  # main game loop
  def run(self):
    '''
        main game loop player take turn shooting ship and if ai hit a shot it turn on hunt mode
        :return:
        '''

    if debug:

      self._p2.print_board()
      self._p1.print_board()

    Player_Turn = 1
    self.print_display_board()
    p1_fired = []
    p2_fired = []
    p2_hunt_mode = False
    vertical_hit = False
    horizontal_hit = False
    update_option = True
    p2_last_hit = ''
    missed = " "

    while self._p1.has_ship() and self._p2.has_ship():
      if Player_Turn == 1:

        print("Player 1 Turn", end="\n" * 2)

        cord = self._p1.select_target()
        while cord[1] in p1_fired:
          print("P1 have already selected this coordinates!")
          cord = self._p1.select_target()
        p1_fired.append(cord[1])

        p2_tile = self._p2.check_hidden(cord[0])
        p2_x, p2_y = cord[1]

        if p2_tile != missed:

          self._p2_display_board[p2_x][p2_y] = p2_tile

          ship_name = self.hit_ship(p2_tile)
          print(f"P1 has hit the {ship_name}!")
          self._p2.is_hit(ship_name)

          # print sunk

          if self._p2.is_sunk(ship_name):
            print(f"P1 have sunk the {ship_name}")

            if self._p2.has_ship() == False:
              self.print_display_board()
              print("P1 has won!")
              self.print_display_board()
              break

          # debug
          # for x in self._p2.get_list_of_ship():
          #     if x.get_name() == ship_name:
          #         print(x)

        else:
          # update board
          self._p2_display_board[p2_x][p2_y] = 'x'
          print("P1 missed!")

        self.print_display_board()
        # update turn
        Player_Turn = 2
      elif Player_Turn == 2:
        print("Player 2 Turn", end="\n" * 2)
        # player2 turn
        if not p2_hunt_mode:
          # debug
          # ['g', 5]->(6, 4)

          # cord = ['G5', [6, 4]]

          cord = self._p2.select_random()
          p1_tile = self._p1.check_hidden(cord[0])
          p1_x, p1_y = cord[1]

        if p2_hunt_mode:
          if update_option:
            all_options = find_all_avaliable_options(p2_last_hit, GRID_LENGTH,
                                                     p2_fired)
            vertical_options = all_options[0]
            horizontal_options = all_options[1]
            update_option = False
          # rng decide vertical or horizontal first

          if vertical_hit:

            cord = vertical_options.pop(
              random.randint(0,
                             len(vertical_options) - 1))

            p1_tile = self._p1.check_hidden(cord[0])
            p1_x, p1_y = cord[1]
            if p1_tile != missed:
              p2_last_hit = cord[0]
              vertical_hit = True
              update_vertical_options(vertical_options, p2_last_hit,
                                      GRID_LENGTH, p2_fired)

          elif horizontal_hit:

            cord = horizontal_options.pop(
              random.randint(0,
                             len(horizontal_options) - 1))
            if debug:
              print(f'first select cord:', cord)

            p1_tile = self._p1.check_hidden(cord[0])
            p1_x, p1_y = cord[1]
            if p1_tile != missed:
              p2_last_hit = cord[0]
              horizontal_hit = True
              update_horizontal_options(horizontal_options, p2_last_hit,
                                        GRID_LENGTH, p2_fired)
            if debug:
              print('horizontal_options after update:', horizontal_options)

          # rng decide vertical or horizontal first if both vertical and horizontal hit false
          if not vertical_hit and not horizontal_hit:
            if debug:
              print("First pick")
              self._p1.print_board()
            go_vertical = 0
            go_horizontal = 1

            rng = random.randint(go_vertical, go_horizontal)

            if rng == go_horizontal and len(horizontal_options) > 0:
              cord = horizontal_options.pop(
                random.randint(0,
                               len(horizontal_options) - 1))
              if debug:
                print("first select cord:", cord)
                print("horizontal:", horizontal_options)
              p1_tile = self._p1.check_hidden(cord[0])
              p1_x, p1_y = cord[1]
              if p1_tile != missed:
                p2_last_hit = cord[0]
                horizontal_hit = True
                update_horizontal_options(horizontal_options, p2_last_hit,
                                          GRID_LENGTH, p2_fired)

            elif rng == go_vertical or len(vertical_options) > 0:
              # random missed and pick vertical again but no vertical to be selected
              if len(vertical_options) == 0:

                cord = horizontal_options.pop(
                  random.randint(0,
                                 len(horizontal_options) - 1))
                if debug:
                  print("No vertical option")
                  print("horizontal:", horizontal_options)
                p1_tile = self._p1.check_hidden(cord[0])
                p1_x, p1_y = cord[1]
                if p1_tile != missed:
                  p2_last_hit = cord[0]
                  horizontal_hit = True
                  update_horizontal_options(horizontal_options, p2_last_hit,
                                            GRID_LENGTH, p2_fired)

              # procceed as normal
              else:

                # if debug:
                #     print("vertical:", vertical_options)
                #
                # if debug:
                #     print("first select cord:", cord)
                cord = vertical_options.pop(
                  random.randint(0,
                                 len(vertical_options) - 1))
                p1_tile = self._p1.check_hidden(cord[0])
                p1_x, p1_y = cord[1]
                if p1_tile != missed:
                  p2_last_hit = cord[0]
                  vertical_hit = True
                  update_vertical_options(vertical_options, p2_last_hit,
                                          GRID_LENGTH, p2_fired)
                else:
                  if debug:
                    print("RNG", rng)
                    print('BUG!!!')

        print("P2 selected:", cord[0])
        p2_fired.append(cord[0])
        self._p2.remove_option(cord[0])
        if debug:
          print('P2 fired:', p2_fired)
        # check tile at location

        if p1_tile != missed:
          p2_hunt_mode = True
          p2_last_hit = cord[0]
          if debug:
            print('Hunt Mode ON Last hit', p2_last_hit)

          # update display board
          self._p1_display_board[p1_x][p1_y] = p1_tile
          # get ship name and update ship hp in player's list of ship

          ship_name = self.hit_ship(p1_tile)
          print(f"P2 has hit the {ship_name}!")
          self._p1.is_hit(ship_name)

          # debug
          if debug:
            for x in self._p1.get_list_of_ship():
              print(x)

          # print sunk

          if self._p1.is_sunk(ship_name):
            print(f"P2 have sunk the {ship_name}")
            p2_hunt_mode = False
            update_option = True
            vertical_hit = False
            horizontal_hit = False
            if debug:
              print("HUNT MODE OFF")

            if self._p1.has_ship() == False:
              print("P2 has won!")
              self.print_display_board()
              break

          # debug
          # for x in self._p1.get_list_of_ship():
          #     if x.get_name() == ship_name:
          #         print(x)

        else:
          self._p1_display_board[p1_x][p1_y] = 'x'
          print("P2 missed!")

        self.print_display_board()
        # update turn

        # update turn
        Player_Turn = 1
