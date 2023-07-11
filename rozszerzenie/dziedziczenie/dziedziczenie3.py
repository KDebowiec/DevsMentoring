class Member:
    def __init__(self, name):
        self.full_name = name

    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')


class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason


payvand = Student('Payvand', 'Money')


class Instructor(Member):
    def __init__(self, name, bio, skillset):
        super().__init__(name)
        self.bio = bio
        self.skillset = skillset

    def add_skill(self, skill):
        self.skillset.append(skill)


brandon = Instructor('Brandon', 'I am a genius', ['React', 'Node', 'C'])


class Workshop():
    def __init__(self, date, subject, instructors, students):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students

    def add_participant(self, participant):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)

    def print_details(self):
        print(f'Workshop - {self.date} - {self.subject}\n')

        print('Students:')
        for s in self.students:
            print(f'{s.full_name} - {s.reason}')

        print('\nInstructors:')
        for i in self.instructors:
            print(f'{i.full_name} -  {i.skillset}')



workshop = Workshop("12/03/2014", "Shutl", [], [])

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.", ['Ruby - HTML', 'JavaScript'])
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love", ['Ruby'])
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()