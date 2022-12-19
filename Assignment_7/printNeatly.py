def neat(text, maximum):

    list_of_words = text.split()
    length_of_line = 0

    for i in list_of_words:

        if length_of_line + len(i) <= maximum:
            print(i, end=' ')
            length_of_line += len(i) + 1

        else:
            print()
            print(i, end=' ')
            length_of_line = len(i) + 1

    print()
