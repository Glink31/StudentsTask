from student_visitor import StudentVisitor
class LowAchieverPrintVisitor(StudentVisitor):
  def start_visit(self):
    self.has_Low_Achievers = False

  def visit_student(self, index, student):
    if student.isLowAchiever():
        print(f"=== {index} ===")
        student.print_detailed()
        self.has_Low_Achievers = True

  def finish_visit(self):
    if not self.has_Low_Achievers:
      print("В базе данных нет неуспевающих")