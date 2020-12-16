#advent calendar day 4
import fileinput

#apparently you can do switch statement in Python by putting methods in a dictionary
def birthYear(byr):
    byr = int(byr)
    return byr >= 1920 and byr <= 2002

def issueYear(iyr):
    iyr = int(iyr)
    return iyr >= 2010 and iyr <= 2020

def expYear(eyr):
    eyr = int(eyr)
    return eyr >= 2020 and eyr <= 2030

def height(hgt):
    #get the last two 
    units = hgt[-2:]
    if hgt[:-2].isnumeric():
        measurement = int(hgt[:-2])
    else:
        return False
        
    if units == "cm":
        return measurement >= 150 and measurement <= 193
    elif units == "in":
        return measurement >= 59 and measurement <= 76
    else:
        return False

def hairColor(hcl):
    hashTag = hcl[0]
    color = hcl[1:]
    if hashTag == '#':
        for letter in color:
            if letter >= 'a' or letter <= 'f':
                pass
            elif letter >= '0' or letter <= '9':
                pass
            else:
                return False
        return True
    else:
        return False

def eyeColor(ecl):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in eye_colors

def passportID(pid):
    valid = pid.isnumeric() and len(pid) == 9
    #if not valid:
        #print(pid.isnumeric(), len(pid))
    return valid

passport = {}
numValidPassports = 0
valid_fields = {}

for line in fileinput.input(files = "advent4input.txt"):
    #print(line)
    if line == "\n":
        validPassport = True
        #check passport for missing fields
        for field in valid_fields.keys():
            if field not in passport.keys():
                validPassport = False
                break
            
        if validPassport:
            valid_fields = {"byr": birthYear(passport.get("byr")), 
                "iyr": issueYear(passport.get("iyr")), 
                "eyr": expYear(passport.get("eyr")),
                "hgt": height(passport.get("hgt")),
                "hcl": hairColor(passport.get("hcl")),
                "ecl": eyeColor(passport.get("ecl")),
                "pid": passportID(passport.get("pid"))}
            if all(valid_fields.values()):
                numValidPassports += 1
        #clear list
        passport = {}
    else:
        entries = line.split()
        for item in entries:
            key, value = item.split(":")
            passport[key] = value
            
print(numValidPassports)

























    
