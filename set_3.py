social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def relationship_status(from_member, to_member, social_graph):
    if (from_member in social_graph[to_member]["following"]) and (to_member in social_graph[from_member]["following"]) == True:
        return "friends"
    elif (to_member in social_graph[from_member]["following"]) == True:
        return "follower"
    elif (from_member in social_graph[to_member]["following"]) == True:
        return "followed by"
    return "no relationship"

def tic_tac_toe(board):
    rows = len(board)

    for i in range(rows):
        row = board[i]
        if row[0] and all(symbol == row[0] for symbol in row):
            return row[0]
    
    for j in range(rows):
        column = board[0][j]
        if column and all(board[i][j] == column for i in range(rows)):
            return column
        
    diagonal_right = board[0][0]
    if diagonal_right and all(board[i][i] == diagonal_right for i in range(rows)):
        return diagonal_right
    
    diagonal_left = board[0][rows - 1]
    if diagonal_left and all(board[i][rows - 1 - i] == diagonal_left for i in range(rows)):
        return diagonal_left
    
    return "NO WINNER"



def main():
    print(tic_tac_toe(board1))

if __name__ == "__main__":
    main()