import json


def file_manager():
    json_file = input("Json File: ")
    with open(json_file, "r") as file:
        data = json.load(file)
    current_location = "data"
    while True:
        if type(eval(current_location)) == dict:
                print("\n" + str(list(eval(current_location).keys())))
        elif type(eval(current_location)) == list:
            for each in eval(current_location):
                print("\n" + str(each))
        else:
            print(print("\n" + str(eval(current_location))))
        command = input("\n1.Enter name of next location to go to next location\n"
                        "2.Enter back to previous location\n"
                        "3.Enter exit to finish execution\n\n")
        if command == "exit":
            break
        elif command == "back":
            current_location = current_location[:-last_command_len]
        elif type(eval(current_location)) == list:
            current_location = current_location + "[" + command + "]"
            last_command_len = len(command) + 2
        else:
            current_location = current_location + "[\"" + command + "\"]"
            last_command_len = len(command) + 4
        print(current_location)


if __name__ == '__main__':
    file_manager()
