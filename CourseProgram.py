"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    import CourseClass as cc

    my_course = cc.Course(name, crn, seats, status)

    for name in students:
        if my_course.get_status() == "open":
            studentR = cc.Register(name, "crn")
            print("Student Name: ", studentR.get_name())
            print("Course Name: ", my_course.get_name())
            print("CRN: ", my_course.get_crn())
            print("Seats Left: ", (my_course.get_seats() - 1))
            print()
            (my_course.get_status())
            (my_course.update_seat_count())
        else:
            print("Sorry ", name, ", registration is closed for", my_course.get_name())


main()
