tsp_per_tbsp = 3
tsp_per_cup = 48 

def reduceMeasure(num, unit):
  unit = unit.lower()
  if unit == "teaspoon" or unit == "teaspoons":
    teaspoons = num 
  elif unit == "tablespoon" or unit =="tablespoons":
    teaspoons = num * tsp_per_tbsp
  elif unit == "cup" or unit == "cups":
    teaspoons = num * tsp_per_cup
  cups = teaspoons // tsp_per_cup
  teaspoons = teaspoons - cups * tsp_per_cup
  tablespoons = teaspoons // tsp_per_tbsp
  teaspoons = teaspoons - tablespoons * tsp_per_tbsp

  result = ""

  if cups > 0:
    result = result + str(cups) + " cup"
    if cups > 1:
      result += "s"
  if tablespoons > 0:
    if result != "":
      result = result + ", "
    result = result + str(tablespoons) + " tablespoon"
    if tablespoons > 1:
      result = result + "s"
  if teaspoons > 0:
    if result != "":
      result = result + ","
    result = result + str(teaspoons) + " teaspoon"
    if teaspoons > 1:
      result = result + "s"
  if result == "":
    result = "0 teaspoons"
  return result
def main():
  print("59 teaspoons is %s." % reduceMeasure(59, "teaspoons"))
main()
