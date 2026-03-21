print("Bem-vindo à calculadora de gorjetas!")
bill = float(input("Qual foi o valor total da conta? em R$: ")) # Coloque com "." o valor Ex: 300.00
tip = int(input("Qual porcentagem de gorjeta você gostaria de dar? 10 12 15 %: "))
people = int(input("Quantas pessoas dividirão a conta?: "))

tip_as_percent = tip / 100
total_tip_amout = bill * tip_as_percent
total_bill = bill + total_tip_amout

bill_per_person = total_bill/ people
final_amount = round(bill_per_person, 2)

print(f"Cada pessoa deverá pagar: R${final_amount}.")





