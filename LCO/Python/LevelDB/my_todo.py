import db_helper

def main():
    run=1
    db_helper.create_table()

    while run:
        print("\n")
        print("1. Insert new task in todo list \n"
              "2. View the todo list \n"
              "3. Delete the task \n"
              "4. Exit \n")
        x=input("Choose any of above options: ")
        if x=="1":
            task=str(input("Enter your todo: "))
            db_helper.data_entry(task)
        elif x=="2":
            db_helper.printData()
        elif x=="3":
            index_to_be_deleted=int(input("Enter the index of task to be deleted: "))
            db_helper.deleteTask(index_to_be_deleted)
        elif x=="4":
            run=0
        else:
            print("Enter the valid options")

    db_helper.closeCursor()

if __name__ == '__main__' :
    main()