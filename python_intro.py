print('Hello, Django Girls!')
if 3>2:
    print('To działa!')
if 4<6:
    print('ok!!!')
if 5>2:
    print('5 jest jednak większe od 2')
else:
    print('5 nie jest większe od 2')
name = "Kinga"
if name == "Zuza":
    print('Hej Zuza')
elif name == 'Kinga':
    print('Hej Kinga!')
else:
    print('Hej anonimie!')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
volume = 20
if volume < 10:
    print("Cześć")
elif volume <= 20:
    print("cośtamcośtam")
else:
    print("abc")
def hi():
    print('Hej!')
    print('Jak się masz?')
hi()
def hi(imie):
    if imie == 'Kinga':
        print('Hej Kinga!')
    elif imie == 'Zuza':
        print('Hej Zuza!')
    else:
        print('Hello stranger!')
hi("Ala")
def hi(imie):
    print('Hej ' + imie + '!')
hi("Rachel")
dziewczyny = ['Rachel', 'Monika', 'Ala', 'Kasia', 'Kinga']
for imie in dziewczyny:
    hi(imie)
    print('Kolejna dziewczyna')
for i in range (1, 6):
    print('i=' +str(i))
