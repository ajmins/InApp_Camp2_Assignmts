import pyodbc
import functools

conString = 'Driver={SQL Server};Server=DESKTOP-CJEOG7N\SQLEXPRESS;Database=Camp2;Trusted_Connection=yes;'

MAXberth = 5
MAXwait = 2
class Utils:
    def getNum(*msg):
        while(1):
            try:
                num = int(input(*msg))
                return num
            except:
                print("Enter valid number")
                continue


#decorator for connecting db and python
def connectdb(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        try:
            myConn = pyodbc.connect(conString)
            myCursor = myConn.cursor()
            result = myFunc(myCursor, *args)
            myConn.commit()
            myConn.close()
            return result
        except Exception as e:
            print("Not connected because of :\n")
            print(e)
            print(f"{type(e).__name__}")
    return innerWrapper

#to list all the stations
@connectdb
def listStops(myCursor):
    myCursor.execute('SELECT * FROM stations')
    stations = myCursor.fetchall()
    return stations

#to book a ticket
@connectdb
def ticketBook(myCursor, stationID, name ):
    myCursor.execute('SELECT * FROM trains WHERE stop_id >= ?', (stationID))
    trains = myCursor.fetchall()
    bookStatus = False
    for trainID,trainName,_,_,_,berthFill,_ in trains:
        if berthFill < MAXberth:
            myCursor.execute('INSERT INTO passengers(passenger_name,station_id,train_id) VALUES (?,?,?);',(name,stationID,trainID)) 
            myCursor.execute('UPDATE trains SET berth_fill = ? WHERE train_id = ?',(berthFill+1, trainID))
            bookStatus = True
            print(f'{trainName} available and Booking is successfull')
            return bookStatus
    return bookStatus

@connectdb 
def addtoWaitingList(myCursor, stationID, name):
    myCursor.execute('SELECT * FROM trains WHERE end_id >= ?',(stationID))
    trains = myCursor.fetchall()
    addtoWLStatus = False
    for trainId,trainName,_,_,waitingListFill in trains:
        if waitingListFill < MAXwait:
            myCursor.execute('INSERT INTO waitlist(passenger_name,stop_id,train_id) VALUES (?,?,?);',(name,stationID,trainId))
            myCursor.execute('UPDATE trains SET wait_list_filled = ? WHERE train_id = ?',(waitingListFill+1,trainId))
            addtoWLStatus = True
            print(f'{trainName} available and added to Waiting List')
            return addtoWLStatus
    return addtoWLStatus

@connectdb
def showPassengerDetails(myCursor):
    myCursor.execute('''SELECT passenger_id, passenger_name, station_name, train_name  FROM passengers 
    JOIN stations ON passengers.station_id = stations.station_id 
    JOIN trains ON passengers.train_id = trains.train_id ORDER BY passengers.train_id''')
    print('Passenger Details are: ')
    passengers = myCursor.fetchall()
    print('Passenger Id     name    stop    train_name')
    for passenger_id, name, stations, train_name in passengers:
        print(f'{passenger_id}  {name}  {stations}  {train_name}')

@connectdb
def showWLDetails(myCursor):
    myCursor.execute('''SELECT passenger_id, passenger_name, station_name, train_name  FROM waitlist 
    JOIN stations ON waitlist.station_id = stations.station_id 
    JOIN trains ON waitlist.train_id = trains.train_id ORDER BY waitlist.train_id''')
    print('waiting list Details are: ')
    passengers = myCursor.fetchall()
    print('Passenger Id     name    station_name    train_name')
    for passenger_id, name, stations, train_name in passengers:
        print(f'{passenger_id} \t {name}\t  {stations}  \t{train_name}')

def bookorAddtoWL():
    Station = listStops()
    print('\nPlease enter your destinations listed below')
    for stationcode, stationname in Station:
        if stationcode!=0:
            print(stationcode, stationname)
    destination = Utils.getNum("Please enter the number of the destination station for booking: ")
    name = input(('Please enter your name: '))
    if not ticketBook(destination,name):
        option = input('No trains available to book. Do you want to added to waiting list of available train(y/n)')
        match(option):
            case 'y': 
                if not addtoWaitingList(destination,name):
                    print("No trains to available to be added to waiting list!")
                    return
            case 'n': print("Thankyou!")

while(1):
    ch = Utils.getNum("""
    1. View all stations
    2. Ticket Booking
    3. View details of passengers
    4. Show waiting list
    5. Exit
    """)
    match(ch):
        case 1: 
            station = listStops()
            print(station)
        case 2:
            bookorAddtoWL()
        case 3:
            showPassengerDetails()
        case 4:
            showWLDetails()
        case 5:
            exit()
        case _:
            print('Invalid input')





























