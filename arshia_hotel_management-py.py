from abc import ABC, abstractmethod 
import logging
import json
with open('jason_test.json','r') as file:
    data = json.load(file)



logging.basicConfig(filename='scraper.log',level=logging.INFO,
                    format='%(asctime)s- %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

class Person(ABC):
    @abstractmethod
    def __init__(self, unique_id, name, contact_info,rooms ):
        self.unique_id = unique_id
        self.name = name
        self.contact_info = contact_info
        self.staff = []
        self.all = []
        self.guests = []
        self.rooms = {}
        self.clean_status = {}
        self.clean_supplies = []
        self.repair_status = {}

        # guest_information ={
        #     "name": "John Doe",
        #     "age": '30',
        #     "isMarried": 'false',
        #     "address": {
        #             "street": "123 Main St",
        #             "city": "New York",}
        # }

    def update_contact_details(self, contact_info=None):
        self.contact_info = contact_info or self.contact_info

    def __str__(self):
        logging.info(f'your id is{self.unique_id},your name is{self.name},your contact_info is {self.contact_info}')    


class Admin(Person):
    def __init__(self, unique_id, name, contact_info):
        super().__init__(unique_id, name, contact_info)

    def create_staff_account(self, staff_detail):#crating account adding new staff
        self.all[staff_detail] = staff_detail.Staff
        Staff_name = input("enter staff name:")
        self.staff.append(Staff_name)
        logging.info(f"{Staff_name} added to staff")


    def remove_staff_member(self, staff_id):
        if staff_id in self.staff:
                self.staff.pop(staff_id)
                logging.info('removed!')
        else:
            logging.info('staff not found!')    

    def updating_staff_roll(self, staff_id=None, new_roll=None):
        self.staff_id = staff_id or self.staff_id
        self.new_roll = new_roll or self.new_roll
        old_name = input('enter staff name to update:')
        if old_name in self.staff:
            staff_id = ('enter your id:')
            new_roll = input('new position roll for staff:')
        else:
            logging.info('staff roll updated!')

    def approve_maintenace_request(self, room_id, maintenace_type):
        pass    
#check this out later    
    def generate_payroll_report(self):
        staff_member = Staff(unique_id=None,name=None,contact_info=None)
        print('staff salary report:')
        for staff_member in self.staff:
            logging.info(f'name{staff_member.name}, unique_id{staff_member.unique_id},contact_info{staff_member.contact_info}')
            
rooms = {
    '101': {'status': 'available', 'guest': None,'dates':0/0/0},
    '102': {'status': 'available', 'guest': None,'dates':0/0/0},
    '103': {'status': 'available', 'guest': None,'dates':0/0/0},
}#its can be more than 3 room but for ex we have 3 room :)    

class Staff(Person):
    def __init__(self, unique_id, name, contact_info):
        super().__init__(unique_id, name, contact_info)

    def display_available_rooms(self):#add 
        logging.info("Available Rooms:")
    for room, info in rooms.items():
        if info['status'] == 'available':
            logging.info(f"Room {room}")

    def display_occupied_rooms(self):
        occupied_room = [room for room,info in self.rooms.items() if not info['available']]
        print(f'occupied rooms:{occupied_room}')        

    def book_guest(self, guest_id, room_id):
        self.guest_id = guest_id
        self.room_id = room_id
        room_id = logging.info('enter your room number(id):')
        if room_id in rooms.keys:
            if rooms[room_id]['status'] == 'available':
                guest_id = input('enter guest name:')
                rooms[room_id]['status'] = 'occupied'
                rooms[room_id]['guest'] = guest_id
                logging.info(f'Room {room_id} booked for {guest_id}.')
            else:
                logging.info(f'Room {room_id} is already occupied.')
        else:
            logging.info("<Invalid room number>!")            

#Receptionist
    def check_in(self, room_number,guest_id):
        if room_number in self.rooms:
            logging.info(f'Room {room_number} is already occupied.')
        else:
            self.rooms[room_number] = guest_id 
            logging.info(f"{guest_id} has been checked into Room{room_number}.")

    def check_out_guest(self,room_number):
        if room_number in self.rooms:
            guest_id = self.rooms.pop(room_number)
            logging.info(f"{guest_id}has been checked out from Room{room_number}.")
        else:
            logging.info(f'Room{room_number} is not occupied')     
#Housekeeping
    def mark_room_cleaned(self, room_number):
        if room_number in self.rooms:
            self.clean_status[room_number] = True
            logging.info(f"Room{room_number}has been marked as clean.")
        else:
            logging.info(f'Room{room_number}does not exist or not currently in use.')    

    def request_cleaning_supplies(self, room_number):
        if room_number in self.rooms:
            self.clean_supplies[room_number] = True
            logging.info(f"cleaning supplies requested for Room{room_number}.")
        else:
            logging.info(f"room {room_number} is not occupied.")    
        
#Maintenance
    def report_repair_done(self, room_number, issue_discription):
        if room_number in self.rooms:
            self.repair_status[room_number] = issue_discription
            logging.info(f'Repair report for Room{room_number} has been faild:{issue_discription}')
        else:
            logging.info(f"Room {room_number} is not occupied.")

    def order_repair_material(self, material_list, quantity, suplier_name):
        logging.info(f'order placed for{quantity}units of {material_list}from suplier{suplier_name}.')

available_rooms = {
            'single': [101,102,103],
            'double': [201,202,203,204],
            'suite' : [301, 302],
            'vip' : [401, 402]
        }#oder room types and and room number...
class Guests(Person):
    def __init__(self, unique_id, name, contact_info):
        super().__init__(unique_id, name, contact_info)
    def add_guest(self, guest_id,guest_name):
        self.guests.append({"guest_id":guest_id,"guest_name":guest_name})
        print(f"guest{guest_name}with id{guest_id}added!")


    def request_room_booking(self, guest_id, check_in_date, check_out_date,room_type):
        if room_type in available_rooms and available_rooms[room_type]:
            room_number1 = available_rooms[room_type][0]
            return f"guest {guest_id}successfully booked room{room_number1}of type{room_type} from {check_in_date} to {check_out_date}"
        else:
            logging.info('somthing wrong , be cerful to choose type room!')


    def amend_booking(self, booking_id, new_dates,new_name_guest):
        if booking_id in self.rooms:
            self.rooms[booking_id]['dates'] = new_dates
            self.rooms[booking_id]['guest'] = new_name_guest
            logging.info(f'booking for room{booking_id}has been updated to{new_name_guest} for time{new_dates}')
        else:
            logging.info(f'room {booking_id} is not available!')    


    def cancel_booking(self, booking_id):
        if booking_id in self.rooms:
            self.rooms[booking_id]['available'] = "occuppied"
            self.rooms[booking_id]['guest'] = ''
            logging.info(f'booking for room{booking_id} has been cancelled.')
        else:
            logging.info(f'room{booking_id} is not available!')

    def give_feedback(self, feedback_text):
        logging.info(f'feedback:{feedback_text}thank you send a feedback.')

class Rooms(Staff):
    def __init__(self, new_status, maintenace_type,):
        self.new_status = new_status or self.new_status  
        self.maintenace_type = maintenace_type or self.maintenace_type

    def set_room_status(self, room_id,new_status):
        if room_id in self.rooms:
            self.rooms[room_id] = new_status
            logging.info(f'the status of room {room_id} has been set to{new_status}')
        else:
            print(f'room{room_id}does not exist in the hotel!')

    def schedule_room_maintenance(self, maintenance_type):
        schedule_room_type ={
             "1" : 'cleaning',
             '2' : 'Checking consumables',
             '3' : 'checking calls and letter',
             '4' : 'food , drink , snack asn stuff',
        }
        if maintenance_type in schedule_room_type and schedule_room_type[maintenance_type]:
            logging.info(f'you should choose range 1 to 4 for schedule room type:{maintenance_type}')
        else:
            print('is not able to maintenance scheduling.')
            
    def __str__(self):
        logging.info(f'your status is{self.new_status},your maintenance_type is{self.maintenance_type}')    


class Hotel(Staff):
    def list_available_rooms(self, room_type):
        available_rooms1 = [room for room in self.rooms.values if 'status' == 'available']
        if available_rooms1 and available_rooms.keys == room_type:
            print(f'available room {available_rooms1} and the room type is{room_type}')
        else:
            logging.info('no available room of the specified type.')    

    def get_guest_details(self, guest_id):
        self.guest_id = guest_id
        for self.guest in guest_id:
            if self.guest["guest_id"] == guest_id:
                return self.guest
            return None
        
    def summarize_daily_operations(self):
        total_guest = len(self.guest_id)
        operation_report = input('pls discribe every check in and check out to this letter and suplies delivery(check logging server to see all cheanges):')
        print(f"number of guest in the hotel today{total_guest},and discription writen by operation{operation_report} ")
while True:
    menu = input('Person/Admin/Staff/Guests/Room/Hotel/EXIT:')
    if menu == "Person":
        cmd1 = input('init/update_contact_detail,__str__')
        if cmd1 == 'init':
            unique_id = input('enter your id:')
            name = input('enter your name:')
            contact_info = input('whats your contact info:')
            rooms = input('enter your rooms:')
            Person.__init__(unique_id,name,contact_info,rooms)
        elif cmd1 == '__str__':  
            unique_id = input('enter your id:')
            name = input('enter your name:')
            contact_info = input('whats your contact info:')
            rooms = input('enter your rooms:')
            Person.__str__(unique_id,name,contact_info,rooms)
        elif cmd1 == "update_contact_detail":
            contact_info = input('whats your contact info:')
            Person.update_contact_details()
    elif menu == 'Admin':
        cmd2 = input('create_staff_account/remove_staff_member/update_staff_roll/approve_maintenance_request/generate_payroll_report:')
        if cmd2 == "create_staff_account":
            staff_detail = input('enter staff detail:')
            Admin.create_staff_account()
        elif cmd2 == "remove_staff_member":
            Staff_id = input('enter staff id to remove:')
            Admin.remove_staff_member()
        elif cmd2 == "update_staff_roll":
            Staff_id = input('enter staff id to remove:')
            new_roll = input('enter new roll for staff:')
            Admin.updating_staff_roll()
        elif cmd2 == "approve_maintenance_request":
            room_id = input('enter room id:')
            maintenace_type = input('enter maintenace type:')
            Admin.approve_maintenace_request()
        elif cmd2 == "generate_payroll_report":
            Admin.generate_payroll_report()
        else: 
            break
    
    elif menu == 'Staff':
        cmd3 = input('display_available_rooms,display_occupied_rooms,book_guest,check_out,check_in,marked_room_clean,request_suplies,report_repair,order_repair:')
        if cmd3 == 'book_guest':
            guest_id = input('enter your id:')
            room_id = input('enter your room id:')
            Staff.book_guest()
        elif cmd3 == 'check_out':
            room_number = input('enter room number: ')
            Staff.check_out_guest()
        elif cmd3 == 'check_in':
            room_number = input('enter room number:')
            guest_id = input('enter guest id:')
            Staff.check_in()
        elif cmd3 == 'marked_room_clean':
            room_number = input('enter room number:')
            Staff.mark_room_cleaned()
        elif cmd3 == 'request_suplies':
            room_number = input('enter room number:')
            Staff.request_cleaning_supplies()
        elif cmd3 == 'report_repair':
            room_number = input('enter room number:')
            issue_discription = input('what your issue pls discribe:')
            Staff.request_cleaning_supplies()
        elif cmd3 == 'order_repair':
            material_list = input('pls enter your material list you need:')
            quantity = input("quantity:")
            suplier_name = input('suplier name is:')
            Staff.order_repair_material()
        elif cmd3 == "display_available_rooms":
            Staff.display_available_rooms() 
        elif cmd3 == 'display_occupied_rooms':
            Staff.display_occupied_rooms()    
        else:
            break
    elif menu == 'Guests':
        cmd4 = input('request_room_booking,amend_booking,cancel_booking,give_feed_back:')
        if cmd4 == 'request_room_booking':
            guest_id = input('guest id:')
            check_in_date = input('cheack in date:')
            check_out_date = input('cheack out date:')
            room_type = input("choose type.single,double,suite,vip:")
            Guests.request_room_booking()
        elif cmd4 == 'amend_booking':
            booking_id = input("booking id:")
            new_dates = input("enter new dates:")
            new_name_guest = input('enter new name:')
            Guests.amend_booking()
        elif cmd4 == 'cancel_booking':
            booking_id = input("booking id:")
            Guests.cancel_booking() 
        elif cmd4 == 'give_feed_back':
            feedback_text = input('your feedback for our hotel:')
        else:
            break
            
    elif menu == 'Room':
        cmd5 = input('set_status_room,schedule,str_room:')
        new_status = input("enter new status:")
        maintenance_type = input('choose schedule 1=> cleaning ,2=>Checking consumables,3=>checking calls and letter,4=>food , drink , snack asn stuff')
        if cmd5 == 'set_status_room':
            room_id = input('enter room id:')
            new_status = input("enter new status:")
            Rooms.set_room_status()
        elif cmd5 == "schedule":
            maintenance_type = input('choose schedule 1=> cleaning ,2=>Checking consumables,3=>checking calls and letter,4=>food , drink , snack asn stuff')
            Rooms.schedule_room_maintenance()
        elif cmd5 == "str_room":
            Rooms.__str__()
        else:
            print('error')
    elif menu == 'Hotel':
        cmd6 = input("list_avilable_rooms,get_guest_details,summarize_daily_operation:")
        if cmd6 == 'list_avilable_rooms':
            room_type = input("choose type.single,double,suite,vip:")
            Hotel.list_available_rooms()
        elif cmd6 == "get_guest_details":
            guest_id = input('enter guest id:')
            Hotel.get_guest_details()
        elif cmd6 == "summarize_daily_operation":
            Hotel.summarize_daily_operations()
        else:
            print('error')
    else:
        menu == "EXIT"
        break

with open('data.json','w') as file:
    json.dump(available_rooms, file, indent=1 , sort_keys=True)
    print('done')
with open('data.json','w') as file:
    json.dump(rooms, file, indent=2 , sort_keys=True)
    print('done')        

if __name__ == "__main__":
    main()
