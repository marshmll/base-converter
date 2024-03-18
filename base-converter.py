hexToDecimal = {
	'A': 10,
	'B': 11,
	'C': 12,
	'D': 13,
	'E': 14,
	'F': 15,
}

def main():
	number = input("Insert a number to convert: ")

	originalBaseN = int(input("Insert the original base: "))
	newBaseM = int(input("Insert the base to convert to (max 16, min 2): "))

	convertedNumber = baseNToM(number, originalBaseN, newBaseM)

	print(f"{number} (base {originalBaseN}) = {convertedNumber} (base {newBaseM})")

def baseNToM(number, n, m):
	convertedNumber = base10ToN(baseNTo10(number, n), m)
	return convertedNumber

def baseNTo10(numberStr, base):
	if base == 10:
		return numberStr
	
	numberInBase10 = 0;
	reversedNumberStr = reversed(numberStr)

	for i, digit in enumerate(reversedNumberStr):
		if digit.isalpha():
			digit = hexToDecimal[digit.upper()]
		
		numberInBase10 += int(digit) * (base ** i)
	
	return numberInBase10

def base10ToN(numberStr, base):
	if base == 10:
		return numberStr
	
	divisionResult = int(numberStr)

	numberInBaseN = ""
	
	while divisionResult != 0:
		remainder = int(divisionResult) % base
		divisionResult = (int(divisionResult) - remainder) / base

		if remainder >= 10 and remainder <= 15:
			remainder = list(hexToDecimal.keys())[list(hexToDecimal.values()).index(remainder)]

		numberInBaseN = str(remainder) + numberInBaseN

	return numberInBaseN

main()
