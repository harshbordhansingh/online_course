# u = ' '
# while True:
#     user = input("Say something: ")
#     u += user.title() + " "
#     if user == "\end":
#         break
#     else:
#         continue
#
# c = u[:-6]
# print(c)


def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how", "when", "why", "what", "are", "do", "does")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))