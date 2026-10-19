def bfs(game_map,ghost_x,ghost_y,player_x,player_y):
    queue = [(ghost_x,ghost_y)]
    visited = [(ghost_x,ghost_y)]
    parent = {}
    actions = [(1,0),(-1,0), (0,-1),(0,1)]
    target_found = False
    while queue:
        cell = queue.pop(0)
        if cell[0] == player_x and cell[1] == player_y:
            target_found = True
            break
        for x, y in actions:
            neightbor = (cell[0] + x,cell[1] + y)
            if (0 <= neightbor[1] < len(game_map)) and (0 <= neightbor[0] < len(game_map[0])):
                if game_map[neightbor[1]][neightbor[0]] == ' ':
                   if neightbor not in visited:
                      visited.append(neightbor)
                      parent[neightbor] = cell
                      queue.append(neightbor)
    if target_found == False:
        return  None
    b = []
    c = (player_x,player_y)
    while c != (ghost_x,ghost_y):
        b.append(c)
        c = parent[c]
    return b[-1]
class Ghost:
    def __init__(self,ghost_x,ghost_y):
        self.ghost_x = ghost_x
        self.ghost_y = ghost_y
    def move(self,game_map,player_x,player_y):
        next_step = bfs(game_map,self.ghost_x,self.ghost_y,player_x,player_y)
        if next_step:
            self.ghost_x = next_step[0]
            self.ghost_y = next_step[1]
            return next_step[0],next_step[1]