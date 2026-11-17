import socket
import time

HOST = "0.0.0.0"
PORT = 5000

RESPONSE_DELAY = 0

def rec_message(connection):
	data = b""
	while b"\n" not in data:
		chunk = connection.recv(1024)
		if not chunk:
			return None
		data += chunk
		if len(data) > 1024:
			raise ValueERROR("message is too long")
	return data.split(b"\n", 1)[0].decode("utf-8")
