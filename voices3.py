# **** ****
import re
import speech_recognition as sr


# **** respond to speech method ****
def speechResponse(words):
    
    # **** ****
    matches = re.search("my name is (.*)", words)
    #print(f"type(matches): {type(matches)}")

    # **** build proper response ****
    if matches:
        print(f"matches: {matches}\n")
        print(f"Hey, {matches[1].title()}!!!")
    else:
        print("Hey you.")


# **** main method ****
def main():

    # **** obtain audio from microphone ****
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say: my name is ... (use microphone): ")
        audio = r.listen(source)
        
    # **** recognize speech using Google Speech Recognition ****
    words = r.recognize_google(audio)
    print(f"words ==>{words}<==\n")

    # **** respond to speech ****
    speechResponse(words)

# **** call main method ****
main()