from student_visitor import StudentVisitor
class BriefPrintVisitor(StudentVisitor):
  def start_visit(self):
    self.has_students = False

  def visit_student(self, index, student):
    print(f"{index}. ",end="")
    student.print_brief()
    self.has_students = True

  def finish_visit(self):
    if not self.has_students:
      print("В базе данных еще нет студентов")