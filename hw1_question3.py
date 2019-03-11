
def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    for name in subj1_all_students:
        if name in subj2_all_students:
            subj1_grade = subj1_all_students[name]
            subj2_grade = subj2_all_students[name]
            print (name+"\t", max(subj1_grade,subj2_grade))


        


dic1 = {"Jack" : 90, "Dor" : 85, "Liri" : 85, "Dan" : 92, "Daniel" : 70}
dic2 = {"Jack" : 91, "Liri" : 87, "Dan" : 92, "Daniel" : 74}

compare_subjects_within_student(dic1,dic2)

