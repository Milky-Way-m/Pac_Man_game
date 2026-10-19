import map
import curses
def walk(key,player_x,player_y):
    if key == curses.KEY_RIGHT:
        new_x = player_x + 1
        new_y = player_y
    elif key == curses.KEY_LEFT:
        new_x = player_x - 1
        new_y = player_y
    elif key == curses.KEY_UP:
        new_y = player_y - 1
        new_x = player_x
    elif key == curses.KEY_DOWN:
        new_y = player_y + 1
        new_x = player_x
    else:
        new_x = player_x
        new_y = player_y
    return new_y,new_x

