
print("_"*80,"\t")
print("*"*5,"WELCOME TO STUDENT MANAGEMENT SYSTEM","*"*5)
print("_"*80)

li=['Aman', 'shivam','Raju', 'mayank']

def student_list():
    for i in range(len(li)):
        print(li[i])

def add_data():
    n=input("\nEnter Student Name:")
    li.append(n)
    print("Student name added sucessfull....")
   

def remove_data():
    n=input("Enter student name:")
    if n in li:
        li.remove(n)
        print("remove data successfull.....")
    else:
        print("worng input")

def search_data():
    n=input("Enter student name:")
    if n in li:
        print("Name found.....")
    else:
        print("Record not found??")
    
        
        
    
    
while True:
   
    print("                                                         ")
    print("Please choose any one option:\n")
    print("1.To Viwe Student List: ")
    print("2.To Add New Student List ")
    print("3.To remove data")
    print("4.To Search Student name ")
    print("5. EXIT")
    ch=int(input("\nEnter any number:"))
    if ch==1:
        student_list()
    elif ch==2:
        add_data()
    elif ch==3:
        remove_data()
    elif ch==4:
        search_data()
    elif ch==5:
        exit()
    else:
        print("worng input")
     g=(input("continue y/n="))
     print("______________________________________________")

     if (g=="y" or g=="Y"):
         continue
     elif(g=="n" or g=="N"):
         break

