import random
import pprint

class TimeTable:
    def __init__(self, disciplines, teachers, groups, rooms, students, maxdisc=4):
        self.disciplines = disciplines
        self.teachers = teachers
        self.groups = groups
        self.rooms = rooms
        self.students = students
        self.maxdisciplinesperday = maxdisc
        self.days = {'Mo': {}, 'Tu': {}, 'We': {}, 'Th': {}, 'Fr': {}}

    # random.choice(numberList)
    def createtimetable(self):
        for day in self.days:
            for group in self.groups:
                self.days[day][group] = {}

        pp = pprint.PrettyPrinter(indent=4)
        # add disciplines to tt
        for discipline in self.disciplines:
            self.adddisctott(discipline)
            pp.pprint(discipline)
        pp.pprint(self.days)

        sumgroups_exp = {}
        sumgroups_tt = {}
        for group in self.groups:
            sumgroups_exp[group] = 0
            sumgroups_tt[group] = 0

        for day in self.days:
            for group in self.days[day]:
                for discipl in self.days[day][group]:
                    sumgroups_tt[group] = sumgroups_tt[group] + 1
        print('sumgroups_tt')
        pp.pprint(sumgroups_tt)

        for group in self.groups:
            for disc in self.disciplines:
                if disc in self.groups[group]:
                    sumgroups_exp[group] = sumgroups_exp[group] + self.disciplines[disc]
        print('sumgroups_exp')
        pp.pprint(sumgroups_exp)

    def adddisctott(self, disc):
        day = ''
        lect = ''
        r = 0
        if 'lecture' in disc:
            for i in range(self.disciplines[disc]):
                can_add = False
                while not can_add:
                    day = random.choice([*self.days])
                    if len(day) < self.maxdisciplinesperday:
                        can_add = True
                for t in self.teachers:
                    if disc in self.teachers[t]:
                        lect = t
                r_value = len(self.students)
                available = []
                for r in self.rooms:
                    if self.rooms[r] >= r_value:
                        available.append(r)
                r = random.choice(available)
                busy_numbers = []
                for pair in self.days['Mo']['TTP1']:
                    busy_numbers.append(self.days['Mo']['TTP1'][pair]['number'])
                number = random.choice(list(set(list(range(self.maxdisciplinesperday))) - set(busy_numbers)))
                for group in self.groups:
                    if lect != '' and r != 0:
                        self.days[day][group][disc] = {'lecturer': lect, 'room': r, 'number': number}
        else:
            needy_groups = []
            for group in self.groups:
                if disc in self.groups[group]:
                    needy_groups.append(group)
            for i in range(self.disciplines[disc]):
                for group in needy_groups:
                    room = 0
                    numbers = []
                    teachers = []

                    for t in self.teachers:
                        if disc in self.teachers[t]:
                            teachers.append(t)

                    for day in self.days:
                        busy_numbers = []
                        for pair in self.days[day][group]:
                            busy_numbers.append(self.days[day][group][pair]['number'])
                        numbers = list(set(list(range(self.maxdisciplinesperday)))-set(busy_numbers))
                        if not numbers:
                            continue
                        busy_teachers = []
                        busy_rooms = []
                        for number in numbers:
                            for pair in self.days[day][group]:
                                if self.days[day][group][pair]['number'] == number:
                                    busy_teachers.append(self.days[day][group][pair]['lecturer'])
                                    busy_rooms.append(self.days[day][group][pair]['room'])
                            for teacher in list(set(teachers)-set(busy_teachers)):
                                self.days[day][group][disc] = {'lecturer': teacher, 'room': room, 'number': number}
                                print('added ', disc, ' to ', group, ' group!')
                                pp = pprint.PrettyPrinter(indent=4)
                                pp.pprint(self.days[day][group][disc])
                                break
                            break
                        break


                    # for day in self.days:
                    #     busy_numbers = []
                    #     for pair in self.days[day][group]:
                    #         busy_numbers.append(self.days[day][group][pair]['number'])
                    #     busy_rooms = []
                    #     for d in self.days:
                    #         for gr in self.days[d]:
                    #             for pair in self.days[d][gr]:
                    #                 busy_rooms.append(self.days[d][gr][pair]['room'])
                    #     if not list(set(self.rooms) - set(busy_rooms)):
                    #         continue
                    #     for room in list(set(self.rooms) - set(busy_rooms)):
                    #         number = random.choice(list(set(list(range(self.maxdisciplinesperday))) - set(busy_numbers)))
                    #         teachers = []
                    #         for t in self.teachers:
                    #             if disc in self.teachers[t]:
                    #                 teachers.append(t)
                    #         busy_teachers = []
                    #         for d in self.days:
                    #             for gr in self.days[d]:
                    #                 for pair in self.days[d][gr]:
                    #                     if self.days[d][gr][pair]['number'] == number:
                    #                         busy_teachers.append(self.days[d][gr][pair]['lecturer'])
                    #         if not list(set(teachers) - set(busy_teachers)):
                    #             continue
                    #         teacher = random.choice(list(set(teachers) - set(busy_teachers)))
                    #         if teacher != '' and room != 0 and number != 0:
                    #             added = True
                    #             self.days[day][group][disc] = {'lecturer': teacher, 'room': room, 'number': number}
                    #             break
                    print('added ', disc, ' to ', group, ' group!')

            # teachers = []
            # for x in self.teachers:
            #     if disc in self.teachers[x]:
            #         teachers.append(x)
            # print(disc, ': ', teachers)
            # for group in self.groups:
            #     for day in self.days:
            #         group_dont_have = False
            #         k = []
            #         for pairs in self.days[day][group]:
            #             k.append(pairs[:-1])
            #         if disc not in k:
            #             group_dont_have = True
            #         if disc in self.groups[group] and group_dont_have:
            #             for i in range(self.disciplines[disc]):
            #                 can_add = False
            #                 while not can_add:
            #                     day = random.choice([*self.days])
            #                     t = random.choice(teachers)
            #                     busy = []
            #                     for gr in self.days[day]:
            #                         for d in self.days[day][gr]:
            #                             # if self.days[day][gr][d]['lecturer'] == t:
            #                             busy.append(self.days[day][gr][d]['lecturer'])
            #                     busy_numbers = []
            #                     for day in self.days:
            #                         for gro in self.days[day]:
            #                             for pair in self.days[day][gro]:
            #                                 busy_numbers.append(self.days[day][gro][pair]['number'])
            #                             if len(busy_numbers) < 4:
            #                                 number = random.choice(list(set(list(range(self.maxdisciplinesperday))) - set(busy_numbers)))
            #                                 if number == 0:
            #                                     continue
            #                             else:
            #                                 continue
            #                     if len(self.days[day][group]) < self.maxdisciplinesperday and t not in busy:
            #                         can_add = True
            #                         available = []
            #                         for r in self.rooms:
            #                             if self.rooms[r] >= 3:
            #                                 available.append(r)
            #                         r = random.choice(available)
            #
            #                         if t != '' and r != 0:
            #                             self.days[day][group][disc + str(i + 1)] = {'lecturer': t, 'room': r, 'number': number}




