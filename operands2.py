#A list is define as a variable that that holds data in a particular order 
#A list is mutable: that means it can be changed
#countries = ["Australia", "Malawi", "Nigeria", "Usa", "Iran"]
#print(type(countries))

favorite_movies = ["Head Of State", "Fifty Shades of Grye", "Love me" "More of Me", "Talk to me"]
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Biography =  ["Benjamin", 25, False, "male", 1.54, "red"]
ProvisionList = ["Rice", "Beans", "Milo", "Biscuit", "Groundnut"]

print (favorite_movies)
print()
print (Numbers)
print()
print (Biography)
print() 
print (ProvisionList)

andriod = ["Samsung", "Redmi", "Oppo", "Itel", "Techno"]
ios = ["11-pro-max", "15-pro", "Xr", "16-plus", "Iphone-7"]
phones = [andriod, ios]
print(phones)
print(phones[0][1])


code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-    ", "n", " ", "W", "@", "r", "d", "o", "#"]
print (code[1],code[2],code[4],code[5], code[8])
print (code[-6],code[-2],code[-4],code[5],code[4],code[-3])
print (code[::-1])

grid = [
    ["The", "sky", "is"],
    ["full", "of", "stars"],
    ["shining", "bright", "tonight"]
]

print (grid[0][0], grid[0][1])
print (grid[0][0], grid[1][2], "are", grid[2][0])
print (grid[1][::-1])

Best_fruits = ["Mango", "Apple", "Orange"]
print("Bfore update>>>>>>>>>>>")
print(Best_fruits)
Best_fruits[0] = "coconut"
print ("After update>>>>")
print(Best_fruits) 
Best_fruits[-1] = "grapes"
print("newly made list>>>>>")
print (Best_fruits)
Best_fruits.append("Mango")
print (Best_fruits)
Best_fruits.insert(1, "Mango")
print (Best_fruits)

playlist = ["Song A", "Song B", "Song C"]
print("playlist before change")
print(playlist)

playlist[1] ="Song D"
print("playlist after update")
print (playlist)

playlist.append("Song E")
print("playlist after new song is added")
print (playlist)

playlist.insert(0,"intro")
print("playlist after intro was added to playlist")
print (playlist)

desk = []
user_input1 = input("Enter name of first student: ")
user_input2 = input("Enter name of second student: ")
user_input3 = input("Enter name of third student: ")
desk.append(user_input1)
desk.append(user_input2)
desk.append(user_input3)
print (desk)

replace_name = input("Enter name to be replaced: ")
desk[1] = replace_name
print (desk)

desk.insert(1,"grace")
print("updated list of names")
print (desk)
