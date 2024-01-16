visina = float(input("Unesite vašu visinu u metrima npr. 1.72 / 1.86\n"))

težina = float(input("Unesite vašu težinu u kilogramima npr. 72 / 86\n"))

bmi =  težina / (visina ** 2)


if bmi < 18.5 :
  print(f"Vaš BMI je {bmi} i Vi ste neuhranjeni, potražite pomoć")
elif 18.5 <= bmi < 25 :
  print(f"Vaš BMI je {bmi} i Vi ste idealne težine, svaka čast")
elif 25 <= bmi < 30 :
  print(f"Vaš BMI je {bmi} i Vi ste blago gojazni, malo vam fali ali na vama je da odlučite ka kojoj granici")
elif 30 <= bmi < 35 :
  print(f"Vaš BMI je {bmi} i Vi ste debeli")
else :
  print(f"Vaš BMI je {bmi} i Vi ste klinički gojazni, potražite pomoć")