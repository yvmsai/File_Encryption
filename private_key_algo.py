import numpy as np


# converts given string to list of string
def StringListConverter(input_data):
    if type(input_data) == str:
        return_val = []
        for each_char in input_data:
            return_val.append(each_char)
    elif type(input_data) == list:
        return_val = ''
        for each_item in input_data:
            return_val = return_val + each_item
    return return_val


def AsciiConverter(input_data):
    return_val = []
    if input_data and type(input_data[0]) == str:
        for each_char in input_data:
            return_val.append(ord(each_char))
    elif input_data and type(input_data[0] == int):
        for each_num in input_data:
            return_val.append(chr(each_num))

    return return_val


# Method to convert Ascii values to binary values
def AsciiToBinaryConverter(input_data):
    return_val = []
    binary_flag = ''
    # functions appropriate based on input data type whether it is list or string
    if input_data and type(input_data[0]) == int and input_data[0] < 500:
        binary_flag = False
    elif input_data and type(input_data[0] == str):
        binary_flag = True

    if input_data and type(input_data) == list:
        number_flag = True
        for each_num in input_data:
            if type(each_num) != int:
                if type(each_num) != str:
                    number_flag = False
        if number_flag:
            if binary_flag:
                for each_binary in input_data:
                    return_val.append(int(str(each_binary), 2))
            elif not binary_flag:
                for each_ascii in input_data:
                    return_val.append(bin(each_ascii)[2:])
            return return_val


def encoder_decoder_function(generated_str, conversion_key):
    if len(generated_str) < 8:
        for i in range(8 - (len(generated_str))):
            generated_str = '0' + generated_str

    first_vals = str(generated_str)[:4]
    remaining_vals = str(generated_str)[4:]

    converted_key = int(conversion_key, 2)
    first_vals_int = int(first_vals, 2)
    remaining_vals_int = int(remaining_vals, 2)
    generated_val = 2 * (remaining_vals_int ** converted_key) % 16

    final_val_int = first_vals_int ^ generated_val
    binary_value = np.binary_repr(final_val_int, width=4)

    final_first_value = remaining_vals
    final_remaining_value = binary_value
    final_binary_value = final_first_value + final_remaining_value
    return final_binary_value


# Actual Feistel Cipher logic
def cipher_feistel_function(user_input, user_key):
    binary_num_list = []
    for binary_data in user_key:
        binary_num_list.append(np.binary_repr(binary_data, width=4))

    str_list = StringListConverter(user_input)
    str_int_data = AsciiConverter(str_list)
    binary_int_data = AsciiToBinaryConverter(str_int_data)

    cip_binary_list = []
    for binary_data in binary_int_data:
        current_cip_data = binary_data

        for binary_num in binary_num_list:
            current_cip_data = encoder_decoder_function(current_cip_data, binary_num)
        swapped_data = current_cip_data[4:] + current_cip_data[:4]
        cip_binary_list.append(swapped_data)

    cip_num_val = AsciiToBinaryConverter(cip_binary_list)
    cip_str_val = AsciiConverter(cip_num_val)
    final_cip_str = StringListConverter(cip_str_val)

    return final_cip_str


# reading the input file or text
def read_data(input_file):
    print(input_file)
    key = np.arange(16)
    key_reverse = np.flip(key)
    message_1 = input_file
    cipher_1 = cipher_feistel_function(message_1, key)
    recovered_message_1 = cipher_feistel_function(cipher_1, key_reverse)
    return cipher_1, recovered_message_1
