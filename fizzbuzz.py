import sys
try:
  if len(sys.argv) > 1:
    n = int(sys.argv[1])

  else:
    n = int(raw_input("Enter a number: "))


  print "Fizzbuzz is counting up to {}".format(str(n))

  for number in range(1, n+1):
    if number % 3 == 0 and number % 5 == 0:
      print "fizzbuzz"
    elif number % 3 == 0:
      print "fizz"
    elif number % 5 == 0:
      print "buzz"
    else:
      print str(number)
      
except:
  print "Please enter a number greater than 0."

