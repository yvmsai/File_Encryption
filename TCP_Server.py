import socket
import private_key_algo
import public_key_algo
import os

HOST = "127.0.0.1"  # localhost address
PORT = 65432  # Port to listen

# creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding the socket with port and address
s.bind((HOST, PORT))
# listening for any client connections on port
s.listen()
# connection accept and address of the client
conn, addr = s.accept()
with conn:
    print(f"Connected by {addr}")
    while True:
        # loop for handling each option entered by client or end-user
        print("Server Waiting for client Input.........\n")
        data = conn.recv(1024)
        if not data:
            break
        input_data = data.decode()
        input_data_split = input_data.lower().split()
        # handing for writing the content
        if input_data_split[0] == 'write':
            file_name = input_data_split[1]
            file1 = open(file_name, "w")
            i = 2
            while input_data_split[i] != 'end':
                file1.write(input_data_split[i] + " ")
                i = i +1
            print("Server sent : File created and data Saved Successfully\n")
            conn.sendall("Data Saved Successfully!".encode())
        # handing for read the content
        elif input_data_split[0] == 'read':
            print("Server Recived : To read data from file")
            pub_key = []
            pub_key.append(int(input_data_split[2]))
            pub_key.append(int(input_data_split[3]))
            file_name = input_data_split[1]
            if os.path.exists(file_name):
                file1 = open(file_name, "r")
                cip_1_text = []
                cipher_text = ''
                for i in file1.readlines():
                    input_chara = public_key_algo.func_strList_converter(i)
                    input_chara_inte = public_key_algo.func_StrAscii_Converter(input_chara)
                    for each in input_chara_inte:
                        cipher_tempor_text = public_key_algo.find_encrypt_val(each, pub_key)
                        cip_1_text.append(cipher_tempor_text)
                cipher_tex_list = public_key_algo.func_StrAscii_Converter(cip_1_text)
                for each in range(len(cipher_tex_list)):
                    cipher_text += cipher_tex_list[each]
                print("Server Sent : ", cipher_text)
                conn.sendall(cipher_text.encode())
            else:
                conn.sendall("File not exist".encode())
        # Handling for updating the file
        elif input_data_split[0] == 'update':
            print("Server Received : To update file")
            file_name = input_data_split[1]
            if os.path.exists(file_name):
                file1 = open(file_name, "a")
                i = 2
                while input_data_split[i] != 'end':
                    file1.write(input_data_split[i] + " ")
                    i = i + 1
                print("Server Sent : Data updated Successfully\n")
                conn.sendall("Data updated Successfully!".encode())
            else:
                conn.sendall("File not exist".encode())
        # Handling for deleting the file
        elif input_data_split[0] == 'delete':
            print("Server Received : To delete File")
            file_name = input_data_split[1]
            if os.path.exists(file_name):
                os.remove(file_name)
                print("Server Sent: File deleted Successfully\n")
                conn.sendall("File deleted Successfully!".encode())
            else:
                conn.sendall("File not exist".encode())
        # Handing for client exit or closes the connection
        elif input_data_split[0] == 'exit':
            print("Server Received: connection close\n")
            print("Server Sent : closed\n")
            conn.sendall("connection closed".encode())
            conn.close()
            break




