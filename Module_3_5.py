def gmd(number):
   str_number = str(number)
   first = int(str_number[0])
   if len(str_number) == 1:
       return first
   else:
       return first * gmd(int(str_number[1:]))

result = gmd(90802)
print(result)
