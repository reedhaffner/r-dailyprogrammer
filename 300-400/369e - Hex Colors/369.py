
def hexcolor(r, g, b):
    red = str(hex(r).split("x")[-1]).zfill(2)
    green = str(hex(g).split("x")[-1]).zfill(2)
    blue = str(hex(b).split("x")[-1]).zfill(2)
    return ("#"+red+green+blue).upper()

def blend(*args):
    red = round(float(sum([int(x, 16) for x in [x[1:3] for x in args[0]]])) / max(len([int(x, 16) for x in [x[1:3] for x in args[0]]]), 1))
    green = round(float(sum([int(x, 16) for x in [x[3:5] for x in args[0]]])) / max(len([int(x, 16) for x in [x[3:5] for x in args[0]]]), 1))
    blue = round(float(sum([int(x, 16) for x in [x[5:7] for x in args[0]]])) / max(len([int(x, 16) for x in [x[5:7] for x in args[0]]]), 1))
    return hexcolor(red, green, blue)

"""
hexcolor = lambda r, g, b: ("#"+str(hex(r).split("x")[-1]).zfill(2)+str(hex(g).split("x")[-1]).zfill(2)+str(hex(b).split("x")[-1]).zfill(2)).upper()
blend = lambda *args: hexcolor(round(float(sum([int(x, 16) for x in [x[1:3] for x in args[0]]])) / max(len([int(x, 16) for x in [x[1:3] for x in args[0]]]), 1)), round(float(sum([int(x, 16) for x in [x[3:5] for x in args[0]]])) / max(len([int(x, 16) for x in [x[3:5] for x in args[0]]]), 1)),round(float(sum([int(x, 16) for x in [x[5:7] for x in args[0]]])) / max(len([int(x, 16) for x in [x[5:7] for x in args[0]]]), 1)))
"""

hexcolor(255, 99, 71)  # => "#FF6347"  (Tomato)
hexcolor(184, 134, 11)  # => "#B8860B"  (DarkGoldenrod)
hexcolor(189, 183, 107)  # => "#BDB76B"  (DarkKhaki)
hexcolor(0, 0, 205)  # => "#0000CD"  (MediumBlue)

blend({"#000000", "#778899"}) # => "#3C444C"
blend({"#E6E6FA", "#FF69B4", "#B0C4DE"})  # => "#DCB1D9"
