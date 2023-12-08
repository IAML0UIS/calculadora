def calculadora_basica(a,b,operation):

  if (a.isnumeric() & b.isnumeric()):
    a=int(a)
    b=int(b)
    if operation == "suma":
      result = a + b
    elif operation == "resta":
      result = a - b
    elif operation == "division":
      result = a / b
    elif operation == "multiplicacion":
      result = a * b
    else:
      result = "solo se acepta: suma, resta, division, multiplicacion"
    
  else:
    result = "Porfavor Introduce Un Valor calculable "
    

  return result