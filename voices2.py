# **** ****
import speech_recognition as sr


# **** speech response method ****
def speechResponse(words):
    if "hello" in words:
        print("Hello to you too!")
    elif "how are you" in words:
        print("I am well, thanks!")
    elif "goodbye" in words:
        print("Goodbye to you too!")
    elif "good morning" in words:
        print("Good morning!")

    elif "good afternoon" in words:
        print("Good afternoon!")
    elif "good evening" in words:
        print("Good evening!")
    elif "goodnight" in words:
        print("Hope you sleep well tonight!")
    else:
        print("Huh?")


# **** main method ****
def main():

    # **** obtain audio from microphone ****
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something (use microphone): ")
        audio = r.listen(source)
        
    # **** recognize speech using Google Speech Recognition ****
    words = r.recognize_google(audio)
    print(f"words ==>{words}<==\n")

    # **** respond to speech ****
    speechResponse(words)


# **** call main method ****
main()