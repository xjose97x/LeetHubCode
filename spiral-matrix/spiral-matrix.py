LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def get_next_direction(direction: int) -> int:
    return {
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP,
        UP: RIGHT
    }[direction]

def get_next_position(position: Tuple[int, int], direction: int) -> Tuple[int, int]:
    if direction == RIGHT:
        return (position[0], position[1] + 1)
    if direction == DOWN:
        return (position[0] + 1, position[1])
    if direction == LEFT:
        return (position[0], position[1] - 1)
    if direction == UP:
        return (position[0] - 1, position[1])

def is_valid_position(position: Tuple[int, int], matrix: List[List[int]]) -> bool:
    return (0 <= position[0] < len(matrix) and
            0 <= position[1] < len(matrix[0]) and
            matrix[position[0]][position[1]] is not None)
    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        direction = RIGHT
        position = (0, 0)
        
        remaining = len(matrix) * len(matrix[0])
        while remaining > 0:
            remaining -= 1
            result.append(matrix[position[0]][position[1]])
            matrix[position[0]][position[1]] = None
            next_position = get_next_position(position, direction)
            if not is_valid_position(next_position, matrix):
                direction = get_next_direction(direction)
                next_position = get_next_position(position, direction)
            position = next_position
        
        return result