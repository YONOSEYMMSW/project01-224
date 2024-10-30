def pretty_print(matrix):
    """
    pretty_print prints out 2D lists in an easier to read format than built-in print.
    :param matrix: A 2D list 
    :return: None
    :time complexity: Runs in O(n^2) time, where n is the number of rows or columns in matrix 
                        because each element in each row of the matrix is printed once
    """
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()

def transpose_major(matrix, in_place=False):
    """
    transpose_major transposes a 2D lists across the major diagonal. Can transpose either in-place or not
        depending on user-preference or project requirements
    :param matrix: A 2D list to be transposed
    :param in_place: determines whether matrix is transposed in-place or as a copy
    :return t_matrix: Either a reference to a 2D list (if transposed in-place) or a transposed copy of a 2D list
    :time complexity: O(n^2) because each element is moved once
    """
    size = len(matrix)
    
    if in_place:
        t_matrix = matrix
        for row in range(size - 1):
            for col in range(row + 1, size):
                temp = t_matrix[row][col]
                t_matrix[row][col] = t_matrix[col][row]
                t_matrix[col][row] = temp
    else:
        t_matrix = [[matrix[col][row] for col in range(size)] for row in range(size)]
    return t_matrix

def transpose_minor(matrix, in_place=False):
    """
    Transpose a 2D list across the minor diagonal. Can be done in-place or as a new copy.
    
    :param matrix: A 2D list to be transposed
    :param in_place: If True, transposes the matrix in-place; if False, returns a new transposed copy
    :return t_matrix: Either the original matrix (if in-place) or a new transposed copy
    :time complexity: O(n^2) because each element is moved once
    """
    size = len(matrix)
   
    if in_place:
        t_matrix = matrix
        for row in range(size - 1):
            for col in range(size - row - 1):
                temp = t_matrix[row][col]
                t_matrix[row][col] = t_matrix[size - col - 1][size - row - 1]
                t_matrix[size - col - 1][size - row - 1] = temp
    else:
        t_matrix = [[matrix[size - col - 1][size - row - 1] for col in range(size)] for row in range(size)]
    return t_matrix

