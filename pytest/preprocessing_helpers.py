import re

def convert_to_int(number):
  if re.search("^(0|[1-9][0-9]{0,2}(,[0-9]{3})*)$", number) is None:
    return None
  number=number.replace(",", "")
  return int(number)

def convert_to_int_alternative(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    # Fill in with a ValueError
    except ValueError:
        return None

# print(convert_to_int("2,081"))
def row_to_list(values):
  
  values = values.replace("\n", "")
  arr = values.split("\t")
  if len(arr)!=2:
    return None
  for x in arr:
    if re.search("^(0|[1-9][0-9]{0,2}(,[0-9]{3})*)(\\.[0-9]+)?$", x) is None:
      return None
  return arr

# print(row_to_list("1,059\t186,606\n"))