from student_visitor import StudentVisitor
class DetailedPrintVisitor(StudentVisitor):
  def start_visit(self):
    self.has_students = False

  def visit_student(self, index, student):
    print(f"=== {index} ===")
    student.print_detailed()
    self.has_students = True

  def finish_visit(self):
    if not self.has_students:
      print("В базе данных еще нет студентов")