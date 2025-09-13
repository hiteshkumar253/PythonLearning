sub1_marks = float(input("Enter the first subject marks: "))
sub2_marks = float(input("Enter the second subject marks: "))
sub3_marks = float(input("Enter the third subject marks: "))

total_percentage = ((sub1_marks+sub2_marks+sub3_marks)/300)*100

if(total_percentage>=40 and sub1_marks>=33 and sub2_marks>=33 and sub3_marks>=33 ):
    print("✅ Yor are PASSED: ", total_percentage)
else:
    print("❌ You FAILED: ", total_percentage)



    

 

