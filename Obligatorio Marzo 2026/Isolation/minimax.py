from agent import Agent
from board import Board

class MiniMaxAgent(Agent):

    def __init__(self, player=1, depth=3):
        super().__init__(player)
        self.depth = depth
    
    def next_action(self, board: Board):
        return self.minimax_decision(board)
    
    # ---------------- HEURÍSTICA ----------------

    def heuristic_utility(self, board: Board):
        finished, winner = board.is_end(self.player)
        if finished:
            return 1000 if winner == self.player else -1000
        points = self.mobility(board) + self.spaceleft(board) + self.center_control(board)
        return points

    # ---------------- MINIMAX + ALPHA-BETA ----------------

    def minimax(self, board: Board, depth, alpha, beta, current_player):

        finished, _ = board.is_end(current_player)

        if depth == 0 or finished:
            return self.heuristic_utility(board)

        # Nodo MAX (mi turno)
        if current_player == self.player:

            value = float("-inf")

            for action in board.get_possible_actions(current_player):

                new_board = board.clone()
                new_board.play(action, current_player)

                value = max(
                    value,
                    self.minimax(
                        new_board,
                        depth - 1,
                        alpha,
                        beta,
                        3 - current_player
                    )
                )

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

            return value

        # Nodo MIN (turno rival)
        else:

            value = float("inf")

            for action in board.get_possible_actions(current_player):

                new_board = board.clone()
                new_board.play(action, current_player)

                value = min(
                    value,
                    self.minimax(
                        new_board,
                        depth - 1,
                        alpha,
                        beta,
                        3 - current_player
                    )
                )

                beta = min(beta, value)

                if alpha >= beta:
                    break

            return value

    # ---------------- DECISIÓN ----------------

    def minimax_decision(self, board: Board):

        best_value = float("-inf")
        best_action = None

        alpha = float("-inf")
        beta = float("inf")

        for action in board.get_possible_actions(self.player):

            new_board = board.clone()
            new_board.play(action, self.player)

            value = self.minimax(
                new_board,
                self.depth - 1,
                alpha,
                beta,
                3 - self.player
            )

            if value > best_value:
                best_value = value
                best_action = action

            alpha = max(alpha, best_value)

        return best_action

    #--------------Funciones--------------

    def mobility(self, board: Board):
        my_moves = len(board.get_possible_actions(self.player))
        opp_moves = len(board.get_possible_actions(3 - self.player))
        return my_moves - opp_moves
    
    def spaceleft(self, board: Board):
        my_space = self.accessible_space(board, self.player)
        opp_space = self.accessible_space(board, 3 - self.player)
        return my_space - opp_space

    def accessible_space(self, board: Board, player):
        start = board.find_player_position(player)
        if start is None:
            return 0
        visited = set()
        stack = [start]
        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)
        ] 
        while stack:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (
                    0 <= nr < board.board_size[0]
                    and 0 <= nc < board.board_size[1]
                ):
                    if (
                        board.grid[nr, nc] == 0
                        and (nr, nc) not in visited
                    ):
                        stack.append((nr, nc))
        return len(visited) - 1
    
    def center_control(self, board: Board):
        my_row, my_col = board.find_player_position(self.player)
        opp_row, opp_col = board.find_player_position(3 - self.player)
        center_row = (board.board_size[0] - 1) / 2
        center_col = (board.board_size[1] - 1) / 2
        my_distance = abs(my_row - center_row) + abs(my_col - center_col)
        opp_distance = abs(opp_row - center_row) + abs(opp_col - center_col)
        return  -1 * (my_distance - opp_distance)