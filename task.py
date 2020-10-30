import statistics

class Student:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.scores = []
    self.attendances = []

  def add_score(self, score):
    self.scores.append(score)

  def add_attendance(self, attendance):
    self.attendances.append(attendance)

  def get_avegare_of_scores(self):
    return statistics.mean(self.scores)

  def get_num_of_attendances(self):
    return sum(self.attendances)

class SchoolClass:
  def __init__(self):
    self.students = []

  def add_student(self, student):
    self.students.append(student)

  def average_score_across_class(self):
    all_average_scores = []
    for student in self.students:
      all_average_scores.append(student.get_avegare_of_scores())
    return statistics.mean(all_average_scores)

class School:
  def __init__(self):
    self.school_classes = []

  def add_school_class(self, school_class):
    self.school_classes.append(school_class)

if __name__ == "__main__":
  student1 = Student("John", "Doe")
  student1.add_score(1)
  student1.add_score(1)
  student1.add_score(1)
  print(student1.get_avegare_of_scores())

  student1.add_attendance(True)
  student1.add_attendance(True)
  student1.add_attendance(True)
  student1.add_attendance(False)

  print(student1.get_num_of_attendances())

  student2 = Student("John2", "Doe2")
  student2.add_score(6)
  student2.add_score(6)
  student2.add_score(4)
  print(student2.get_avegare_of_scores())

  classA = SchoolClass()
  classA.add_student(student1)
  classA.add_student(student2)
  print(classA.average_score_across_class())

  student3 = Student("John3", "Doe3")
  student3.add_score(6)
  student3.add_score(6)
  student3.add_score(4)

  classA.add_student(student3)
  print(classA.average_score_across_class())