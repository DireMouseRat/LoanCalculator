import string
print(string.Template("Dear $username! It was really nice to meet you. "
                      "Hopefully, you have a nice day! "
                      "See you soon, $username!")
      .substitute(username=input()))
