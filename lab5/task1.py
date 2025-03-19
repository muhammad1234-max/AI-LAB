import chess
import chess.engine
import heapq

class ChessBeamSearch:
    def __init__(self, beam_width=3, depth_limit=3):
        self.beam_width = beam_width
        self.depth_limit = depth_limit

    def evaluate_board(self, board):
        """
        Simple heuristic evaluation function.
        +1 for each pawn, +3 for knights/bishops, +5 for rooks, +9 for queens.
        """
        piece_values = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
                        chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}
        
        evaluation = 0
        for piece_type in piece_values:
            evaluation += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
            evaluation -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
        return evaluation

    def beam_search(self, board):
        """
        Perform Beam Search to find the best move sequence.
        """
        beam = [(self.evaluate_board(board), board, [])]  # (score, board, move_sequence)

        for _ in range(self.depth_limit):
            candidates = []
            
            for score, current_board, move_sequence in beam:
                legal_moves = list(current_board.legal_moves)
                
                for move in legal_moves:
                    new_board = current_board.copy()
                    new_board.push(move)
                    new_score = self.evaluate_board(new_board)
                    new_move_sequence = move_sequence + [move]
                    heapq.heappush(candidates, (-new_score, new_board, new_move_sequence))  # Max heap

            # Keep top 'beam_width' candidates
            beam = heapq.nsmallest(self.beam_width, candidates, key=lambda x: x[0])

        # Return the best move sequence found
        best_score, best_board, best_moves = max(beam, key=lambda x: x[0])
        return best_moves, -best_score  # Negate score since we stored it as negative for max heap

# Initialize board and Beam Search
board = chess.Board()  # Standard chess starting position
beam_searcher = ChessBeamSearch(beam_width=3, depth_limit=3)

# Find the best move sequence
best_moves, best_score = beam_searcher.beam_search(board)

# Print the result
print("Best Move Sequence:", [board.san(move) for move in best_moves])
print("Evaluation Score:", best_score)
