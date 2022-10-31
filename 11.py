# # rle-decode.py def rle_decode(data): decode = '' count = '' for char in data: # If the character is numerical... if char.isdigit(): # ...append it to our count count += char else: # Otherwise we've seen a non-numerical # character and need to expand it for # the decoding decode += char * int(count) count = '' return decode
# def rle_decode(data):
# decode: str = ''
# count: str = ''
# for char in data:
#     if char.isdigit():
#         count += char
#     else:
#         decode += char * int(count)
#         count = ''
# print(count)
# print(decode)

# def rle_decode(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode
# print(rle_decode('2a3d4e5t'))
#
#
def rle_count(data):
    count = 1
    decode = str("")
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            decode += str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data)-2] != data[-1]):
        decode += str(count) + data[-1]
    return decode


print(rle_count('aadddeeeettttt'))

# def rle_coding (txt):
#     count  =  1
#     res = ""
#     for i in range (len(txt) -1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = str(count) + txt[i]
#             count = 1
#     if  1 > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = str(count) + txt[-1]
#     return res
#
# def rle_decoding (txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res
#
#
# s = ['aaadddfffffff']
# print(f"Текст после кодировки: {rle_coding(s)}")
# print(f"Текст после дешифровки: {rle_decoding(rle_coding(s))}")
