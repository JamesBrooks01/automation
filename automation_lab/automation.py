import re

def get_phone_numbers(document):
  try:
    file = open(document)
    full_doc = file.read()
  finally:
    file.close()

  phone_number_regex = "((\+\d-)?\(?\d{3}\)?(-|\.|x)?\d{3}(-|\.|x)?\d{4}(-|\.|x)?(\d+(-|\.|x)?)?\d+)|(\d{10,})"
  grab_phone_format = "(\(?\d{3}\)?(-|\.|x)?\d{3}(-|\.|x)?\d{4})|(\d{10,})"

  phone_numbers = re.findall(phone_number_regex, full_doc)
  phone_list = []
  for string in phone_numbers:
    if string[0] == "":
      phone_list.append(string[-1])
    else:
      phone_list.append(string[0])

  format_list = []
  for number in phone_list:
    formatted_number = re.findall(grab_phone_format, number)
    format_list.append(formatted_number[0][0])

  finished_set = set()
  for number in format_list:
    if "." in number:
      period_replaced = re.sub("\.+","-",number)
      finished_set.add(period_replaced)
    elif "-" in number:
      closing_bracket = re.sub("\)","-", number)
      opening_bracket = re.sub('\(', '', closing_bracket)
      finished_set.add(opening_bracket)
    else:
      split_number = list(number)
      split_number.insert(3,"-")
      split_number.insert(7,"-")
      joined_num = ''.join(split_number)
      finished_set.add(joined_num)
  try:
    new_file = open("phone_numbers.txt", "w")
    for number in sorted(finished_set):
      new_file.write(number + "\n")
  finally:
    new_file.close()

def get_emails(document):
  try:
    file = open(document)
    full_doc = file.read()
  finally:
    file.close()

  email_regex = "[a-zA-Z0-9]+.?[a-zA-Z0-9]+@[\S]+\.[a-z]{3}"

  emails = re.findall(email_regex, full_doc)
  email_set = set()
  for email in emails:
    email_set.add(email)

  try:
    new_file = open("emails.txt", "w")
    for number in sorted(email_set):
      new_file.write(number + "\n")
  finally:
    new_file.close()


document = "potential-contacts.txt"
get_phone_numbers(document)
get_emails(document)