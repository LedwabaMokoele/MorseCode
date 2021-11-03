def checkAssertion(phrase, morse):
	assert(phrase.count(' ') == morse.count('/')),"Number of spaces are not the same"
	assert(len(phrase) == len(morse.split())),"Number of characters are not the same"

def lettersToMorseCode(phrase_1):
	if phrase_1 == "":
		print("")
		return
	morse_chart = {"A": ".-", "B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","&": ".-...","'": ".----.","@":".--.-.",")":"-.--.-","(":"-.--.",":":"---...",",":"--..--","=":"-...-","!":"-.-.--",".":".-.-.-","-":"-....-","×":"-..-","%":"----- -..-. -----","+":".-.-.",'"':".-..-.","?":"..--..","/":"-..-."," ": " / "}
	morse_code = ""
	for i in range(0,len(phrase_1)):
		morse_code += " "+ morse_chart[phrase_1[i].upper()]
	checkAssertion(phrase_1,morse_code)
	print(morse_code)

def morseCodeToLetters(phrase_1):
	if phrase_1 == "":
		print("")
		return
	morse_chart = {"A": ".-", "B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","&": ".-...","'": ".----.","@":".--.-.",")":"-.--.-","(":"-.--.",":":"---...",",":"--..--","=":"-...-","!":"-.-.--",".":".-.-.-","-":"-....-","×":"-..-","%":"----- -..-. -----","+":".-.-.",'"':".-..-.","?":"..--..","/":"-..-."," ": "/"}
	morse_decoded = ""
	list_of_morse_values = phrase_1.split();
	morse_items = morse_chart.items()
	for i in list_of_morse_values:
		for key, value in morse_chart.items():
			if i == value:
				morse_decoded +=key
	checkAssertion(morse_decoded,phrase_1)
	print(morse_decoded.capitalize())
		
lettersToMorseCode("Apples are for everybody!")
morseCodeToLetters('.... .. / - .... . .-. .')