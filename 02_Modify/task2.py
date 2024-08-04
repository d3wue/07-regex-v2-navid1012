import re

reg = re.compile("(Prof\. |Dr\. )*([A-Z][a-z]+) ([A-Z\.a-z]*) ?([A-Z][a-z]+)(, (PhD|MSc|Duke of Manchester|KG|KT|PC|ADC))*")

#meine_Übung: reg = re.compile("(Prof\. |Dr\. )*([A-Z][a-z]+) ([A-Z\.])*([A-Z][a-z]+)?( )?([A-Z][a-z]+)(, (PhD|MSc|Duke of Manchester|KG|KT|PC|ADC))*")




m = reg.match("Uwe Meier")
print(m)
m = reg.match("Prof. Dr. Chris C Schmidt")
print(m)
m = reg.match("Hanna J Gruber, PhD")
print(m)
m = reg.match("Hanna J. Gruber, PhD")
print(m)
m = reg.match("Hanna Jana Gruber, PhD, MSc")
print(m)
m = reg.match("Dr. Uwe Meier, MSc")
print(m)
m = reg.match("Dr. Alfred Nobel, PhD, PhD, PhD, MSc")
print(m)
m = reg.match("Dr. Dr. Dr. Theodore Hesburgh, PhD, PhD, PhD, MSc")
print(m)
m = reg.match("Albert KD Klein, PhD, PhD, PhD, MSc")
print(m)
m = reg.match("Prince William, Duke of Manchester, KG, KT, PC, ADC")
print(m)
