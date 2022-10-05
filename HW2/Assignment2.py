#Name: Sahil Mahendra Mody
#CWID: 20007262
# Assignment 2



f=open('./Mody_Sahil Mahendra_GEDCOM.ged',"r")
#print(f.read())
l=f.read().split('\n')
f.close()
# print(l)

tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM','MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

dummy=l

for i in range(len(dummy)):
    temp=dummy[i].split(" ")
    if len(temp)>2:
        if temp[2]=='INDI' or temp[2]=='FAM':
            temp[1],temp[2]=temp[2],temp[1]
            dummy[i]=' '.join(temp)

print(dummy)


fl = open("./Demo.txt", "w")
for i in range(len(l)):
    fl.write("-->{}\n".format(l[i]))
    temp=dummy[i].split(' ')
    #print(temp)

    if len(temp)==2:
        if temp[1] in tags:
            valid='Y'
        else:
            valid='N'
        fl.write("<--{}|{}|{}\n".format(temp[0], temp[1], valid))
        continue
    if temp[1] in tags:
        valid = 'Y'
    else:
        valid = 'N'
    fl.write("<--{}|{}|{}|{}\n".format(temp[0],temp[1],valid,' '.join(temp[2:])))

fl.close()
