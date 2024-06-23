#EXISTEM K PERIODOS DE FERIAS. EX: NATAL, REVEILLON, DIA DO TRABALHADOR (3 PERIODOS DE FERIAS)
#Dj é a quantidade de dias que o feriado representa. Por exemplo, Carnaval são 3 dias de férias
#Existem N médicos (ex: existem 6 médicos)
#Cada médico precisa trabalhar em um conjunto de feriados, mas nunca pode ser todo o feriado.
    #(EX: O carnaval tem 4 dias de feriado, o médico que for trabalhar no feriado, pode trabalhar até 3 dias)

class Day:
    def __init__(self, day):
        self.day = day
        self.hasDoctor = False
        self.doctors = []


class Holidays:
    def __init__(self, name):
        self.days = []
        self.name = name
    
    def insertDays(self, qtdDays):
        for i in range(qtdDays):
            self.days.append(Day(str(i)))
        
    def insertDoctorsInWorkHolidayDays(self, workDay, doctorName):
        self.days[int(workDay)].hasDoctor = True
        self.days[int(workDay)].doctors.append(doctorName)
    
    def checkIfDoctorIsAlreadyWorkingOnCurrentHoliday(self, doctorName):
        for day in self.days:
            if doctorName in day.doctors:
                return True
        return False
    
    def getDays (self):
        aux = []
        for i in self.days:
            aux.append(i.day)
        return aux
    
    def checkIfHolidayHasLeastOneDoctor(self):
        for day in self.days:
            if day.hasDoctor == False:
                return False
        return True


quantityOfPeriodsOfHolidays = int(input("Digite a quantidade k de períodos de férias: "))
totalMaximumDaysOfWork = int(input("Digite o parâmetro c, que representa o total dias de férias que um médico poderá trabalhar: "))

holidays = {}

#CADASTRAMENTO DOS FERIADOS

for i in range (quantityOfPeriodsOfHolidays):
    holidayName = input((f"Digite o nome do {i+1}° feriado: "))
    holidayDays = int(input(f"Digite a quantidade de dias do feriado {holidayName}: "))
    holidays[holidayName] = Holidays(holidayName)
    holidays[holidayName].insertDays(holidayDays)

print("---------------------------------")

#CADASTRAMENTO DE MÉDICOS E OS DIAS QUE ELES IRÃO TRABALHAR

while True:
    doctor = input("Digite o nome do médico que deseja adicionar ou 0 para sair: ")
    if doctor == "0":
        break
    else:
        totalDaysOfWork = 0
        while True:
            holiday = input("Digite o feriado que ele irá trabalhar ou 0 para voltar ao cadastro de médico: ")
            if holiday == "0":
                break
            else:
                days = (input(f"Digite qual dia do feriado que ele irá trabalhar(opções deste feriado - {holidays[holiday].getDays()}):")) 
                workDay = days
                if workDay not in holidays[holiday].getDays():
                    print("ERRO.")
                else:
                    totalDaysOfWork += 1
                    if totalDaysOfWork > totalMaximumDaysOfWork:
                        totalDaysOfWork -= 1
                        print(f"Este médico não pode trabalhar mais que {totalMaximumDaysOfWork} dias.")
                    elif holidays[holiday].checkIfDoctorIsAlreadyWorkingOnCurrentHoliday(doctor): 
                        print("Este médico já trabalha neste feriado. Considere que ele só pode trabalhar no máximo um dia de cada feriado, conforme regra 2.")
                    else:
                        holidays[holiday].insertDoctorsInWorkHolidayDays(workDay, doctor)
        

#VERIFICACAO SE HAVERÁ MÉDICOS PARA TODOS OS DIAS NOS FERIADOS OU NÃO

flag = 0

for holiday, holidayObj in holidays.items():
    if not holidayObj.checkIfHolidayHasLeastOneDoctor():
        flag = 1
        break

print("Não existe médico suficiente para todos os conjuntos de feriados") if flag == 1 else print("Existe pelo menos um médico de plantão em cada dia de cada feriado!")
        
