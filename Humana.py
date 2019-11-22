#####################################################################
# Humana Data Engineer Challenge
# Jiang Yao
# 11/22/2019
#####################################################################

import re

# Function to return string of the first part of broken line
def getFirstPart(partLine):
    newLine = "NEWLINE"
    lineFields = partLine.split('\t')
    fieldsBeforeLast = '\t'.join(lineFields[:-1])
    lastFieldNoLastChar = lineFields[-1][:-1]

    s = '%s\t%s%s' % (fieldsBeforeLast, lastFieldNoLastChar, newLine)
    return( s )


dataFileName = "data.tsv"
outPutFile = "new_data.tsv"

# Open data.tsv with "utf-16le" encoding
dataFile = open(dataFileName, mode='r', encoding='utf-16le' )

# Write formatted records to "new_data.tsv with "utf-8" encoding
formattedfile = open(outPutFile, mode='w', encoding='utf-8')

# initialization
header = 0
firstPart = ""
tmpLine = "Empty"

for line in dataFile:
    # write the first line of data.tsv into new file.
    if header == 0:
        formattedfile.write(line)
        header = 1
    else:

        # new record starts with digit

        if re.match("^\d",line):
            goodLine = "Ept"
            # write the line before this line into file
            if tmpLine != "Empty":
                for f in (firstPart +tmpLine).split('\t'):
                    if re.search('NEWLINE', f):
                        goodLine = goodLine + '\t\"' + f.replace('NEWLINE', '\\n') + '\"'
                    else:
                        if goodLine == "Ept":
                            goodLine = f
                        else:
                            goodLine = goodLine +"\t"+ f

                formattedfile.write(goodLine)
            else:
                pass

            # initial tmpLIne when it's the first part(or whole line) of a new record
            tmpLine ="Empty"

            # There are 5 fields in data file "id", "first_name", "last_name", "account_number" and "email"
            # get the number of fields in the line, if number is less than 5, that indicates it's a broken line
            if len(line.split('\t')) < 5:
                firstPart = getFirstPart(line)

            # not a broken line, write it into new file
            else:
                formattedfile.write(line)
        else:
            if tmpLine != "Empty":
                tmpLineNoLastChar = tmpLine[:-1]
                tmpLineLastChar = tmpLine[-1]
                tmpLine =  tmpLineNoLastChar +'NEWLINE' + line
                # tmpLine =  tmpLineNoLastChar  + line
            else:
                tmpLine = line

formattedfile.close()

dataFile.close()
