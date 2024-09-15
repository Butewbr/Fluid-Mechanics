fobos_div = float(input("1 F é o diâmetro de Fobos dividido por? "))
# fobos_div = 17600.0

deimos_div = float(input("1 D é o uma volta dividido por? "))

# deimos_div = 5.0

fobos = 22000.0/fobos_div

print("1 fobos = %.4f m" %(fobos))

deimos = 108000.0/deimos_div

print("1 deimos = %.4f s" %(deimos))

ares = 44.01

print("1 ares = %.4f g" %(ares))

olimpo = (44.01/1000)*3.721

print("1 olimpo = %.4f N" %(olimpo))

curiosity = olimpo/(fobos*fobos)

print("1 curiosity = %.4f Pa" %(curiosity))

viscosidade = float(input("Viscosidade da água (vem em 10^{-3} no site) (você pode conseguir por https://www.omnicalculator.com/pt/fisica/calculadora-viscosidade-da-agua )? "))
# viscosidade = 0.453

viscosidade_marte = (viscosidade)*1000000/(curiosity*deimos)

viscosidade_marte = viscosidade_marte

print("Respostas letra a: %.4f x 10^{-3} N.s/m² e %.4f nC.D" %(viscosidade, viscosidade_marte))

letrab = float(input("b) Quantos F é para calcular? "))
# letrab = 5

letrab_answer = letrab*fobos

print("Resposta letra b: %.4f m" %(letrab_answer))

letrac = float(input("c) Quantos D é para calcular? "))
# letrac = 7

letrac_answer = letrac*deimos/60

print("Resposta letra c: %.4f minutos" %(letrac_answer))

letrad = float(input("d) Quantos A é para calcular? "))
# letrad = 8

letrad_answer = letrad*ares/1000

print("Resposta letra d: %.4f kg" %(letrad_answer))

letrae1 = float(input("e) Quantos m/s²? "))
# letrae1 = 8

letrae2 = float(input("e) Quantos kg? "))
# letrae2 = 65

letrae_answer1 = letrae1*letrae2

letrae_answer2 = letrae_answer1/olimpo

print("Respostas letra e: %.4f N e %.4f O" %(letrae_answer1, letrae_answer2))

letraf1 = float(input("f) Qual é a área? "))
# letraf1 = 0.8

letraf2 = float(input("f) Qual é o peso? "))
# letraf2 = 71

pressao_pa = letraf2*3.721/letraf1

letraf_answer = pressao_pa/(curiosity*1000)

print("Respostas letra f: %.4f kC e %.4f kg" %(letraf_answer, letraf2))