from board import Board, Result, Status, Player
import itertools

class TicTacToe(Board):

    def __init__(self, nodes=[[' ' for c in range(3)] for r in range(3)]):
        super().__init__()
        self.nodes = list(nodes)
        self.winning_states = [
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)]]

       


    def reset(self):
        super().reset()
        self.nodes = [[' ' for c in range(3)] for r in range(3)]

    def hash_value(self):
        return hash(",".join(self.one_dimensional_representation()))

    def one_dimensional_representation(self):
        return list(map(lambda node: self.translate_node(node) ,itertools.chain.from_iterable(self.nodes)))

    def available_moves(self):
        moves = []
        for r in range(len(self.nodes)):
            row = self.nodes[r]
            for c in range(len(row)):
                column = row[c]
                if type(column) is not tuple:
                    moves.append((r,c))

        return moves



    def is_move_valid(self, move):
        [row, column] = move
        if type(self.nodes[row][column]) is not tuple:
            return True 
        return False



    def save_move(self, player, move):
        [row, column] = move
        self.nodes[row][column] = (player,move)
        return True



    def moves_by_player(self,player):
        moves = []
        for r in range(len(self.nodes)):
            row = self.nodes[r]
            for c in range(len(row)):
                column = row[c]
                if type(column) is tuple and column[0] == player:
                    moves.append((r,c))
        return moves



    def evaluate_result(self,player):
        result = Result.Invalid
        moves = self.moves_by_player(player)

        for w_state in self.winning_states:
            matches = set(w_state).intersection(set(moves)) #[i for i,j in zip(w_state,moves) if i == j]
            if len(matches) >= 3:
                result = Result.Won
                break
        
        if result == Result.Invalid and len(self.available_moves()) == 0:
            result = Result.Draw

        return result



    def visualize_state(self):
        for row in range(len(self.nodes)):
            row_data = self.nodes[row]
            print('|{}|{}|{}|'.format(self.translate_node(row_data[0]), self.translate_node(row_data[1]), self.translate_node(row_data[2])))



    def translate_node(self,node):
        if type(node) is tuple:
            return node[0].avatar
        else:
            return node