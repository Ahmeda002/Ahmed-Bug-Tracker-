import random 
def show_menu():
    print("\nbug Tracker")
    print("1. add bug")
    print("2. view bug")
    print("3. update bug")
    print("4. delete bug")
    print("5. exit bug")

def main():
    bugs=[]
    next_id=1
    while True:
        show_menu()
        choice=input("Enter a menu option")
        if choice == "1":
            print("Adding a bug... (placeholder)")
            bugtitle=input("Whats the title of the bug").strip()
            bugdescription=input("Whats the description of the bug").strip()
            severity=input("Whats the severity(Low,medium, or high)").strip()
            while severity.lower() not in ["low", "medium", "high"]:
                severity = input("Invalid severity. Enter Low, Medium, or High: ").strip()

            severity=severity.capitalize
            status="Open"

            bug={"id":next_id,
                  "title":bugtitle,
                  "description":bugdescription,
                  "severity":severity,
                  "status":status
                  }
            bugs.append(bug)
            print("Bug added successfully")
            next_id +=1
        
        elif choice == "2":
            print("Viewing bugs... (placeholder)")
            if not bugs:
                print("No bugs")
            else:
                print("\nAll bugs:")
                for bug in bugs:
                    print(f"ID: {bug['id']} | title: {bug['title']} | status: {bug['status']}")

                look_description = input("\nDo you want to view a bug's description? (y/n): ").strip().lower()
                if look_description == 'y':
                    try:
                        which_id = int(input("Enter the bug ID: ").strip())
                    except ValueError:
                        print("Invalid ID (must be a number).")
                    else:
                        match = next((b for b in bugs if b['id'] == which_id), None)
                        if match is None:
                            print("No bug found with that ID.")
                        else:
                            print("\nBug details:")
                            print(f"ID: {match['id']}")
                            print(f"Title: {match['title']}")
                            print(f"Severity: {match['severity']}")
                            print(f"Status: {match['status']}")
                            print(f"Description: {match['description']}")

        elif  choice == "3":
            print("Updating a bug... (placeholder)")
        elif choice == "4":
            print("Deleting a bug... (placeholder)")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")



if __name__=="__main__":
    main()