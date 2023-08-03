#!/usr/bin/env python3


# step 1, Decode Vishal's message

message = "xuo Jxuhu! jxyi Yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt Cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
key = 10


def ceasar_mess(message, key, mode):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_message = ""
    for i, symbol in enumerate(message):
        if symbol.isalpha():
            index = alpha.find(symbol)
            if mode == "encrypt":
                final_message += alpha[(index - key) % 26]
            elif mode == "decrypt":
                final_message += alpha[(index + key) % 26]
        else:
            final_message += symbol

    return final_message


final_version = ceasar_mess(message, key=10, mode="decrypt")
print(final_version)


def cap_sentences(string):
    words = string.split()
    # Loop over the words and capitalize the first letter of each word that follows a delimiter
    delimiters_lst = ["!", ".", "?"]
    new_words = []
    for i in range(len(words)):
        # Capitalize the first word
        if i == 0:
            new_words.append(words[i].capitalize())
        # Capitalize the first letter of each word that follows a delimiter
        else:
            for delim in delimiters_lst:
                if words[i - 1].endswith(delim):
                    new_words.append(words[i].capitalize())
                    break
            else:
                new_words.append(words[i])
    # Join the words back into a single string
    new_string = " ".join(new_words)
    return new_string


print("---------")
version_1 = cap_sentences(final_version)
print(version_1)

# step 2. Encrypt your message to Vishal.
my_message = "Hello, Vishal. What a nice suprice!"

encrypted_my_message = ceasar_mess(my_message, key=15, mode="encrypt")
print("------")
print(encrypted_my_message)


# step 3, make functions for decoding and coding


def decoder(message, offset):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_message = ""
    for i, symbol in enumerate(message):
        if symbol.isalpha():
            find_index = alpha.find(symbol)
            final_message += alpha[(find_index + offset) % 26]
        else:
            final_message += symbol
    return final_message


def coder(message, offset):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_message = ""
    for i, symbol in enumerate(message):
        if symbol.isalpha():
            find_index = alpha.find(symbol)
            final_message += alpha[(find_index - offset) % 26]
        else:
            final_message += symbol
    return final_message


first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = (
    "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
)
decoded_first = decoder(first_message, offset=10)
decoded_second = decoder(second_message, offset=14)
print(decoded_first)
print("-----------------------------------------------\n", decoded_second)

# step 4, solving a ceasar cipher without knowing the shift value

message_1 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."


def brute_force(message, offset=50):
    "Should print possible text for the provided cipher text."
    for shift_value in range(1, offset):
        possible_text = decoder(message, shift_value)
        print(f"Shift value:  {shift_value} - Plain text: {possible_text}")


brute_force(message_1)
print("-----------------")
# step 5 the vigenere cypher

vigenere_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"


def decoder_vigenere(message, keyword):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword_index = 0
    keyword_final = ""
    for i in range(0, len(message)):
        if not message[i].isalpha():
            keyword_final += message[i]
        else:
            keyword_final += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
    decoded_message = ""
    for i in range(0, len(message)):
        if message[i].isalpha():
            index = alpha.find(message[i]) - alpha.find(keyword_final[i])
            decoded_message += alpha[index % 26]
        else:
            decoded_message += message[i]
    return decoded_message


vigenere_message_decoded = decoder_vigenere(vigenere_message, keyword="friends")
print(cap_sentences(vigenere_message_decoded))
print("-------------")


def coder_vigenere(message, keyword):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword_index = 0
    keyword_final = ""
    for i in range(0, len(message)):
        if not message[i].isalpha():
            keyword_final += message[i]
        else:
            keyword_final += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
    coded_message = ""
    for i in range(0, len(message)):
        if message[i].isalpha():
            index = alpha.find(message[i]) + alpha.find(keyword_final[i])
            coded_message += alpha[index % 26]
        else:
            coded_message += message[i]
    return coded_message


message_v = "it is quite hard to understand."
keyword_v = "nice"
vigenere_message_coder = coder_vigenere(message_v, keyword_v)
print(cap_sentences(vigenere_message_coder))
