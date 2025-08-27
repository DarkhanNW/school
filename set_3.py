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

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

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

def eta(first_stop, second_stop, route_map):
    travel_time = 0
    trip_processing = True
    trip_started = False
    trip_start = None
    trip_end = None

    for route in route_map:
        if first_stop in route[0]:
            trip_start = route
        if second_stop in route[1]:
            trip_end = route
    
    while trip_processing:
        for route in route_map:
            if route == trip_start:
                if route == trip_end:
                    travel_time += route_map[route]["travel_time_mins"]
                    trip_processing = False
                    break
                travel_time += route_map[trip_start]["travel_time_mins"]
                trip_started = True
                continue
            if trip_started:
                if route == trip_end:
                    trip_processing = False
                    travel_time += route_map[route]["travel_time_mins"]
                    break
                travel_time += route_map[route]["travel_time_mins"]

    return travel_time

# for my own testing
def main():
    print(eta("admu", "dlsu", legs))
    print(eta("upd", "upd", legs))
    print(eta("admu", "upd", legs))
    print(eta("upd", "dlsu", legs))

if __name__ == "__main__":
    main()