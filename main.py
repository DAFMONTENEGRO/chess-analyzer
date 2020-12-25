import math


class Chess:

    template = ""
    chessboard = []
    default_pieces = "Tn.Cn.An.Dn.Rn.An.Cn.Tn." \
                     "Pn.Pn.Pn.Pn.Pn.Pn.Pn.Pn." \
                     "  .  .  .  .  .  .  .  ." \
                     "  .  .  .  .  .  .  .  ." \
                     "  .  .  .  .  .  .  .  ." \
                     "  .  .  .  .  .  .  .  ." \
                     "Pb.Pb.Pb.Pb.Pb.Pb.Pb.Pb." \
                     "Tb.Cb.Ab.Db.Rb.Ab.Cb.Tb"

    def __init__(self, pieces="", size=8):
        if not pieces and size == 8:
            pieces = self.default_pieces
        pieces = pieces.split(".")
        if len(pieces) != size**2:
            raise Exception("Notación incorrecta, por favor revise la notación para las piezas.")
        else:
            for piece in pieces:
                if not piece.isspace():
                    self.chessboard.append(piece)
                else:
                    self.chessboard.append("")
            self.__create_template(size)

    def __str__(self):
        return self.template

    def __create_template(self, size):
        letters = [chr(letter_i) for letter_i in range(97, 97+size)]
        letters = "  ".join(letters)
        self.template = "\n   {}\n".format(letters)
        for row in range(8, 0, -1):
            self.template += str(row) + " |"
            for column in range(1, 9):
                piece = str(self.chessboard[self.chessboard_index(row, column)])
                if piece:
                    self.template += piece + "|"
                else:
                    self.template += "  |"
            self.template += " {}\n".format(row)
        self.template += "   {}\n".format(letters)

    def chessboard_index(self, row, column):
        size = int(math.sqrt(len(self.chessboard)))
        index = size**2 - row*size + column-1
        if index < 0 or index >= len(self.chessboard):
            raise Exception("No existe la posición especificada en el tablero.")
        return index

    def notation_piece(self, notation):
        row = int(notation[1])
        column = ord(notation[0]) - 96
        return str(self.chessboard[self.chessboard_index(row, column)])

    def motion_summary(self, notation, step_column, step_row):
        row = int(notation[1]) + step_row
        column = ord(notation[0]) - 96 + step_column
        original_piece = self.notation_piece(notation)
        if 0 < row < 9 and 0 < column < 9:
            movement_notation = chr(column+96) + str(row)
            movement_piece = self.notation_piece(movement_notation)
            if movement_piece:
                if movement_piece[1] != original_piece[1]:
                    if not original_piece[0].startswith("P"):
                        return original_piece[0] + "x" + movement_notation
                    else:
                        return notation[0] + "x" + movement_notation
            else:
                if not original_piece[0].startswith("P"):
                    return original_piece[0] + movement_notation
                else:
                    return movement_notation
        return ""

    def __lineal_movements(self, notation, direction, step_column=0, step_row=0):
        step_row += direction[1]
        step_column += direction[0]
        movement = self.motion_summary(notation, step_column, step_row)
        if movement:
            movement += "."
            if "x" not in movement:
                movement += self.__lineal_movements(notation, direction, step_column, step_row)
            return movement
        return ""

    def tower_movements(self, notation, directions=((-1, 0), (0, -1), (1, 0), (0, 1))):
        if len(directions) > 0:
            return self.__lineal_movements(notation, directions[-1]) + self.tower_movements(notation, directions[:-1])
        else:
            return ""

    def bishop_movements(self, notation, directions=((1, 1), (1, -1), (-1, -1), (-1, 1))):
        if len(directions) > 0:
            return self.__lineal_movements(notation, directions[-1]) + self.bishop_movements(notation, directions[:-1])
        else:
            return ""

    def queen_movements(self, notation):
        return self.tower_movements(notation) + self.bishop_movements(notation)

    def position_movements(self, notation):
        piece = self.notation_piece(notation)
        if piece.startswith("T"):
            print(piece, notation + ":", self.tower_movements(notation))
        if piece.startswith("C"):
            # Codigo para caballo
            print("Aun no se ha implementado")
        if piece.startswith("A"):
            print(piece, notation + ":", self.bishop_movements(notation))
        if piece.startswith("D"):
            print(piece, notation + ":", self.queen_movements(notation))
        if piece.startswith("R"):
            # Codigo para rey
            print("Aun no se ha implementado")
        if piece.startswith("P"):
            # Codigo para peon
            print("Aun no se ha implementado")


pcs = "Tn.Cn.An.  .Rn.An.Cn.Tn." \
      "Pn.Pn.Pn.Pn.Pn.Pn.Pn.Pn." \
      "  .  .  .  .  .  .  .  ." \
      "  .Dn.  .  .Ab.  .  .  ." \
      "  .  .  .Tn.  .  .  .  ." \
      "  .  .  .  .  .  .  .  ." \
      "Pb.Pb.Pb.Pb.Pb.Pb.Pb.Pb." \
      "Tb.Cb.Ab.Db.Rb.  .Cb.Tb"
chess = Chess(pcs)
print(chess)
chess.position_movements("d4")
chess.position_movements("e5")
chess.position_movements("b5")
