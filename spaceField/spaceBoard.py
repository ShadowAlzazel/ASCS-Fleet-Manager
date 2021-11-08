#board

def makeGameBoard(opsSpace):
    n = 1
    lane = []
    row = ''
    indent = False
    if opsSpace.w % 2 == 0:
        indent = True

    def hexSquare(opsHex):
        if opsHex.empty == True:
            return '[ ]'
        else:
            s = opsHex.entity.command
            return ''.join(['[', str(s[0]), ']'])

    while n != len(opsSpace.starSpaceHexes) + 1:
        lane.append(hexSquare(opsSpace.starSpaceHexes[-n]))
        row = ''.join([hexSquare(opsSpace.starSpaceHexes[-n]), row])
        if len(lane) == opsSpace.l:
            if indent:
                print(' ', row)
            elif not indent:
                print(row)
            indent = not indent
            lane = []
            row = ''
        n += 1 
