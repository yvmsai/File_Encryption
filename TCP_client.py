import socket
import public_key_algo
import private_key_algo

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
'''def Socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        #pub_k, prv_k = public_key_algo.rsa_key_val_gen(100, 250)
        data = "Hello"
        s.sendall(bin(data[0]))
        data = s.recv(1024)
        print(f"Received {data!r}")'''


# The main block
if __name__ == '__main__':
    nextstr = ''
    # creating a socket to communicate with server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establishing connection between server and client
    s.connect((HOST, PORT))
    '''pub_k, prv_k = public_key_algo.rsa_key_val_gen(100, 250)
        print(pub_k, prv_k)
        send_data = str(pub_k)
        s.send(send_data.encode())
        data = s.recv(1024)
        print(f"Received {data!r}")
        s.close()'''
    # The main loop
    while True:
        # Options displayed to end-user
        print('Enter one of the following:')
        print('  c - for creating and saving new file')
        print('  r - for reading the data from the given file')
        print('  u  - for adding the data in the given file')
        print('  d  - for deleting the existing file')
        print('  x  - for exit')
        choice = input('? ').strip().lower()
        # No option chosen, it closes the connection
        if len(choice) == 0:
            choice = 'x'
        # need to choose only above-mentioned options other than that throws error
        if (choice[0] != 'c' and choice[0] != 'r' and
                choice[0] != 'u' and choice[0] != 'd' and
                choice[0] != 'x'):
            print('Invalid choice\n')
        # Option for creating and updating the file
        if choice == 'c':
            print("Client : Request to create and update the file")
            file_name = str(input("Enter the filename to be created and data to enter and enter end at the end of data\n")).lower()
            split_data = file_name.split()
            encrypt_fn, orig_fn = private_key_algo.read_data(split_data[0])
            split_data[0] = encrypt_fn
            file = 'write '
            for i in range(len(split_data)):
                file += split_data[i] + " "
            send_data = file
            s.send(send_data.encode())
            data = s.recv(1024).decode()
            print(f"Client Received : {data!r}")
        # option for reading content of a file
        if choice == 'r':
            print("CLient : Request to fetch the data")
            file_name = str(input("Enter the filename, and data to be read\n")).lower()
            encrypt ,original = private_key_algo.read_data(file_name)
            sent_data = 'read ' + encrypt + ' '
            pub_k, prv_k = public_key_algo.rsa_key_val_gen(100, 250)
            sent_data += str(pub_k[0]) + ' ' + str(pub_k[1])
            s.send(sent_data.encode())
            data = s.recv(1024).decode()
            print("Client Received : ", data)
            rec_1_text = []
            rec_text = ''
            input_chara = public_key_algo.func_strList_converter(data)
            input_chara_inte = public_key_algo.func_StrAscii_Converter(input_chara)
            for each in input_chara_inte:
                cipher_tempor_text = public_key_algo.find_encrypt_val(each, prv_k)
                rec_1_text.append(cipher_tempor_text)
            cipher_tex_list = public_key_algo.func_StrAscii_Converter(rec_1_text)
            for each in range(len(cipher_tex_list)):
                rec_text += cipher_tex_list[each]
            print("Readable text : ", rec_text)
        # option for updating the file
        if choice == 'u':
            print("Client : Request to update the file")
            file_name = str(input("Enter the filename,  and data to be updated and enter end at the end of data\n")).lower()
            split_data = file_name.split()
            encrypt_fn, orig_fn = private_key_algo.read_data(split_data[0])
            split_data[0] = encrypt_fn
            file = 'update '
            for i in range(len(split_data)):
                file += split_data[i] + " "
            send_data = file
            s.send(send_data.encode())
            data = s.recv(1024).decode()
            print(f"Client Received {data!r}")
        # option for deleting the file
        if choice == 'd':
            print("Client : request to delete the file")
            file_name = str(input("Enter the filename to be deleted\n")).lower()
            split_data = file_name.split()
            encrypt_fn, orig_fn = private_key_algo.read_data(split_data[0])
            file = 'delete ' + encrypt_fn
            s.send(file.encode())
            data = s.recv(1024).decode()
            print(f"Client Received {data!r}")
        # option to exit
        if choice == 'x':
            print("Client sent: Close")
            s.send('exit'.encode())
            data = s.recv(1024).decode()
            print(f"Client Received: {data!r}")
            s.close()
            break


