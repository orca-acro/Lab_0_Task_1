'''https://github.com/orca-acro/Lab_0_Task_1
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, 'r') as file_open:
        file_content = file_open.readlines()
    file_content = [content.strip() for content in file_content]
    return file_content


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    for i in range(pivot+1, len(input_line)):
        if input_line[pivot] <= input_line[i]:
            return False
    for i in range(1, pivot):
        if input_line[pivot] <= input_line[i]:
            return False
    return True


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
    '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    element = 0
    for i in range(len(board)):
        element += board[i].find('?')
    if abs(element) == len(board):
        return True
    else:
        return False


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(len(board)):
        row = board[i]
        for j in range(1, len(row)-1):
            if row[j].isdigit() == True:
                for k in range(j+1, len(row)-1):
                    if row[j] == row[k]:
                        return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1, len(board)-1):
        row = board[i]
        if row[0].isdigit():
            hint = int(row[0])
            return left_to_right_check(row, hint)


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    pass


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    pass


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))