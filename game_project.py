import curses
import time
import map
from controls import walk
from monster import Ghost

def game(stdscr):
    last_time = time.time()
    ghost = Ghost(14,13)
    player_x = 5
    player_y = 1
    for y, row in enumerate(map.map1):
        stdscr.addstr(y, 0, row)
    stdscr.addch(player_y, player_x, '@')
    stdscr.addch(ghost.ghost_y,ghost.ghost_x,'G')
    stdscr.refresh()
    while True:
        now_time = time.time()
        stdscr.nodelay(True)
        key = stdscr.getch()
        if key != -1:
            y_new, x_new = walk(key, player_x, player_y)

            if map.is_walkable(y_new, x_new):
                stdscr.addch(player_y, player_x, ' ')

                player_y = y_new
                player_x = x_new

                stdscr.addch(player_y, player_x, '@')
        if player_x == ghost.ghost_x and player_y == ghost.ghost_y:
            break

        if now_time - last_time >= 0.5:
            old_ghost_x = ghost.ghost_x
            old_ghost_y = ghost.ghost_y
            ghost.move(map.map1,player_x,player_y)
            stdscr.addch(old_ghost_y,old_ghost_x,' ')
            stdscr.addch(ghost.ghost_y,ghost.ghost_x, 'G')
            last_time = now_time
        if player_x == ghost.ghost_x and player_y == ghost.ghost_y:
            break

        stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.clear()
    stdscr.addstr(4, 10, "Ты проиграл! :(")
    stdscr.refresh()
    stdscr.getch()
# Вместо простого curses.wrapper(game) напишите:
if __name__ == "__main__":
    try:
        curses.wrapper(game)
    except Exception as e:
        import traceback
        print("\n=== ИГРА УПАЛА С ОШИБКОЙ ===")
        traceback.print_exc()
        print("===========================")
        input("\nНажмите Enter для выхода...") # Держит окно PowerShell открытым