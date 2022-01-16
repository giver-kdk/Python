import random

sentence=[]

def main():
    while True:

        age= int(input(print("Enter your age: ")))
        letter1= str(input(print("Enter the first letter of your name: ")))
        letter2= str(input(print("Enter the first letter of your surname: ")))

        if(age>=1 and age<=14):
            with open('PythonSecond\Fortune Teller Code\Fortune1.txt') as file:
                for line in file: # for-each loop gives lines one at a time

                    sentence.append(line.strip())

        elif(age>=15 and age<=20):
            with open('PythonSecond\Fortune Teller Code\Fortune2.txt') as file:
                
                for line in file: # for-each loop gives lines one at a time

                    sentence.append(line.strip())

        elif(age>=21 and age<=35):
            with open('PythonSecond\Fortune Teller Code\Fortune3.txt') as file:
                
                for line in file: # for-each loop gives lines one at a time

                    sentence.append(line.strip())

        elif(age>=36 and age<=50):
            with open('PythonSecond\Fortune Teller Code\Fortune4.txt') as file:
                
                for line in file: # for-each loop gives lines one at a time

                    sentence.append(line.strip())

        elif(age>=51 and age<=65):
            with open('PythonSecond\Fortune Teller Code\Fortune5.txt') as file:
                
                for line in file: # for-each loop gives lines one at a time

                    sentence.append(line.strip())

        elif(age>=66 and age<=100):
            with open('PythonSecond\Fortune Teller Code\Fortune6.txt') as file:
                
                for line in file: # for-each loop gives lines one at a time

                    sentence.append(line.strip())

        else:
            print("Invalid Age")
            break


        length=len(sentence)
        random_index=random.randint(0, length-1)

        print(sentence[random_index])

        sentence.clear()

    





if __name__ == '__main__':
    main()