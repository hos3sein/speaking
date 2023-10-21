import pyttsx3


def speak(input):

	# text = 'hello evetyone'
	engin = pyttsx3.init()

	engin.setProperty('rate' , 150)
	engin.setProperty('volume' , 0.8)


	engin.say(text)
	engin.runAndWait()



while(1):      
    # Exception handling to handle
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognize
            r.adjust_for_ambient_noise(source2, duration=0.2)

            #listening
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            speak(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")








