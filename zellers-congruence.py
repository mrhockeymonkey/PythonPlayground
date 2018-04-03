"""
Zellers Congruence
"""

# Code for reading in the date */
dates = ['1/1/1980','25/12/1983','2/2/1990', '9/8/1982','31/5/1989','29/2/1992']
for date in dates:
  d,m,y = date.split('/')
  d = int(d)
  m = int(m)
  y = int(y)
  leap = False


  # test for leap year
  div_by_4 = not bool(y % 4)
  div_by_100 = not bool(y % 100)
  div_by_400 = not bool(y % 400)

  if div_by_400:
      leap = True
  elif div_by_4 and not div_by_100:
      leap = True

  # adjustments
  if m in [1,2]:
    m += 12
    if leap:
      d -= 2
    else:
      d -= 1


  # Zellers algorythm
  z = 1 + d + (m * 2) + (3 * (m + 1) // 5) + y + y//4 - y//100 + y//400

  z %= 7

  days = ["Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"]
  print("{0} was a {1}day".format(date, days[z]))

