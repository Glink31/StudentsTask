from menu import Menu
from command import (
    add_student_command,
    list_students_command,
    delete_student_command,
    show_low_achievers_command,
    show_high_achievers_command,
    select_student_command,
    show_selected_student_command,
    deselect_student_command,
    edit_name_command,
    edit_surname_command,
    edit_patronymic_command,
    edit_group_command,
    add_mark_command,
    edit_mark_command,
    delete_mark_command
) 

main_menu = Menu()
main_menu.additem('Список студентов',list_students_command)
main_menu.additem('Добавить студента',add_student_command)
sub = main_menu.addSubmenu('Редактировать студента')
sub.onStartCommand = select_student_command
sub.beforeSelectedCommand = show_selected_student_command
sub.onFinishCommand = deselect_student_command
sub.additem('Изменить имя',edit_name_command)
sub.additem('Изменить фамилию',edit_surname_command)
sub.additem('Изменить отчество',edit_patronymic_command)
sub.additem('Изменить группу',edit_group_command)
sub.additem('Добавить оценку',add_mark_command)
sub.additem('Изменить оценку',edit_mark_command)
sub.additem('Удалить оценку',delete_mark_command)
main_menu.additem('Удалить студента',delete_student_command)
main_menu.additem('Показать отличников',show_high_achievers_command)
main_menu.additem('Показать неуспевающих',show_low_achievers_command)
main_menu.run()
