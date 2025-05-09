text = "»"
print(text*89)
"""
Dictionary value :
🪶 create with {}
🪶 create with dict()
"""

student = {"name" : "praveen","age": 20,"marks": 90,"course" : "python"  }
print(type(student))
student.clear()


print("after clear:",student )

student = dict(name = "praveen",age = 20,marks = 90,course = "python")
print(type(student))
student.clear()
print("after clear:",student )

text = "<>"
print(text*45)


"""
Book name and author name 
"""
details = {
    "1️⃣ kalki" : { "name": "ponniyin selvan","published": "01/01/1954"},
    "2️⃣ Jayakanthan" : {"name":"Sila Nerangalil Sila Manithargal","published" : "01/01/1954" },
    "3️⃣ Vairamuthu" : {"name":" Kallikaattu Ithigaasam", "published" : "01/01/2001"},
    "4️⃣ Sundara Ramaswamy" :{"name" : "Oru Puliyamarathin Kathai", "published" : "01/01/1966"},
    "5️⃣ Janakiraman" : {"name" : "Amma Vanthaal", "published" : "01/01/1966" },
    "6️⃣ Madhan" : {"name":"Ki.Mu Ki.Pi", "published" : "01/01/2006"},
    "7️⃣ Sandilyan" :{"name": " Kadal Pura 1", "published" : "01/01/1967"},
    "8️⃣ Jeyamohan":{"name": "Aram", "published" : "01/01/2011"},
    "9️⃣ Sujatha":{"name":"Srirangathu Devadhaigal", "published" : "01/01/2004" },
    "🔟 Perumal Murugan":{"name": "Madhorubhagan", "published" : "01/01/2004"},
        }
print("🪶print book name:",details["1️⃣ kalki"]["name"] )
print("🪶print book name:",details["7️⃣ Sandilyan"]["published"] )
print("🪶print book name + year:",details["5️⃣ Janakiraman"]["name"] ,details["5️⃣ Janakiraman"]["published"])



text = "🔚"
print(text*41)