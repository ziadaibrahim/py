from oop import Person, Employee, Car, Office  
fiat = Car("Fiat128", fuelRate=50, velocity=100)

samy = Employee(
    name="Samy",
    money=500,
    mood="",
    healthRate=0,
    emp_id=1,
    car=fiat,
    email="samy@iti.gov",
    salary=3000,
    distanceToWork=20
)

samy.sleep(6)
print(f"{samy.name}'s mood after sleep: {samy.mood}")

samy.eat(2)
print(f"{samy.name}'s health rate: {samy.healthRate}%")

samy.buy(2)
print(f"{samy.name}'s money after shopping: {samy.money} LE")

samy.drive()

samy.refuel()
print(f"Fuel after refuel: {samy.car.fuelRate}")

iti_office = Office("ITI Smart Village")

iti_office.hire(samy)
print(f"Total employees: {Office.employeesNum}")

samy.car.velocity = 100  
iti_office.check_lateness(empId=1, moveHour=7)  

print(f"{samy.name}'s salary after checking lateness: {samy.salary} LE")

