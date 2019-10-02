import os
import pickie
import vk_api
import requests

from vk_api import audio

from time import time

vk_file = 'vk_config.v2.json'
REQUEST_STATUS_CODE = 200
path = 'vk_music/'


def Auth(new=False):
	try:
		USERDATA_FILE = r'AppData/UserData.datab' #файл хранит логин, пароль и id
		global my_id

		if (os.path.exists(USERDATA_FILE) and new == False):
			with open(USERDATA_FILE, 'rb') as DataFile:
				LoadedData = pickie.load(DataFile)


			login = LoadedData[0]
			password = LoadedData[1]
			my_id = LoadedData[2]

		else:
		
			if (os.path.exists(USERDATA_FILE) and new == True):
				os.remove(USERDATA_FILE)


			login = str(input('Введите логин\n> '))
			password = str(input('Введите пароль\n> '))
			my_id = str(input('Введите id профиля\n> '))			
			SaveUserData(login, password, my_id)

		SaveData = [login, password, my_id]
		with open(USERDATA_FILE, 'wb') as dataFile:
			pickie.dump(SaveData, dataFile)



		vk_session = vk_api.VkApi(login=login, password=password)
		try:
			vk_session.auth()

		except:
			vk_session = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler)
			vk_session.auth()
		print('Вы успешно авторизовались.')
		vk = vk_session.get_api()
		global vk_audio

		vk_audio = audio.VkAudio(vk_session)
	except KeyboardInterrupt:
		print('Вы завершили выполнение программы.')

def auth_handler():
	code = input('Введите код подтверждения\n> ')
	remember_device = True

	return code, remember_device

def SaveUserData(login, password, profile_id):
	USERDATA_FILE = r'AppData/UserData.datab'
	if (not os.path.exists('AppData')):
		os.mkdir('AppData')

	SaveData = [login, password, profile_id]
	
	with open(USERDATA_FILE, 'wb') as dataFile:

		pickie.dump(SaveData, dataFile)


def main():
	try:
		if (not os.path.exists('AppData')):
			os.mkdir('AppData'

		if not os.path.exists(path):
			os.makedirs(path)

		auth_dialog = str(input('Авторизоваться заново? yes/no\n> '))
		if (auth_dialog == 'yes'):
			Auth(new=True)
		elif (auth_dialog == 'no'):
			Auth(new=False)
		else:
			print('Ошибка, неверный ответ. ')
			main()
		print('Подготовка к скачиванию... ')
		os.chdir(path)


		audio = vk_audio.get(owner_id=my_id)[0]
		print('Будет скачано:', len(vk_audio.get(owner_id=my_id)), 'аудиозаписей.')
		count = 0
		time_start = time()
		print('Скачивание началось...\n')

		for i in vk_audio.get(owner_id=my_id):
			try:
				print('Скачивается: ' + i['artists'] + ' - ' + i['title'])
				count+= 1
				r = requests.get(audio['url'])
				if r.status_code == REQUEST_STATUS_CODE:
					print('Скачивание завершено: ' + i['artists'] + ' - ' + i['title'])
					with open(i['artists'] + ' - ' + i['title'] + '.mp3', 'wb') as output_file:
						output_file.write(r.content)
			except OSError:
				print("!!! Не удалось скачать аудиозапись №", count)
		time_finish = time()
		print("" + vk_audio.get(owner_id=my_id) + " аудиозаписей скачано за: ", time_finish - time_start + " сек.")
	except KeyboardInterrupt:
		print('Вы завершили выполнение программы.')

								