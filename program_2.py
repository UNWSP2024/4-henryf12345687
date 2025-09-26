# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    totalTickets = 0
    while True:
        movie = input("Enter any movie  or say 'stop' to stop: ")
        if movie == "stop":
                break
        tickets = int(input("Enter the amount of tickets wanted for the movie: "))
        totalTickets += tickets
    print("Total tickets wanted:", totalTickets)


if __name__ == '__main__':
    main()