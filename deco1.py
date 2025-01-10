def dev_dec(func):
  def inner(a,b):
    if a<b:
      a,b=b,a
    return func(a,b)
  return inner
@dev_dec
def div(a,b):
  #print(a/b)
  if a<b:
    a,b=b,a
  return a/b
#test cases
div(2,4)