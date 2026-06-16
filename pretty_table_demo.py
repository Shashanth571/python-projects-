from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon",["pikachu","charmander","squirtle"])
table.add_column("Type",["electric","fire","water"])
print(table)
table.align = "l"
print(table)