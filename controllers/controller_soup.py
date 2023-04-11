def __search_word_in_matrix(matrix: list, word: str) -> list | None:
    """
    Get the range of matrix and range of each array inside the matrix
    Iterate over the matrix and check if the first letter of the word not is equal to the first letter of the matrix
    If it is equal, then it will check the next letter in the matrix
    If it is not equal, then it will continue with the next letter in the matrix

    build all possible directions to search the word
    iterate over the directions
    reassign the variables to not lose them and not overwrite them
    create a list with the letters found
    iterate over the word
    create new variables with the new position to search
    if the new position is out of the matrix, then break
    if the new position is equal to the next letter of the word, then append the new position to the list

    if the length of the list is equal to the length of the word, then return the list

    Args:
        matrix (list): The matrix to search the words in
        word (str): The word to search in the matrix

    Returns:
        list | None: A list with the letters found or None if the word is not found
    """
    for i in range(len(matrix)):  # get the length of the array
        for j in range(len(matrix[i])):  # get the length of each internal array
            if matrix[i][j] != word[0]:
                # if the first letter is not equal to the first letter to search, continue
                continue

            directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
            for direction in directions:
                # reassign the variables so that
                # they are not overwritten
                x, y = (i, j)
                letters = [[x, y]]

                for k in range(1, len(word)):
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if new_x < 0 or new_x >= len(matrix) or new_y < 0 or new_y >= len(matrix[0]):
                        break
                    if matrix[new_x][new_y] == word[k]:
                        letters.append([new_x, new_y])
                        x, y = new_x, new_y
                    else:
                        break

                if len(letters) == len(word):
                    return letters

    return None


def search_words_in_matrix(
    entrypoint: list,
    words: list,
) -> dict:
    """
    Iterates over the words list and searches for each word in the matrix

    Args:
        entrypoint (list): The matrix to search the words in
        words (list): The list of words to search in the matrix

    Returns:
        dict: A dictionary with the words found as keys and the letters as values
    """
    words_found = {}
    for word in words:
        if letters := __search_word_in_matrix(entrypoint, word):
            words_found[word] = letters
    return words_found
