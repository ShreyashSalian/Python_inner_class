class Student:
    def __init__(self, StudentName, StudentEmail, StudentContactNo):
        self.StudentName = StudentName
        self.StudentEmail = StudentEmail
        self.StudentContactNo = StudentContactNo
        self.s = self.Subject

    def setData(self, StudentName, StudentEmail, StudentContactNo):
        self.StudentName = StudentName
        self.StudentEmail = StudentEmail
        self.StudentContactNo = StudentContactNo
        self.s.setData(self)

    def getData(self):
        self.StudentName = input("Enter The Student Name : ")
        self.StudentEmail = input("Enter The Email : ")
        self.StudentContactNo = int(input("Enter The Contact Detail of Student : "))
        self.s.getData(self)

    def showData(self):
        print("The Name of The Student is : ", self.StudentName)
        print("The Email of The Student is : ", self.StudentEmail)
        print("The Student Contact Number is : ", self.StudentContactNo)
        self.s.showData(self)

    class Subject:
        """def __init__(self,Subject1,Subject2,total,percentage):
            self.Subject1 = Subject1
            self.Subject2 = Subject2
            self.total = total
            self.percentage = percentage
            self.total = Subject1 + Subject2
            self.percentage = self.total/200*100
            """

        def setData(self, Subject1, Subject2, total, percentage):
            self.Subject1 = Subject1
            self.Subject2 = Subject2
            self.total = total
            self.percentage = percentage

        def getData(self):
            self.Subject1 = float(input("Enter The Subject 1 Marks : "))
            self.Subject2 = float(input("Enter The Subject 2 Marks : "))
            self.total = self.Subject1 + self.Subject2
            self.percentage = self.total / 200 * 100

        def showData(self):
            print("The Marks in Subject 1 is :", self.Subject1)
            print("The Marks in Subject 2 is : ", self.Subject2)
            print("The Total Marks of Student is :", self.total)
            print("The Percentage of the Student is :", self.percentage)


s1 = Student("Shreyash", "sss@gmail.com", 9925123114)
s1.getData()
s1.showData()