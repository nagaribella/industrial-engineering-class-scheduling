import prettytable as prettytable
import random as rnd
POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1
class Data:
    ROOMS = [["R201",30], ["R301A",40], ["R301B",40],
            ["R302",40], ["R303",40], ["R406",40]]
    MEETING_TIMES = [["MT1", "M 07:30 - 09:15"],
                     ["MT2", "M 09:20 - 11:05"],
                     ["MT3", "M 13:00 - 14:45"],
                     ["MT4", "M 14:50 - 16:35"],
                     ["MT5", "T 07:30 - 09:15"],
                     ["MT6", "T 09:20 - 11:05"],
                     ["MT7", "T 13:00 - 14:45"],
                     ["MT8", "T 14:50 - 16:35"],
                     ["MT9", "W 07:30 - 09:15"],
                     ["MT10", "W 13:00 - 14:45"],
                     ["MT11", "W 14:50 - 16:35"],
                     ["MT12", "TH 07:30 - 09:15"],
                     ["MT13", "TH 09:20 - 11:05"],
                     ["MT14", "TH 13:00 - 14:45"],
                     ["MT15", "TH 14:50 - 16:35"],
                     ["MT16", "F 07:30 - 09:15"],
                     ["MT17", "F 09:20 - 11:05"],
                     ["MT18", "F 13:00 - 14:45"],
                     ["MT19", "F 14:50 - 16:35"]]
    #JANGAN LUPA PENULISAN INDEKS DIMULAI DARI 0 BUKAN 1 PROF SUSY BERARTI INDEKS KE 0 DST
    INSTRUCTORS = [["SS", "Prof. Dr. IR. Susy Susmartini, MSIE"],
                   ["CNR", "Prof. Dr. Cucuk Nur Rosyidi, ST, MT"],
                   ["LH", "Dr. Ir. Lobes Herdiman, MT"],
                   ["BS", "Prof. Dr. Bambang Suhardi, ST, MT"],
                   ["EP", "Dr. Eko Pujiyanto, Ssi, MT"],
                   ["MH", "Dr. Muh. Hisjam, STP, MT"],
                   ["EL", "Dr. Eko Liquiddanu, ST, MT"],
                   ["WS", "Prof. Dr. Wahyudi Sutopo, ST, M.Si"],
                   ["RDA", "Rahmaniyah Dwi A., ST, MT"],
                   ["IRF", "Irwan Iftadi, ST, M. Eng."],
                   ["MNF", "Ir. Munifah, MSIE, MT"],
                   ["RHS", "Dr. Ir. R. Hari Setyanto, M.Si"],
                   ["FF", "Fakhrina Fahma, STP, MT"],
                   ["YA", "Yuniaristanto, ST, MT"],
                   ["IWS", "I WAYAN SULETRA, S.T.,M.T."],
                   ["RWD", "RETNO WULAN DAMAYANTI, S.T., M.T."],
                   ["PWL", "PRINGGO WIDYO LAKSONO, ST., M.Eng."],
                   ["RZ", "RONI ZAKARIA, S.T.,M.T."],
                   ["YP", "YUSUF PRIYANDARI, S.T.,M.T."], 
                   ["TR", "Taufiq Rochman, S.TP.,M.T."],
                   ["L01", "Drs. SANTOSO BUDI WIYONO, M.Si."],
                   ["L02", "VIKA YUGI KURNIAWAN, S.Si., M.Sc."],
                   ["L03", "Drs. Slamet , M.Pd"],
                   ["L04", "Dr. Sumarwati, M.Pd."],
                   ["L05", "Dr. Nina Sutrisna, M.Pd."],
                   ["L06", "Dr. Yuli Muliawan, M.Pd."]]
    def __init__(self):
        self._rooms = []; self._meetingTimes = []; self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        #semester 1
        course1A = Course("C1A", "Pengantar Teknik Industri", [self._instructors[6], self._instructors[3], self._instructors[1], self._instructors[18]], 39)
        course1B = Course("C1B", "Pengantar Teknik Industri", [self._instructors[6], self._instructors[3], self._instructors[1], self._instructors[18]], 40)
        course1C = Course("C1C", "Pengantar Teknik Industri", [self._instructors[6], self._instructors[3], self._instructors[1], self._instructors[18]], 38)
        course2A = Course("C2A", "Pengantar Ilmu Ekonomi", [self._instructors[17], self._instructors[6]], 40)
        course2B = Course("C2B", "Pengantar Ilmu Ekonomi", [self._instructors[17], self._instructors[6]], 40)
        course2C = Course("C2C", "Pengantar Ilmu Ekonomi", [self._instructors[17], self._instructors[6]], 40)
        course3A = Course("C3A", "Sistem Lingkungan Industri", [self._instructors[3], self._instructors[11]], 38)
        course3B = Course("C3B", "Sistem Lingkungan Industri", [self._instructors[3], self._instructors[11]], 37)
        course3C = Course("C3C", "Sistem Lingkungan Industri", [self._instructors[3], self._instructors[11]], 36)
        course4A = Course("C4A", "Menggambar Teknik", [self._instructors[18], self._instructors[10]], 38)
        course4B = Course("C4B", "Menggambar Teknik", [self._instructors[18], self._instructors[10]], 37)
        course4C = Course("C4C", "Menggambar Teknik", [self._instructors[18], self._instructors[10]], 36)
        course5A = Course("C5A", "Kalkulus 1", [self._instructors[21]], 38)
        course5B = Course("C5B", "Kalkulus 1", [self._instructors[21]], 38)
        course5C = Course("C5C", "Kalkulus 1", [self._instructors[21]], 37)
        course6A = Course("C6A", "Agama Islam", [self._instructors[22]], 33)
        course6B = Course("C6B", "Agama Islam", [self._instructors[22]], 35)
        course6C = Course("C6C", "Agama Islam", [self._instructors[22]], 28)
        course7A = Course("C7A", "Fisika Dasar I", [self._instructors[23]], 38)
        course7B = Course("C7B", "Fisika Dasar I", [self._instructors[23]], 37)
        course7C = Course("C7C", "Fisika Dasar I", [self._instructors[23]], 36)
        course8A = Course("C8A", "Kewarganegaraan", [self._instructors[20]], 38)
        course8B = Course("C8B", "Kewarganegaraan", [self._instructors[20]], 37)
        course8C = Course("C8C", "Kewarganegaraan", [self._instructors[20]], 40)
        course9A = Course("C9A", "Bahasa Inggris", [self._instructors[24]], 38)
        course9B = Course("C9B", "Bahasa Inggris", [self._instructors[24]], 37)
        course9C = Course("C9C", "Bahasa Inggris", [self._instructors[24]], 36)
        course10A = Course("C10A", "Kimia Dasar", [self._instructors[25]], 38)
        course10B = Course("C10B", "Kimia Dasar", [self._instructors[25]], 38)
        course10C = Course("C10C", "Kimia Dasar", [self._instructors[25]], 36)
        #semester 3
        course11A = Course("C11A", "Aljabar Linear", [self._instructors[20], self._instructors[21]], 40)
        course11B = Course("C11B", "Aljabar Linear", [self._instructors[20], self._instructors[21]], 36)
        course11C = Course("C11C", "Aljabar Linear", [self._instructors[20], self._instructors[21]], 38)
        course12A = Course("C12A", "Proses Manufaktur I", [self._instructors[2], self._instructors[11]], 40)
        course12B = Course("C12B", "Proses Manufaktur I", [self._instructors[2], self._instructors[11]], 37)
        course12C = Course("C12C", "Proses Manufaktur I", [self._instructors[2], self._instructors[11]], 38)
        course13A = Course("C13A", "Elektronika Industri", [self._instructors[9]], 40)
        course13B = Course("C13B", "Elektronika Industri", [self._instructors[9]], 37)
        course13C = Course("C13C", "Elektronika Industri", [self._instructors[9]], 38)
        course14A = Course("C14A", "Ekonomi Teknik", [self._instructors[5], self._instructors[7]], 40)
        course14B = Course("C14B", "Ekonomi Teknik", [self._instructors[5], self._instructors[7]], 36)
        course14C = Course("C14C", "Ekonomi Teknik", [self._instructors[5], self._instructors[7]], 38)
        course15A = Course("C15A", "Elemen Mesin", [self._instructors[19]], 40)
        course15B = Course("C15B", "Elemen Mesin", [self._instructors[19]], 37)
        course15C = Course("C15C", "Elemen Mesin", [self._instructors[19]], 39)
        course16A = Course("C16A", "Teori Probabilitas", [self._instructors[4], self._instructors[12]], 40)
        course16B = Course("C16B", "Teori Probabilitas", [self._instructors[4], self._instructors[12]], 37)
        course16C = Course("C16C", "Teori Probabilitas", [self._instructors[4], self._instructors[12]], 39)
        course17A = Course("C17A", "Ergonomi", [self._instructors[3], self._instructors[8]], 40)
        course17B = Course("C17B", "Ergonomi", [self._instructors[3], self._instructors[8]], 37)
        course17C = Course("C17C", "Ergonomi", [self._instructors[3], self._instructors[8]], 37)
        course18A = Course("C18A", "Bahasa Indonesia", [self._instructors[22], self._instructors[23]], 26)
        course18B = Course("C18B", "Bahasa Indonesia", [self._instructors[22], self._instructors[23]], 22)
        course18C = Course("C18C", "Bahasa Indonesia", [self._instructors[22], self._instructors[23]], 16)
        course19A = Course("C19A", "Matematika Optimisasi", [self._instructors[4], self._instructors[14]], 40)
        course19B = Course("C19B", "Matematika Optimisasi", [self._instructors[4], self._instructors[14]], 36)
        course19C = Course("C19C", "Matematika Optimisasi", [self._instructors[4], self._instructors[14]], 38)
        #semester 5
        course20A = Course("C20A", "Perencanaan dan Pengendalian Produksi", [self._instructors[1], self._instructors[16]], 35)
        course20B = Course("C20B", "Perencanaan dan Pengendalian Produksi", [self._instructors[1], self._instructors[16]], 30)
        course20C = Course("C20C", "Perencanaan dan Pengendalian Produksi", [self._instructors[1], self._instructors[16]], 30)
        course21A = Course("C21A", "Penelitian Operasional II", [self._instructors[0], self._instructors[15]], 34)
        course21B = Course("C21B", "Penelitian Operasional II", [self._instructors[0], self._instructors[15]], 33)
        course21C = Course("C21C", "Penelitian Operasional II", [self._instructors[0], self._instructors[15]], 33)
        course22A = Course("C22A", "Pemodelan Sistem", [self._instructors[18], self._instructors[10]], 33)
        course22B = Course("C22B", "Pemodelan Sistem", [self._instructors[18], self._instructors[10]], 33)
        course22C = Course("C22C", "Pemodelan Sistem", [self._instructors[18], self._instructors[10]], 30)
        course23A = Course("C23A", "Pengendalian dan Penjaminan Mutu", [self._instructors[12], self._instructors[15]], 36)
        course23B = Course("C23B", "Pengendalian dan Penjaminan Mutu", [self._instructors[12], self._instructors[15]], 36)
        course23C = Course("C23C", "Pengendalian dan Penjaminan Mutu", [self._instructors[12], self._instructors[15]], 36)
        course24A = Course("C24A", "Otomasi Sistem Produksi", [self._instructors[16], self._instructors[2]], 35)
        course24B = Course("C24B", "Otomasi Sistem Produksi", [self._instructors[16], self._instructors[2]], 35)
        course24C = Course("C24C", "Otomasi Sistem Produksi", [self._instructors[16], self._instructors[2]], 35)
        course25A = Course("C25A", "Kewirausahaan", [self._instructors[13], self._instructors[5]], 37)
        course25B = Course("C25B", "Kewirausahaan", [self._instructors[13], self._instructors[5]], 37)
        course25C = Course("C25C", "Kewirausahaan", [self._instructors[13], self._instructors[5]], 36)
        course26A = Course("C26A", "Pemasaran", [self._instructors[17], self._instructors[13]], 38)
        course26B = Course("C26B", "Pemasaran", [self._instructors[17], self._instructors[13]], 38)
        course26C = Course("C26C", "Pemasaran", [self._instructors[17], self._instructors[13]], 38)
        #semester 7
        course27A = Course("C27A", "Proyek Peran. Terpadu", [self._instructors[16], self._instructors[3], self._instructors[13], self._instructors[5], self._instructors[15], self._instructors[11], self._instructors[6]], 25)
        course27B = Course("C27B", "Proyek Peran. Terpadu", [self._instructors[16], self._instructors[3], self._instructors[13], self._instructors[5], self._instructors[15], self._instructors[11], self._instructors[6]], 25)
        course27C = Course("C27C", "Proyek Peran. Terpadu", [self._instructors[16], self._instructors[3], self._instructors[13], self._instructors[5], self._instructors[15], self._instructors[11], self._instructors[6]], 25)
        course28A = Course("C28A", "Rekayasa Rantai Pasok", [self._instructors[7], self._instructors[13]], 31)
        course28B = Course("C28B", "Rekayasa Rantai Pasok", [self._instructors[7], self._instructors[13]], 31)
        course28C = Course("C28C", "Rekayasa Rantai Pasok", [self._instructors[7], self._instructors[13]], 31)
        course29A = Course("C29A", "Proposal Tugas Akhir", [self._instructors[1], self._instructors[14], self._instructors[12],  self._instructors[2], self._instructors[8]], 35)
        course29B = Course("C29B", "Proposal Tugas Akhir", [self._instructors[1], self._instructors[14], self._instructors[12],  self._instructors[2], self._instructors[8]], 34)
        course30 = Course("C30", "Perancangan Material Handling Ramah Lingkungan ", [self._instructors[6]], 6)
        course31 = Course("C31", "Ergonomi Fisik", [self._instructors[3], self._instructors[8]], 10)
        course32 = Course("C32", "Analisis Komparasi Kuantitatif", [self._instructors[15]], 10)
        course33 = Course("C33", "Mekanisme Sistem Mekanik", [self._instructors[19]], 11)
        course34A = Course("C34A", "Manajemen proyek", [self._instructors[0], self._instructors[15]], 40)
        course34B = Course("C34B", "Manajemen proyek", [self._instructors[0], self._instructors[15]], 40)
        course34C = Course("C34C", "Manajemen proyek", [self._instructors[0], self._instructors[15]], 40)
        course35 = Course("C35", "Aplikasi Ergonomi Industri", [self._instructors[3], self._instructors[8]], 10)
        course36 = Course("C36", "Sistem Pendukung Keputusan", [self._instructors[18]], 5)
        course37 = Course("C37", "Perbaikan Metode Kerja", [self._instructors[3], self._instructors[8]], 10)
        course38 = Course("C38", "Assistive Technology", [self._instructors[2]], 7)
        course39 = Course("C39", "Manajemen Perawatan", [self._instructors[14]], 6)
        #JANGAN LUPA BAGIAN DI BAWAH INI JUGA DIEDIT YA GUYS SELF.COURSES SAMA DEPT 1 DITAMBAHI SESUAI PENAMBAHAN COURSE PER KELAS
        self._courses = [course1A, course1B, course1C, course2A, course2B, course2C, course3A, course3B,course3C, course4A, 
                        course4B, course4C, course5A, course5B, course5C, course6A, course6B, course6C, course7A, course7B, 
                        course7C, course8A, course8B, course8C, course9A, course9B, course9C, course10A, course10B, course10C,
                        course11A, course11B, course11C, course12A, course12B, course12C, course13A, course13B, course13C, 
                        course14A, course14B, course14C, course15A, course15B, course15C, course16A, course16B, course16C, 
                        course17A, course17B, course17C, course18A, course18B, course18C, course19A, course19B, course19C, 
                        course20A, course20B, course20C, course21A, course21B, course21C, course22A, course22B, course22C, course23A, course23B, course23C, course24A, course24B, course24C, course25A, course25B, course25C, course26A, course26B, course26C, course27A, course27B, course27C, course28A, course28B, course28C, course29A, course29B, 
                        course30, course31, course32, course33, course34A, course34B, course34C, course35, course36, course37, course38, course39]
        dept1 = Department("Industrial", [course1A, course1B, course1C, course2A, course2B, course2C, course3A, course3B,course3C, course4A,
                        course4B, course4C, course5A, course5B, course5C, course6A, course6B, course6C, course7A, course7B, 
                        course7C, course8A, course8B, course8C, course9A, course9B, course9C, course10A, course10B, course10C, 
                        course11A, course11B, course11C, course12A, course12B, course12C, course13A, course13B, course13C, 
                        course14A, course14B, course14C, course15A, course15B, course15C, course16A, course16B, course16C, 
                        course17A, course17B, course17C, course18A, course18B, course18C, course19A, course19B, course19C, 
                        course20A, course20B, course20C, course21A, course21B, course21C, course22A, course22B, course22C, course23A, course23B, course23C, course24A, course24B, course24C, course25A, course25B, course25C, course26A, course26B, course26C, course27A, course27B, course27C, course28A, course28B, course28C, course29A, course29B,
                        course30, course31, course32, course33, course34A, course34B, course34C, course35, course36, course37, course38, course39])
        self._depts = [dept1]
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())
    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses
