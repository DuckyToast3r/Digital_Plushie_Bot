
def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contains letters")
        else:
            return response.title()

question = "Enter your name "
name = check_string(question) 
print(name)