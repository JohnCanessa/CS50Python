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
    else:
        print("Huh?")


# **** main method ****
def main():

    # **** ****
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something: ")
        audio = r.listen(source)

    # **** ****
    print("Google Speech Recognition thinks you said: ")
    print(r.recognize_google(audio))


# **** call main method ****
main()

# # **** prompt for some words ****
# words = input("say something: ").lower()
# print(f"words: {words}\n")

# # **** call textResponse method ****
# textResponse(words)