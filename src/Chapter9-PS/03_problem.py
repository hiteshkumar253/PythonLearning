# n = int(input("Enter a number to generate its multiplication table: "))

def generateTable(n):
        table = ""
        for i in range(1, 11):
                table += f"{n} x {i} = {n*i}\n"

        with open(f"tables/table_of_{n}.txt", "w") as file:
                file.write(table)


for i in range(2, 21):
    generateTable(i)