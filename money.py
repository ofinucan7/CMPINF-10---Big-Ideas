hrsWk = input(prompt="How many hours did you work?")
hrlyWg = input(prompt="What is your hourly wage?")
tax = input(prompt="What tax percent do you pay?")
gross = int(hrsWk)*int(hrlyWg)
taxPct = int(tax)/100
netPay = int(gross) - (int(hrsWk)*int(hrlyWg)*float(taxPct))
print("Your gross pay is: $", gross)
print("Your net pay is: $", netPay)
