def read_file_info(file_name: str):
    number_of_chars = 0
    number_of_words = 0
    number_of_lines = 0

    with open(file_name, 'r') as file:
        for lines in file:
            words = lines.split()
            number_of_lines += 1
            number_of_words += len(words)
            number_of_chars += len(lines)

    print("Number of Lines: {}\nNumber of Words: {}\nNumber of Characters: {}".format(number_of_lines,
                                                                                      number_of_words,
                                                                                      number_of_chars))
