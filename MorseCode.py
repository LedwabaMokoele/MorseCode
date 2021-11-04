
morse_chart = {"A": ".-", "B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","&": ".-...","'": ".----.","@":".--.-.",")":"-.--.-","(":"-.--.",":":"---...",",":"--..--","=":"-...-","!":"-.-.--",".":".-.-.-","-":"-....-","×":"-..-","%":"----- -..-. -----","+":".-.-.",'"':".-..-.","?":"..--..","/":"-..-."," ": " / "}
def checkAssertion(phrase, morse):
	'''Assertion function to make sure that the conversions were done properly in the sense that the spaces and characters match''' 
	assert(phrase.count(' ') == morse.count('/')),"Number of spaces are not the same"
	assert(len(phrase) == len(morse.split())),"Number of characters are not the same"

def lettersToMorseCode(phrase_1):
	if phrase_1 == "":
		print("")
		return
	
	morse_code = ""
	for i in range(0,len(phrase_1)):
		morse_code += " "+ morse_chart[phrase_1[i].upper()]
	checkAssertion(phrase_1,morse_code)
	print(morse_code)

def morseCodeToLetters(phrase_1):
	if phrase_1 == "":
		print("")
		return
	'''This chart is different to the chart that was created as a global variable reason being that the space character is defined differently when decoding hence i defined it again'''	
	morse_chart2 = {"A": ".-", "B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","&": ".-...","'": ".----.","@":".--.-.",")":"-.--.-","(":"-.--.",":":"---...",",":"--..--","=":"-...-","!":"-.-.--",".":".-.-.-","-":"-....-","×":"-..-","%":"----- -..-. -----","+":".-.-.",'"':".-..-.","?":"..--..","/":"-..-."," ": "/"}
	'''morse_decoded is a variable to store the decoded string''' 
	morse_decoded = ""
	'''list_of_morse_values is a variable to store the morse code string as an array of characters'''
	list_of_morse_values = phrase_1.split();
	morse_items = morse_chart2.items()

	for i in list_of_morse_values:
		for key, value in morse_chart2.items():
			if i == value:
				morse_decoded +=key
	checkAssertion(morse_decoded,phrase_1)
	print(morse_decoded.capitalize())
		
lettersToMorseCode("Apples are for everybody!")
morseCodeToLetters('.... .. / - .... . .-. .')