disciplines = {
    'A lecture': 1,
    'E lecture': 1,
    'A1': 1,
    'A2': 1,
    'A3': 1,
    'B': 1,
    'C': 1,
    'E1': 1,
    'E2': 1,
    'D1': 1,
    'F1': 1,
    'G1': 1,
    'H1': 1,
    'D2': 1,
    'F2': 1,
    'G2': 1,
    'H2': 1,
    'D3': 1,
    'F3': 1,
    'G3': 1,
    'H3': 1,
    'D4': 1,
    'F4': 1,
    'G4': 1,
    'H4': 1,
}

teachers = {
    'A A': ['A1', 'A2', 'A3', 'A lecture'],
    'B B': ['A1', 'A2', 'A3'],
    'C C': ['B'],
    'D D': ['C', 'E1', 'E2'],
    'E E': ['D1', 'D2', 'D3', 'D4'],
    'F F': ['F1', 'F2', 'F3', 'F4'],
    'G G': ['G1', 'G2', 'G3', 'G4'],
    'H H': ['H1', 'H2', 'H3', 'H4'],
    'J J': ['E lecture', 'E1', 'E2'],
}

groups = {
    'TTP1': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'D1', 'D2', 'D3', 'D4'],
    'TTP2': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'F1', 'F2', 'F3', 'F4'],
    'TK': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'G1', 'G2', 'G3', 'G4'],
    'MI': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'H1', 'H2', 'H3', 'H4'],
}

rooms = {
    306: 3,
    307: 3,
    308: 3,
    309: 3,
    310: 3,
    311: 3,
    312: 3,
    42: 50,
    43: 50,
}

students = {
    'yarik': 'TTP1',
    'yegor': 'TTP1',
    'sanya': 'TTP1',
    'merk': 'TTP2',
    'holivets': 'TTP2',
    'mykhailov': 'TTP2',
    'dima': 'TK',
    'stas': 'TK',
    'danya': 'TK',
    'nikolya': 'MI',
    'oleg': 'MI',
    'selim': 'MI',
}

tt = TimeTable(disciplines, teachers, groups, rooms, students)
tt.createtimetable()
