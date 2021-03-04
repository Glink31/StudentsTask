from student_visitor import StudentVisitor
class HighAchieverPrintVisitor(StudentVisitor):
  def start_visit(self):
    self.has_High_Achievers = False

  def visit_student(self, index, student):
    if student.isHighAchiever():
        print(f"=== {index} ===")
        student.print_detailed()
        self.has_High_Achievers = True

  def finish_visit(self):
    if not self.has_High_Achievers:
      print("В базе данных нет отличников")