import CinemaDatabase

def main_menu():
    print("Welcome to our cinema.\nFor more info just write info")

    while True:
        command = input("$$$>")

        if command == "info":
            print("To see what movies we have pls write movies")

        if command == "movies":
            return ("SELECT * FROM  Movie")
        if command == "reservation":
            return ("SELECT name,projection,row,col FROM reservation VALUES(?,?,?,?)")
            conn.execute(name,projection,row,col)







def main():
    main_menu()
if __name__ == '__main__':
    main()
