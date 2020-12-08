import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

give_word = input("Enter The Word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %give_word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])

else:
    print("No word found!")
