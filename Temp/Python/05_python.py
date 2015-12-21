>>> players = [29, 58, 66, 71, 87]
>>> players[2]
66
>>> players[2] = 68
>>> players
[29, 58, 68, 71, 87]
>>> players + [90, 91, 98]
[29, 58, 68, 71, 87, 90, 91, 98]
>>> players
[29, 58, 68, 71, 87]
>>> players.append(120)
>>> players
[29, 58, 68, 71, 87, 120]
>>> players[:2]
[29, 58]
>>> players[:2] = [0, 0]
>>> players
[0, 0, 68, 71, 87, 120]
>>> players[:2] = []
>>> players
[68, 71, 87, 120]
>>> players[:] = []
>>> players
[]