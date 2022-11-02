import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import smtplib
def sendEmail(address):
	print(Fore.YELLOW + "\nWelcome to Mailster!")
	print("--------------------------------------------------------------")
	sender = "hackathondell2022@gmail.com"
	password = "swarbabdxxodvlpn"
	# reciever = input(str("\n\nReciever: "))
	reciever =address
	message = """Subject: Rewards\n
	Congratulations DELL
 	You have won a laptop"""

	if not reciever:
		print(Fore.GREEN + "\nReciever's Email is required!")
	if not message:
		print(Fore.GREEN + "\nMessage cannot be left empty!")
	else:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender, password)
		print(Fore.GREEN + "\nAccount successfully verified!")
		server.sendmail(sender, reciever, message)
		print(Fore.YELLOW + "\nYour email has been successfully sent to", reciever)
		server.quit()