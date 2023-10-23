
def compose(musical_notes, moves, start):
    song = []
    song.append(musical_notes[start])

    for i in range(0, len(moves)):
        start += moves[i]
        start %= len(musical_notes)
        song.append(musical_notes[start])

    return song

if __name__ == '__main__':
    n = int(input("Enter the number of musical notes in your list: "))
    musical_notes = [(input("Musical note {} is: ".format(i + 1))) for i in range(n)]

    m = int(input("Enter the number for the list of moves: "))
    moves = [int(input("Enter move {}: ".format(i + 1))) for i in range(m)]

    start_position = int(input("The start position is: "))

    song = compose(musical_notes, moves, start_position)

    print(f"Your song is: {song}")