this is a hotel managment system created in python.this system will manage various aspects of hotel like staff 
rooms , admin, guests ,room booking with each entery by unique id .
this system breack into 5 section(class) person , admin , rooms ,guests, staff.each part have a difrent function .
in person we have counstuctor that crate name unique_id and contact_info,
we can update contact and show all detail in __str__ method.
in admin we can do such things like creat_staff , remove_staff, updating staff roll, approve_maintennance_request,
and generate peyRoll report.
in staff we have 3 part Reseptionist,Housekeeping,Mainteance:
in reseptionist we can booking room , cheack in and checkout room ,display available room
in Housekeeping part we can mark_room_clean and request for supplies we need.
in Mainteance part we can report repair and order repaor materials.
Guests :
we can request for room booking for any type room in the hotel (1,2,suit,vip)rooms
amend booking with dates,
cancel booking room
and give a feedback for hotel
Rooms:
we can set room status like available and occupies .
we can see schedule room for each type of room.
and __str__ method for all details.
Hotel:
we have list of available rooms
get_guests_rooms,
summarize daily for operation.
any input enter we can see in logging file and any storage we have store in json file.
i hope you guys enjoy it.
at least we have menu we can run every functions we have
