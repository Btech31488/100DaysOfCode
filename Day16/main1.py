# from turtle import Turtle, Screen
# # import another_module

# # print(another_module.another_var)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.fd(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
