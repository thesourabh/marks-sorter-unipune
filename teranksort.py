fp = open('teresult.txt')
lines = fp.read().split('. . . . . . . . . . . .')
fp.close()
roll = []
students = []
percent = []
found = 0
student = ""
for x in lines:
 if ((x.find("T808842") != -1) and (x.find("FIRST TERM TOTAL") != -1)):
  found = x.find("T808842")
  roll.append(x[found:found+10])
  student = x[found+10:found+54]
  students.append(student.strip())
  found = x.find("/750")
  marks = float(x[found-3:found])
  percent.append("%.2f" % (marks/7.5))

#for any small updates
fp = open("resultupdates.txt","r")
lines = fp.read().split('. . . . . . . . . . ')
fp.close()
for x in lines:
 if ((x.find("T808842") != -1) and (x.find("FIRST TERM TOTAL") != -1)):
  found = x.find("T808842")
  for i in xrange(len(roll)):
   if (roll[i] == x[found:found+10]):
    students[i] == x[found+10:found+54].strip()
    found = x.find("/750")
    marks = float(x[found-3:found])
    percent[i] = "%.2f" % (marks/7.5)


fp = open("resultranked.txt","w")
fpsite = open("resultranked.html","w")
outp = ""
webout = "<html>\n<head><title>Rank List</title></head>\n<body>\n"
webout += "<h5>In case of any corrections, contact me. Rank list generated using Python.</h5>\n"
webout += "<table>\n"
curr = max(percent)
i = len(percent)-1
count = len(percent)

rank = 0
prev = 0
while i >= 0:
  for j in xrange(len(percent)):
   if curr == percent[j]:
    if (prev != curr):
     rank += 1
    outp = outp + percent[j]+'\t'+str(students[j]) + "\n"
    webout = webout + "<tr><td>" + str(rank)+"</td><td>"+percent[j] + "</td><td>" + roll[j] + "</td><td>" + str(students[j]) + "</td></tr>\n"
    percent.remove(percent[j])
    students.remove(students[j])
    i -= 1
    prev = curr
    break
  if (len(percent) == 0):
    break
  curr = max(percent)

outp += "\n"
fp.write(outp)
fp.close()

webout += "</table>\n<br><br>Total results sorted: " + str(count)
webout += "\n<h5>Copyright &copy; 2014 Sourabh Shetty</h5>\n</body>\n</html>"

fpsite.write(webout)
fpsite.close()