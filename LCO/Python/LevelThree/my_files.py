# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

def main():

    #TODO write("w+") or append("a+") a file

    # file = open("practice.text","a+")
    # for i in range(20):
    #     file.write("This is python code %d \n" %(i))
    # file.close()

    # TODO read("r") a file
    # file = open("practice.text","r")
    # if file.mode == 'r':
    #     filecontent = file.read()
    #     print(filecontent)

    #TODO exception

    try:
        file = open("practice.text","r")
        print("success in reading")
    except IOError:
        print("File does not exists")
    print("Task done")


if __name__ == "__main__":
    main()