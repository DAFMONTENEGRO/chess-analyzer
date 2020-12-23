
class Chessboard:

    chess = {}
    default_pieces = ".Tn.Cn.An.Dn.Rn.An.Cn.Tn" \
                     ".Pn.Pn.Pn.Pn.Pn.Pn.Pn.Pn" \
                     ".  .  .  .  .  .  .  .  " \
                     ".  .  .  .  .  .  .  .  " \
                     ".  .  .  .  .  .  .  .  " \
                     ".  .  .  .  .  .  .  .  " \
                     ".Pb.Pb.Pb.Pb.Pb.Pb.Pb.Pb" \
                     ".Tb.Cb.Ab.Db.Rb.Ab.Cb.Tb"

    def __init__(self, pieces=""):
        if not pieces:
            pieces = self.default_pieces
        pieces = pieces.split(".")
        if len(pieces) != 65:
            raise Exception("Notación incorrecta, por favor revise la notación para las piezas.")
        else:
            for i in range(8, 0, -1):
                for i_ascii in range(97, 105):
                    key = chr(i_ascii) + str(i)
                    if pieces[1].isspace():
                        self.chess[key] = ""
                    else:
                        self.chess[key] = pieces[1]
                    pieces = pieces[1:]

    def __str__(self):
        view = "\n   a  b  c  d  e  f  g  h\n"
        for i in range(8, 0, -1):
            view += str(i) + " |"
            for i_ascii in range(97, 105):
                key = chr(i_ascii) + str(i)
                piece = self.chess[key]
                if piece:
                    view += piece + "|"
                else:
                    view += "  |"
            view += " {}\n".format(i)
        view += "   a  b  c  d  e  f  g  h\n"
        return view


chessboard = Chessboard()
print(chessboard)
