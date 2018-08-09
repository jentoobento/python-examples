class person(object):
    first="None"
    last="None"
    status="None"
    gross=0.0
    tax=0.0
    net=0.0
  
def addPerson(fir,las,sta,gro,tax,net):
    p=person()
    p.first=fir.title()
    p.last=las.title()
    sta=sta.upper()
    sta = "Single" if sta == "S" else "Joint"
    p.status=sta
    p.gross=float(gro)
    p.tax=float(tax)
    p.net=float(net)
    return p

def addFromFile():
    file=raw_input("Enter full path to file: ")
    while not os.path.isfile(file):
        print("Error. This file could not be opened.")
        file=raw_input("Enter a different path: ")
    while not os.path.getsize(file)>0:
        print("Error. This file is empty.")
        file=raw_input("Enter a different path: ")
    f=open(file)
    for i in f:
        i=i.split()
        status=i[2]
        gross=float(i[3])
        tax,net=findTaxAndNet(status.upper(),gross)
        ppl.append(addPerson(i[0],i[1],status,gross,tax,net))
    f.close()

def findTaxAndNet(status,gross):
    if status=="S":
        if gross<=1710:
            tax = 0
        elif gross<=20930:
            tax = 87 + (0.03 * (gross - 1710))
        elif gross<=28790:
            tax = 742.4 + (0.08 * (gross - 20930))
        else:
            tax = 1449.6 + (0.11 * (gross - 28790))
    if status=="J":
        if gross<=3420:
            tax = 0
        elif gross<=47120:
            tax = 330 + (0.04 * (gross - 3420))
        elif gross<=57580:
            tax = 1905.4 + (0.09 * (gross - 47120))
        else:
            tax = 2899.2 + (0.11 * (gross - 57580))
    net = gross - tax
    return tax,net

def validate(min,max):
  choice=raw_input("Please choose an option: ")
  print(line)
  valid=False
  while(not valid):
    try:
      choice=int(choice)
      while choice<min or choice>max:
        print("Error. Enter a number between",min,"and",max)
        choice=int(raw_input("Please choose an option: "))
      valid=True
    except:
      print("Error. Enter a number between",min,"and",max)
      choice=raw_input("Please choose an option: ")
  return choice

def display(flag,array):
  data=''
  if flag==1: 
    data+=("%-10s%-14s%6s%15s%15s%15s\n"%("First","Last","Status","Gross Income","Taxes","Net Income"))
  else:
    data+=("%-14s%-10s%6s%15s%15s%15s\n"%("Last","First","Status","Gross Income","Taxes","Net Income"))
  data+="="*80+'\n'
  for i in array:
    strgross = "${:,.2f}".format(i.gross)
    strtax = "${:,.2f}".format(i.tax)
    strnet = "${:,.2f}".format(i.net)
    if flag==1:  
      data+=("%-10s%-14s%-6s%15s%15s%15s\n"%(i.first,i.last,i.status,strgross,strtax,strnet))
    else:
      data+=("%-14s%-10s%6s%15s%15s%15s\n"%(i.last,i.first,i.status,strgross,strtax,strnet))
  return data

def writeToFile():
  print(line)
  print("Write the current Employee List to a File")
  print(line)
  file=raw_input("Enter name for file: ")
  f=open(file,'w')
  now=datetime.datetime.now()
  f.write("EMPLOYEE DATABASE AS OF %d/%d/%d\n"%(now.month,now.day,now.year))
  f.write("="*80+'\n')
  f.write(display(1,ppl))
  print("List has been written to",file)
  f.close()

def search():
    print("Search for Employee by First or Last Name")
    print(line)
    name=raw_input("Enter search term: ")
    name=name.upper()
    print(line)
    print("   %-10s%-14s%6s%15s%15s%15s"%("First","Last","Status","Gross Income","Taxes","Net Income"))
    print("="*80)
    foundppl={} 
    index=-1
    count=0
    for i in ppl:
        index+=1
        if (name in i.last.upper()) or (name in i.first.upper()):
            count+=1
            foundppl[count]=index
            print(count,") ")
            displaySingle(i)
    print("There were",count,"results found for that search term.")
    return foundppl

def menu():
  print(line)
  print("Main Menu")
  print(line)
  print("1. Add to list from file")
  print("2. Write full list to a file")
  print("3. Sort and display full list to screen")
  print("4. Display full list to screen")
  print("5. Search and display employee data to screen")
  print("6. Add employee to list")
  print("7. Delete employee from list")
  print("8. Edit employee data")
  print("9. Exit")
  print(line)

def sortList():
  print("  1. Sort by First Name")
  print("  2. Sort by Last Name")
  choice=validate(1,2)
  copyppl=ppl[:] 
  sortedppl=[] 
  stop=len(ppl)
  
  while len(sortedppl) != stop: 
    if len(copyppl)!=0:
      current=copyppl[0] 
      if choice==1: 
        for i in copyppl:
          if i.first == current.first: #if the first names are the same, sort based on last name
            if i.last < current.last:
              current = i
          elif i.first < current.first: #if first names are unique, sort based on first name
            current=i #loop until get the lowest element
      if choice==2: 
        for i in copyppl:
          if i.last == current.last:
            if i.first < current.first:
              current = i
          elif i.last < current.last: 
            current=i 
      copyppl.remove(current) 
      sortedppl.append(current) 
  if choice==1:
    print(display(1,sortedppl))
  if choice==2:
    print(display(2,sortedppl))

