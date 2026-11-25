import sys



class Respondent:
    """Класс для хранения информации об участнике опроса."""
    def __init__(self, fio: str, age: int) -> None:
        self.fio = fio
        self.age = age



class AgeGroup:
    """Класс для хранения участников определенной возрастной группы."""
    def __init__(self, lower_limit: int, high_limit: int) -> None:
        self.lower_limit = lower_limit
        self.high_limit = high_limit
        self.people = []


    def add_person(self,person: Respondent) -> None:
        """ Добавить участника в возрастную группу."""
        self.people.append(person)

    def sort_people(self) -> None:
        """ Отсортировать участников группы."""
        self.people.sort(key=lambda x: x.fio)
        self.people.sort(key=lambda x: x.age, reverse=True)

class Survey:
    """Класс для управления опросом и распределения участников по возрастным группам."""

    def __init__(self) -> None:
        self.groups = []

    def create_groups(self,boundaries:list[int]) -> None:
        """Создать возрастные группы на основе заданных границ."""
        group = AgeGroup(0,boundaries[0])
        self.groups.append(group)
        for i in range(1,len(boundaries)):
            self.groups.append(AgeGroup(boundaries[i-1]+1, boundaries[i]) )

        self.groups.append(AgeGroup(boundaries[-1]+1,123))


    def distribute_person(self, person:Respondent) -> None:
        """Распределить участника по подходящей возрастной группе."""
        for group in self.groups:
            if group.lower_limit<= person.age <= group.high_limit:
                group.add_person(person)
                break


    def sort_groups(self) -> None:
        """Отсортировать возрастные группы и участников внутри них."""
        self.groups.reverse()
        for group in self.groups:
            group.sort_people()

    def print_groups(self) -> None:
        """Вывести непустые возрастные группы и их участников."""
        for group in self.groups:

            if not group.people:
                continue

            s=[]
            for person in group.people:

                s.append(str(person.fio) + " (" + str(person.age) + ")")
            result = ', '.join(s)

            print(str(group.lower_limit)+'-'+str(group.high_limit)+': '+ result)












if __name__ == "__main__":
    # Получение границ возрастных групп из аргументов командной строки
    boundaries = [int(x) for x in sys.argv[1:]]\

    survey = Survey()
    survey.create_groups(boundaries)

    # Чтение данных об участниках и их распределение по группам
    person_data = input()

    while person_data!="END":

        parts = person_data.split(",")
        fio = parts[0]
        age = int(parts[1])

        person = Respondent(fio,age)

        survey.distribute_person(person)
        person_data = input()

    # Сортировка и вывод результатов
    survey.sort_groups()
    survey.print_groups()


