class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.__show_list = []
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.seats[id] = []
        for i in range(self.rows):
            r = []
            for j in range(self.cols):
                r.append(0)
            self.seats[id].append(r)

    def book_seats(self, id, list):
        for i,j in list:
            if 0<= i <self.rows and 0<=j<self.cols:
                if self.seats[id][i][j] == 0:
                    self.seats[id][i][j] = 1
                    print(f'seat {i,j} booked')
                else:
                    print(f'seat {i,j} is already booked')

            else:
                print(f'wrong seat')

    def view_show_list(self):
        print("__________________________________")
        for detail in self.__show_list:
            print(f'MOVIE NAME: {detail[1]} SHOW ID:{detail[0]} TIME:{detail[2]}')
        print("__________________________________")

    def view_available_seats(self, id):
        if id not in self.seats:
            print('invalid id')
            return
        for i in range(self.rows):
            for j in range(self.cols):
                print(f'{self.seats[id][i][j]}', end=' ')
            print()


hall = Hall(5,5,1)
hall.entry_show( 111, 'Jawan Maji', '25/10/2024 11:00 AM')
hall.entry_show( 333, 'Sujon Maji', '25/10/2024 2:00 PM')

run = True

while run:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. Exit')

    option = int(input("ENTER OPTION: "))
    
    if option == 1:
        hall.view_show_list()

    elif option == 2:
        id = int(input("Enter id: "))
        hall.view_available_seats(id)

    elif option == 3:
        id = int(input("Enter id: "))
        seat_list =[]
        seat_number = int(input("Number of seat to book: "))
        for _ in range(seat_number):
            i = int(input())
            j = int(input())
            seat_list.append((i,j))

        hall.book_seats(id, seat_list)

    elif option == 4:
        exit()