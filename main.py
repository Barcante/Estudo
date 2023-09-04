import calendar
from client_data import add_client, get_all_clients
from itertools import count

# Calculador de horários e pagamento
print('Bem vindo ao protótipo do gerenciador de turmas.')

obj = calendar.Calendar()

class Class:
    id_counter = count().__next__
    def __init__(self, instructor, capacity):
        self.id = self.id_counter()
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled_clients = []

class Schedule:
    def __init__(self, date, time, class_instance):
        self.date = date
        self.time = time
        self.class_instance = class_instance
        self.absence = []

class Client:
    def __init__(self, name):
        self.name = name
        # self.email = email
        self.schedule = []  # List of scheduled classes

class Instructor:
    def __init__(self, name, payment=0):
        self.name = name
        self.payment = payment
        self.schedule = []  # List of scheduled classes

# Check class availability before creating
def create_class(instructor):
    ...

# Check class availability before booking
def book_class(client, scheduled_class):
    if scheduled_class.class_instance.capacity > len(scheduled_class.class_instance.enrolled_clients):
        if not client_has_conflict(client, scheduled_class):
            scheduled_class.class_instance.enrolled_clients.append(client)
            client.schedule.append(scheduled_class)
            return True
    return False

# Check if client has a schedule conflict
def client_has_conflict(client, scheduled_class):
    for booked_class in client.schedule:
        if booked_class.date == scheduled_class.date and booked_class.time == scheduled_class.time:
            return True
    return False

# Cancel a booked class
def cancel_class_booking(client, scheduled_class):
    if client in scheduled_class.class_instance.enrolled_clients:
        scheduled_class.class_instance.enrolled_clients.remove(client)
        client.schedule.remove(scheduled_class)
        return True
    return False

def client_was_absent(client, scheduled_class):
    if client not in scheduled_class.absence:
        scheduled_class.absence.append(client)

# Criar turma de sábado às 9
andressa = Instructor('Andressa')

# add_client({'name': 'Leonor'})
# add_client({'name': 'Mafalda'})

alunos = {}

for student in get_all_clients():
    alunos[student['name']] = Client(student['name'])

turmas = {
    'sabado_09AM': Class(andressa.name, 2),
    'sabado_10AM': Class(andressa.name, 4),
    'sabado_11AM': Class(andressa.name, 2),
    'sabado_12AM': Class(andressa.name, 4),
    'terca_06PM': Class(andressa.name, 4),
    'terca_07PM': Class(andressa.name, 4),
    'terca_08PM': Class(andressa.name, 4),
    'quarta_06PM': Class(andressa.name, 4),
    'quarta_07PM': Class(andressa.name, 2),
    'quinta_11AM': Class(andressa.name, 4),
    'quinta_12AM': Class(andressa.name, 4),
    'quinta_03PM': Class(andressa.name, 2),
    'sexta_07PM': Class(andressa.name, 2),
    'sexta_08PM': Class(andressa.name, 4),
}

Agosto = {}

days = {
    0: 'segunda',
    1: 'terca',
    2: 'quarta',
    3: 'quinta',
    4: 'sexta',
    5: 'sabado',
    6: 'domingo',
}

hours = ['09AM','10AM','11AM','12AM','01PM','02PM','03PM','04PM','05PM','06PM','07PM','08PM']

for day in obj.itermonthdays2(2023,8):
    if day[0] > 0:
        Agosto[day[0]] = days[day[1]]

agenda = []

for day in Agosto:
    for hour in hours:
        turma = f'{Agosto[day]}_{hour}'
        if turmas.get(turma):
            agenda.append(Schedule(day, hour, turmas[turma]))

book_class(alunos['Luisa Menezes'], agenda[0])
book_class(alunos['Susana Oliveira'], agenda[0])
book_class(alunos['Manuela Paquete'], agenda[0])
book_class(alunos['Marina Ribeiro'], agenda[0])
book_class(alunos['Leonor Malheiros'], agenda[1])
book_class(alunos['Mafalda Amorin'], agenda[1])
book_class(alunos['Tania Costa'], agenda[1])
book_class(alunos['Fred Jacob'], agenda[1])
book_class(alunos['Maria Joao Lima'], agenda[2])
book_class(alunos['Maria Joao Moreira'], agenda[2])
book_class(alunos['Julieta Gama'], agenda[2])
book_class(alunos['Gabi Jardim'], agenda[2])
book_class(alunos['Isabel Lage'], agenda[3])
book_class(alunos['Sara Ferreira'], agenda[3])
book_class(alunos['Odete Almeida'], agenda[3])
book_class(alunos['Claudia Mendes'], agenda[4])
book_class(alunos['Rosa Gouveia'], agenda[5])
book_class(alunos['Maria Isilda Belo'], agenda[5])
book_class(alunos['Silas Grigoleto'], agenda[5])
book_class(alunos['Isabel Teixeira'], agenda[5])
book_class(alunos['Isabel Xavier'], agenda[6])
book_class(alunos['Analia Neiva'], agenda[6])
book_class(alunos['Eduarda Pereira'], agenda[6])
book_class(alunos['Luisa Carvalho'], agenda[7])
book_class(alunos['Claudia Mendes'], agenda[8])
book_class(alunos['Julieta Gama'], agenda[9])
book_class(alunos['Rafael Chacon'], agenda[9])
book_class(alunos['Francisco Aires'], agenda[9])
book_class(alunos['Debora Levi'], agenda[9])
book_class(alunos['Filipa Coelho'], agenda[10])
book_class(alunos['Jorge Coelho'], agenda[10])
book_class(alunos['Pedro Machado'], agenda[11])
book_class(alunos['Gabi Jardim'], agenda[11])
book_class(alunos['Marcos Silva'], agenda[11])
book_class(alunos['Joao Cunha'], agenda[11])
book_class(alunos['Pedro Campos Costa'], agenda[12])
book_class(alunos['Leonor Malheiros'], agenda[13])

client_was_absent(alunos['Leonor Malheiros'], agenda[1])

total_mes = 0

for s in agenda:
    earnings = 15
    if not s.class_instance.enrolled_clients:
        earnings = 0
    elif s.class_instance.capacity <= 2 and len(s.absence) < 2:
        earnings = 16
    elif len(s.class_instance.enrolled_clients) - len(s.absence) == s.class_instance.capacity:
        earnings = 18

    total_mes += earnings

    print(s.date, Agosto[s.date], s.time, f'€ {earnings},00')
    [print('\t', client.name if client not in s.absence else f'f|{client.name}') for client in s.class_instance.enrolled_clients]

print(f'\n\n\nTotal do mes: € {total_mes},00')