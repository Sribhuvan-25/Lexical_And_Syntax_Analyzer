def insideBrackets(statement, startBracket, endBracket):

    bracketCounter = 1
    currentIndex = 1

    while bracketCounter > 0 :
        if statement[currentIndex] == startBracket:
            bracketCounter += 1
        elif statement[currentIndex] == endBracket:
            bracketCounter -= 1

        currentIndex += 1
    
    return [statement.substring(1,currentIndex-1), statement.substring(currentIndex)]

