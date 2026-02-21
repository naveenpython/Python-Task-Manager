import sqlite3


#create batabase and table setup
conn=sqlite3.connect("task_manager.db")
cursor=conn.cursor()

#create a table row and column
cursor.execute("""create table if not exists tasks(
               id integer primary key autoincrement,
               task_name text,
               status text
               )

""")
#save the data 
conn.commit()
print("----welcome to naveen's task manager----")
while True:
    print("\n Main Menu:-")
    print("1.add new task !")
    print("2.view all task ")
    print("3.mark task as done")
    print("4.Exit ")


    #input from the user
    choice = int(input("Enter your choice ex.(1-4): "))
    
    #used the condition
    if choice ==1:
        new_task=input("write your task name !")

        cursor.execute("insert into tasks(task_name,status) values (?,?)",(new_task,"pending"))
        conn.commit()
        print(f" save : {new_task}")


        print(f"task,{new_task}, save your data in our batabase")
    elif choice ==2:
        print("-------your task list------")
        cursor.execute("select * from tasks")
        all_tasks=cursor.fetchall()
        if not all_tasks:
            print("now first add your tasks ")
        else:
            for t in all_tasks:
                print(f"[{t[0]}] {t[1]} status: {t[2]}")
    elif choice==3:
        #--feature update status--
        task_id= int(input("who task is complete please mention the number "))
        #update the sql querry
        cursor.execute("update tasks set status = 'completed' where id = ?",(task_id,))
        conn.commit()
        print(f"Congratulation {task_id} your task is completed ")
    elif choice==4:
        print(f"bye bye ")
        #close the loop
        break
    else:
        print("please enter the valid key ! try again ")
conn.close()