class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def get_numbOfConflicts(self): return self._numbOfConflicts
    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness
    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
                newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])
                self._classes.append(newClass)
        return self
    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents()):
                self._numbOfConflicts += 1
            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and
                    classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room() == classes[j].get_room()): self._numbOfConflicts += 1
                        if (classes[i].get_instructor() == classes[j].get_instructor()): self._numbOfConflicts += 1
        return 1 / ((1.0*self._numbOfConflicts + 1))
    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue
class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())
    def get_schedules(self): return self._schedules
class GeneticAlgorithm:
    def evolve(self, population): return self._mutate_population(self._crossover_population(population))
    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop
    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population
    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5): crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule
    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule
    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop
class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents):
        self._number = number
        self._name = name
        self._maxNumbOfStudents = maxNumbOfStudents
        self._instructors = instructors
    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_instructors(self): return self._instructors
    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
    def __str__(self): return self._name
class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name
class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity
    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity
class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time
    def get_id(self): return self._id
    def get_time(self): return self._time
class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses
    def get_name(self): return self._name
    def get_courses(self): return self._courses
class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room
    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(self._meetingTime.get_id())
class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()
    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)
    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(['id', 'course #', 'max # of students', 'instructors'])
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ", "
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr])
        print(availableCoursesTable)
    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructor'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)
    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)
    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(['id', 'Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)
    def print_generation(self, population):
        #table1 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [dept,class,room,instructor,meeting-time]'])
        table1 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            #table1.add_row([str(i), round(schedules[i].get_fitness(),3), schedules[i].get_numbOfConflicts(), schedules[i].__str__()])
            table1.add_row([str(i), round(schedules[i].get_fitness(),3), schedules[i].get_numbOfConflicts()])
        print(table1)
    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(['Class #', 'Dept', 'Course (number, max # of students)', 'Room (Capacity)', 'Instructor (Id)',  'Meeting Time (Id)'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " +
                           str(classes[i].get_course().get_maxNumbOfStudents()) +")",
                           classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name() +" (" + str(classes[i].get_instructor().get_id()) +")",
                           classes[i].get_meetingTime().get_time() +" (" + str(classes[i].get_meetingTime().get_id()) +")"])
        print(table)
data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # "+str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm()
max_iter = 100 #JUMLAH ITERASI YANG DIINGINKAN
curr_iter = 0 
while (population.get_schedules()[0].get_fitness() != 1.0):
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    # displayMgr.print_schedule_as_table(population.get_schedules()[0])
    if curr_iter >= max_iter:
        break
    curr_iter += 1
print("\n\n")
displayMgr.print_schedule_as_table(population.get_schedules()[0])