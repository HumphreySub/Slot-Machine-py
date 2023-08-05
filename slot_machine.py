import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3 
COLS = 3 

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 10,
    "B": 4,
    "C": 2,
    "D": 1
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    # The function first creates a list all_symbols by repeating each symbol according to its count in the symbols dictionary.
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for _ , column in enumerate(columns):
            if _ != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end ="")
        
        print()


# where users deposit money
def deposit():
    while True: 
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
        # amount will convert into a int  
            amount = int(amount)
        # amount that is greater than 0 will break the loop
            if amount > 0:
                break
            # if the amount is not greater than 0
            else:
                print("Amount must be greater than 0")
        # if amount is not a number
        else: 
            print("Please enter a number")
    
    return amount
# where users choose how many lines to bet 
def get_number_of_lines():
    while True: 
        lines = input("Enter the number of the lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
        # lines will convert into a int
            lines = int(lines)
            # if lines is not less than one and not greater than max_lines
            if 1 <= lines <= MAX_LINES:
                break
            # if lines is not a number or greater than 3 
            else:
                print("Enter a Valid number of lines. ")
    return lines

# where users put the amount of bet
def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            # amount will convert into a int
            amount = int(amount)
            # if amount is not less than min and not greater than max then break 
            if MIN_BET <= amount <= MAX_BET:
                break
            # if amount is less than min or greater than max bet 
            else: 
                print(f"Amount must between ${MIN_BET} - ${MAX_BET}.")
        # if amount is not a digit        
        else: 
            print("Please enter a number")
    
    return amount

# the process of bet
def spin(balance):
    # lines is equal to function get_number_ of_lines 
    lines = get_number_of_lines()
    while True: 
        # bet is equal to function get_bet
        bet = get_bet()
        # var total bet is equal to bet * lines
        total_bet = bet * lines

        # if total_bet is greater than balance 
        if total_bet > balance: 
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        # if total bet is less than or equal to balance then break     
        else: 
            break
    #string message on where the bet is on the lines and the equavalent of total bet
    print(f"You are betting ${bet} on {lines} line. Total bet is equal to ${total_bet}")

    # slot is equal to function get_slot_machine_spin
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

# the process of the slot_machine
def main():
    # balance is equal to function deposit()
    balance = deposit()
    while True:
        # to view the user current balance 
        print(f"Current balance is ${balance}")
        # asking if the user is ready to play
        answer = input("Press enter to play(q to Quit).")
        # if the user press q the while loop will break
        if answer == "q":
            break
        # iterate the variable balance 
        else:
            balance += spin(balance)
    # message after the user press q 
    print(f"you left with ${balance}")


main()