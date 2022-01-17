def convert_to_int(number):
  number = number.replace(",", "")
  return int(number)

# print(convert_to_int("2,081"))
def row_to_list(values):
  values = values.replace(",", ".")
  values = values.replace("\n", "")
  arr = values.split("\t")
  if len(arr)!=2:
    return None
  for x in arr:
    if is_number(x)==False:
      return None
  return arr

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


print(row_to_list("3\t34,5\n"))