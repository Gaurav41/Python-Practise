stud = {
    "name": "Gaurav",
    "age": "20",
    "emg": "😂😂🤣🤣😒😍😍😍"
}

print(stud["emg"])

#print(stud["dob"])#error

print(stud.get('name'))

print(stud.get('dob')) #no error , None
print(stud.get('dob',"Jan,20")) #default value

stud["mob"]= "9767916589"
print(stud)