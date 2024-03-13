class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show(self):
        print(f'Имя: {self.name}, Возраст: {self.age}, Пол: {self.sex}')


class Worker(Human):
    def __init__(self, name, age, sex, occupation, work_length):
        super().__init__(name, age, sex)
        self.occupation = occupation
        self.work_length = work_length

    def show(self):
        super().show()
        print(f'Должность: {self.occupation}, Стаж: {self.work_length}')


class Engineer(Human):
    def __init__(self, name, age, sex, education, company):
        super().__init__(name, age, sex)
        self.education = education
        self.company = company

    def show(self):
        super().show()
        print(f'Образование: {self.education}, Фирма: {self.company}')


class SeniorResearcher(Engineer):
    def __init__(self, name, age, sex, education, company, research_topic):
        super().__init__(name, age, sex, education, company)
        self.research_topic = research_topic

    def show(self):
        super().show()
        print(f'Тема научной работы: {self.research_topic}')


worker = Worker('Иван', 30, 'М', 'Инженер', 5)
engineer = Engineer('Елена', 35, 'Ж', 'Высшее', 'Газпром')
researcher = SeniorResearcher('Алексей', 40, 'М', 'Доктор наук', 'Газпром', 'Исследование новых материалов')

worker.show()
engineer.show()
researcher.show()
