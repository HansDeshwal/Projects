def sum(a,b,c):
     return a + b + c

def printbord(Xstate, Zstate):
    Zero = 'X' if Xstate[0] else ('O' if Zstate[0] else 0)
    one = 'X' if Xstate[1] else ('O' if Zstate[1] else 1)
    two = 'X' if Xstate[2] else ('O' if Zstate[2] else 2)
    three = 'X' if Xstate[3] else ('O' if Zstate[3] else 3)
    four = 'X' if Xstate[4] else ('O' if Zstate[4] else 4)
    five = 'X' if Xstate[5] else ('O' if Zstate[5] else 5)
    six = 'X' if Xstate[6] else ('O' if Zstate[6] else 6)
    seven = 'X' if Xstate[7] else ('O' if Zstate[7] else 7)
    eight = 'X' if Xstate[8] else ('O' if Zstate[8] else 8)
    print(f" {Zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def wincheck(Xstate, Zstate):
    wins =[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if (sum(Xstate[win[0]], Xstate[win[1]], Xstate[win[2]]) == 3):
            print("X won the match")
            return 1
        if (sum(Zstate[win[0]], Zstate[win[1]], Zstate[win[2]]) == 3):
            print("O won the match")
            return 0
    return -1


if __name__ == "__main__":
    Zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #turn 1 for X and 0 for O
    print("Wencome to tick tack toe")
    while(True):
        printbord(Xstate, Zstate)
        if (turn == 1):
            print("turn for player X")
            value = int(input("Please enter a value: "))
            Xstate[value] = 1
        else:
            print("turn for player O")
            value = int(input("Please enter a value: "))
            Zstate[value] = 1

        check = wincheck(Xstate, Zstate)

        if check == 1 or check == 0:
                break
        else:
                turn = 1 - turn