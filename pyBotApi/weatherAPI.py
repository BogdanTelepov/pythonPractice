import pyowm

owm = pyowm.OWM('e1f5c8dd2963f81002ac13dfde531fc2', language='ru')
place = input('Введите страну/город: ')
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]
print('Сейчас в городе ' + place + " - " + w.get_detailed_status())
print('Температура: ' + str(temp))