def displaySingle(i):
    strgross = "${:,.2f}".format(i.gross)
    strtax = "${:,.2f}".format(i.tax)
    strnet = "${:,.2f}".format(i.net)
    print("%-10s%-14s%-6s%15s%15s%15s"%(i.first,i.last,i.status,strgross,strtax,strnet))

def deletePerson():
    print("Delete Employee from List")
    print(line)
    foundppl=search()
    if len(foundppl)>0:
      print("Delete Employee by Entering the corrospoding number next to their name.")
      num=validate(1,list(foundppl.keys())[-1])
      index=foundppl.get(num)
      i=ppl[index]
      print("Delete",i.first,i.last,"from the List?")
      print("  1. Yes\n  2. No")
      choice=validate(1,2)
      if choice==1:
          del ppl[index]
          print(i.first,i.last,"has been deleted.")
      else:
          print("List is unchanged.")

def editPerson():
    print("Edit Employee from List")
    print(line)
    foundppl=search()
    if len(foundppl)>0:
      print("Choose Employee to Edit by Entering the corrospoding number next to their name.")
      num=validate(1,list(foundppl.keys())[-1])
      index=foundppl.get(num)
      i=ppl[index]
      print("Edit",i.first,i.last,"?")
      print("  1. Yes\n  2. No")
      choice=validate(1,2)
      if choice==1:
          again=True
          while again:
              print("Choose which data to Edit")
              print("1. First Name")
              print("2. Last Name")
              print("3. Filing Status")
              print("4. Gross Income")
              print("5. Go Back")
              choice=validate(1,5)
              if choice==1:
                  newfirst=raw_input("Enter the new First Name: ")
                  i.first=newfirst.title()
              if choice==2:
                  newlast=raw_input("Enter new Last Name: ")
                  i.last=newlast.title()
              if choice==3:
                  newstatus=raw_input("Enter new Filing Status: ")
                  while (newstatus.upper() != 'S') and (newstatus.upper() != 'J'):
                      print("Error. Please enter S for Single or J for Joint.")
                      newstatus = raw_input("Enter new Filing status: ")
                  newstatus=newstatus.upper()
                  newstatus = "Single" if newstatus == "S" else "Joint"
                  i.status=newstatus
                  i.tax,i.net=findTaxAndNet(i.status[0],i.gross)
              if choice==4:
                  newgross=raw_input("Enter new Gross Income: ")
                  while (not newgross.isdigit()) or (float(newgross)<=0):
                      print("Error. Please enter valid positive number.")
                      newgross=raw_input("Enter gross income: ")
                  i.gross=float(newgross)
                  i.tax,i.net=findTaxAndNet(i.status[0],i.gross)
              if choice==5:
                  again=False
              if again:
                  print("Employee data has been updated!")
      else:
          print("Employee data is unchanged.")

import datetime
import os
ppl=[]
addFromFile() #Assumption that import file is in correct format
saved=True
again=True
while(again):
  line="="*50
  menu()
  choice=validate(1,9)
  if choice==1:
    print("Add to List from File")
    print(line)
    addFromFile()
    print("List has been updated!")
    saved=False
  if choice==2:
    print("Write full list to a file")
    writeToFile()
    saved=True
  if choice==3:
    print("Sort and Display List on Screen")
    print(line)
    sortList()
  if choice==4:
    print()
    print(display(1,ppl))
  if choice==5:
    foundppl=search()
  if choice==6:
    print("Add Employee to List")
    print(line)
    f=raw_input("Enter first name: ")
    l=raw_input("Enter last name: ")
    s=raw_input("Enter filing status [S]ingle or [J]oint: ")
    while (s.upper() != 'S') and (s.upper() != 'J'):
      print("Error. Please enter S for Single or J for Joint.")
      s = raw_input("Enter filing status: ")
    g=raw_input("Enter gross income: ")
    while (not g.isdigit()) or (float(g)<=0):
      print("Error. Please enter valid positive number.")
      g=raw_input("Enter gross income: ")
    tax,net=findTaxAndNet(s.upper(),float(g))
    ppl.append(addPerson(f,l,s,g,tax,net))
    print(line)
    print(f.title(),"has been added!")
    saved=False
  if choice==7:
    deletePerson()
    saved=False
  if choice==8:
    editPerson()
    saved=False
  if choice==9:
    if (not saved):
        print("There are unsaved changes to the List!")
        print("Exit without saving?")
        print("  1. Yes\n  2. No")
        option=validate(1,2)
        if option==1:
            print(line)
            print(line)
            print("Exiting program.")
            again=False
    else:
        print(line)
        print(line)
        print("Exiting program.")
        again=False
