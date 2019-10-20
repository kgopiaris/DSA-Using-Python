
# Here is the code for assigning cab.

cabs = [{"type":"1.Micro","price":10, "available":3},
		 {"type":"2.Mini","price":12, "available":2},
		 {"type":"3.Prime","price":15, "available":5}]

def ride():
 if cabs[0]["available"] == 0 and cabs[1]["available"] == 0 and cabs[2]["available"] == 0:
  print "Sorry there is no cab available in all categories"
  return
 print "\n\n List of cabs available..."
 for itm in cabs:
  print itm["type"], "\t Price per km:", itm["price"], " No of available: ", itm["available"]
 
 cab_type = input("Please select the cab type \n ")
 
 if cab_type == 1:
  if cabs[0]["available"] == 0:
   print "Sorry there is no cab available in this category please choose another cab type"
  else:
   st_km = input("Enter the Starting point\n")
   end_km = input("Enter the End point\n")
   total_kms = end_km-st_km
   print "Total kms: "+str(total_kms)+" fare is: "+ str(total_kms*cabs[0]["price"])
   cabs[0]["available"] -=1
  ride()
 elif cab_type == 2:
  if cabs[1]["available"] == 0:
   print "Sorry there is no cab available in this category please choose another cab type"
  else:
   st_km = input("Enter the Starting point\n")
   end_km = input("Enter the End point\n")
   total_kms = end_km-st_km
   print "Total kms: "+str(total_kms)+" fare is: "+ str(total_kms*cabs[1]["price"])
   cabs[1]["available"] -=1
  ride()
 elif cab_type == 3:
  if cabs[2]["available"] == 0:
   print "Sorry there is no cab available in this category please choose another cab type"
  else:
   st_km = input("Enter the Starting point\n")
   end_km = input("Enter the End point\n")
   total_kms = end_km-st_km
   print "Total  kms: "+str(total_kms)+" fare is: "+ str(total_kms*cabs[2]["price"])
   cabs[2]["available"] -=1
  ride()
 return
