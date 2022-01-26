# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def first_move():
    print(
        "Make your first move by using one of the keywords:\n"
        "'up','right','down' or 'left'\n"
    )
    playing_str = input("Enter your first move here:\n")


def main():
    """
    Run all program functions
    """
    move_one = first_move()


print(
    "Welcome to 'The MAZE'\n"
    "\n"
    "", "--", "", "--", "END", "--\n"
    "|", " |", "  |", "  ", " ", "|\n"
    "", "--", "", "--", "--\n"
    "|", " |", "  ", "", " |", " ", "|\n"
    "", "--", "", " ", "  ", "\n"
    "|", " |", "  |", "  ", " ", "|\n"
    "", "--", "", "X", "", "--", "--", "\n"
    "\n"
    "Take X to END by using the keywords.\n"
)
main()
