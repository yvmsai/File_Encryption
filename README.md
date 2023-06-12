# File_Encryption

Description:

Now a days, the usage of internet and social networking applications are very high. At the same time, securing of data is difficult on data exchanged between client and server or sender and receiver using any files, texts etc over an insecure network. So, in this paper, we have worked on how to encrypt a file content and transfer over an unsecured network between two devices. The encryption is done at server and receiver, at server end the content of the file is encrypted and receiver side the file content is decrypted and displayed as user readable format and the filename is also encrypted in receiver end and passed over a network using Transmission Control Protocol (TCP) socket communication and stored at server file system. To encrypt the text in files, we have used public and private key encryption algorithms. They are Rivest, Shamir, Adelman (RSA) algorithm is used to encrypt the file content and (Feistel Cipher) Data Encryption Standard (DES) is used to encrypt the file name.![image](https://github.com/yvmsai/File_Encryption/assets/25640559/97275669-f58b-413a-9012-281c28488806)


Steps to execute the code:
1) First need to open two terminal sessions, one for client and one for server.
2) IN next step, Server need to run in one terminal by using below command in specified
path.
> python3 TCP_Server.py
3) Next, in another terminal, need to run client terminal by using command in specified
path,
>python3 TCP_client.py
4) Before running Client, need to ensure Server is up and running. Once server is up and
running, execute client.
5) Once client is executed, ensure socket is established with the client IP address displayed
at server terminal.
6) Once socket is established and tried to use the terminal interface and following the
instructions provided at client side and choose whatever operation you want to
perform.
7) If you want to update directly in initial step, need to sure that the file is available or not,
if file is not available then it throws file not found.
These are the execution steps for the provided project implementation code.
