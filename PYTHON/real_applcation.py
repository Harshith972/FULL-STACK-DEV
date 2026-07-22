#student managemengt system
#read only
SYSTEM_INFO=("Digital Tech ","Student Management System"," v1 ")

ADMIN_INFO=("9999999999","admin@digital.com")

print("="*50)
print(f"welcome to {SYSTEM_INFO[0]}" )
print(f"software: {SYSTEM_INFO[1]}")

print(f"version: {SYSTEM_INFO[2]}")
      
print(f"admin contact: {ADMIN_INFO[0]} | {ADMIN_INFO[1]}")

print("="*50)


# Store Students Info -> Dictionary
students = {}

# Build Menu System For Different CRUD Operations 
while True:
    print("Choose An Option: ")
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Create Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id  = input("Enter ID: ")
        
        if student_id in students:
            print("OOPS! Student ID Already Exists!!!")
        else:
            name = input("Enter Name: ").title()
            
            scores = []
            while True:
                score_input = input("Enter Score or Type done: ")
                if score_input == "done":
                    break 
                
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score Should be (0-100)")
                else:
                    print("Invalid Score, Score Should be Digits Only")
                    
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or Type done: ")
                
                if skill_input == "done":
                    break   
                else:
                    skills.add(skill_input)
                    
            
            print(students) # Before Adding
            
            print("======== Student Added ========")
            
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print(students) # After Adding i.e for Confirmation
                    
               
        
    elif choice == "2":
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
    elif choice == "3":
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
    elif choice == "4":
        # Read Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)
        
    elif choice == "5":
        # Exit Application
        print("=" * 30)
        print("     Exiting application")
        print("=" * 30)
        break
        
    else :
        # Invalid Choice
        print("=" * 50)
        print("     Invalid Option Selected, Only Use (1-5)")
        print("=" * 50)
    