def reverse_matrix_rows(matrix, in_place=False):
    """
    Reverse the order of rows in a 2D list. Can be done in-place or as a new copy.
    
    :param matrix: A 2D list with rows to be reversed
    :param in_place: If True, reverses rows in-place; if False, returns a new matrix with rows reversed
    :return rev_matrix: Either the original matrix (if in-place) or a new matrix with rows reversed
    :time complexity: O(n), where n is the number of rows
    """
    
    size = len(matrix)
    
    if in_place:
        # Modify the original matrix in place
        rev_matrix = matrix
        for i in range(size // 2):
            # Swap rows to reverse the order
            temp = rev_matrix[i]
            rev_matrix[i] = rev_matrix[size - i - 1]
            rev_matrix[size - i - 1] = temp
    else:
        # Create a new matrix with rows in reversed order
        rev_matrix = [matrix[i] for i in range(size - 1, -1, -1)]
    
    return rev_matrix  # Return rev_matrix consistently



def rotate(matrix, threshold=4):
    """
    Rotate a 2D list 90 degrees.
     If size >= threshold, rotates the matrix counterclockwise in-place
     If size < threshold, rotates the matrix clockwise and returns a new copy.
    
    :param matrix: A 2D list to be rotated
    :param threshold: Defines the size threshold for rotation behavior
    :return rotated_matrix: Either the original matrix (if in-place) or a new rotated copy
    :time complexity: O(n^2) because each element is moved once
    """
    size = len(matrix)

    if size >= threshold:
        rotated_matrix = matrix
        for i in range(size // 2):
            for j in range(i, size - i - 1):
                temp = rotated_matrix[i][j]
                rotated_matrix[i][j] = rotated_matrix[j][size - i - 1]
                rotated_matrix[j][size - i - 1] = rotated_matrix[size - i - 1][size - j - 1]
                rotated_matrix[size - i - 1][size - j - 1] = rotated_matrix[size - j - 1][i]
                rotated_matrix[size - j - 1][i] = temp
        return rotated_matrix
    else:
        rotated_matrix = [[matrix[j][size - i - 1] for j in range(size)] for i in range(size)]
        return rotated_matrix

def check_match(big_matrix, small_matrix, start_row, start_col):
    """
    Check if small_matrix matches a section of big_matrix starting from a given row and column.
    
    :param big_matrix: The larger 2D list to be searched
    :param small_matrix: The smaller 2D list to find in big_matrix
    :param start_row: The row in big_matrix where the check starts
    :param start_col: The column in big_matrix where the check starts
    :return: True if small_matrix matches this part of big_matrix, else False
    :time complexity: O(n^2), because n is the size of small_matrix
    """
    small_size = len(small_matrix)
    for i in range(small_size):
        for j in range(small_size):
            if big_matrix[start_row + i][start_col + j] != small_matrix[i][j]:
                return False
    return True

def count_appearances(big_matrix, small_matrix):
    """
    Count how many times small_matrix appears in big_matrix at each rotation (0, 90, 180, 270 degrees).
    
    :param big_matrix: The larger 2D list to search in
    :param small_matrix: The smaller 2D list to count in big_matrix
    :return: A list of counts for each rotation (0, 90, 180, 270 degrees)
    :time complexity: O(N^2 * n^2), because N is the size of big_matrix and n is the size of small_matrix
    """
    counts = [0, 0, 0, 0]
    
    for rotation in range(4):
        for i in range(len(big_matrix) - len(small_matrix) + 1):
            for j in range(len(big_matrix[0]) - len(small_matrix[0]) + 1):
                if check_match(big_matrix, small_matrix, i, j):
                    counts[rotation] += 1
        small_matrix = rotate(small_matrix, threshold=4)
    
    return counts

def main(file_path):
    with open(file_path, 'r') as file:
        while True:
            sizes = file.readline().strip()
            big_size, small_size = map(int, sizes.split())
            if big_size == 0 and small_size == 0:
                break
            
            big_matrix = [list(file.readline().strip()) for _ in range(big_size)]
            small_matrix = [list(file.readline().strip()) for _ in range(small_size)]
            
            counts = count_appearances(big_matrix, small_matrix)
            print(" ".join(map(str, counts)))






# DRIVER CODE (DO NOT MODIFY)
file_path = 'input.txt'
main(file_path)


# EXAMPLE TEST CODE
def initialize_test_matrix():
    return [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]


def test_reverse_matrix_rows():
    original_matrix = initialize_test_matrix()
    test_matrix = initialize_test_matrix()
    
    rev_matrix = reverse_matrix_rows(test_matrix, in_place=False)
    assert rev_matrix == list(reversed(test_matrix)), "reverse_matrix_rows not working as intended when in_place == False"

    rev_matrix = reverse_matrix_rows(original_matrix, in_place=True)
    assert rev_matrix == original_matrix, "reverse_matrix_rows not working as intended when in_place == True"

    
def test_transpose(function, matrix, in_place):
    print(f"\n####### Testing {function.__name__}: in_place = {in_place} #######\n")

    if in_place == False:
        t_matrix = function(matrix, in_place)
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix != matrix, "not working if in_place == False"

    else:
        t_matrix = function(matrix, in_place)
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix == matrix, "not working if in_place == True"

test_reverse_matrix_rows()

test_matrix = initialize_test_matrix()
test_transpose(transpose_major, test_matrix, in_place=False)

test_matrix = initialize_test_matrix()
test_transpose(transpose_minor, test_matrix, in_place=False)

test_matrix = initialize_test_matrix()
test_transpose(transpose_major, test_matrix, in_place=True)

test_matrix = initialize_test_matrix()
test_transpose(transpose_minor, test_matrix, in_place=True)