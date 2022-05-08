import speech_recognition as sr
import pyttsx3
import keyboard
import random #pour la generation du nombre aleatoire
import time #Pour la generation de temporisation

r = sr.Recognizer()
engine = pyttsx3.init()

while True:
    
        
    if (keyboard.read_key() == "backspace"):
        break
    elif (keyboard.read_key() == "space"):
        with sr.Microphone() as source:
            
            print("Que voulez vous ?")
            audio_data = r.record(source ,duration = 4)
            print("Compréhension en cours...")
            try:  
                MyText = r.recognize_google(audio_data, language="fr-FR")
                print("Avez vous dit : ", MyText)
                print(" ")
                
                Mot_1 = 'mode vocal'
                Mot_2 = 'erreur'
    
                if Mot_1 in MyText: 
                    print('Je passe en mode vocal') 
                    vocal = True            
                    engine.say('Vocal mode enabled')
                    engine.runAndWait()
                    break
                elif Mot_2 in MyText: 
                    print('J\'ai rencontre une erreur')
                    engine.say("I got an error")
                    engine.runAndWait()
                else:
                    print("Je n'ai pas compris votre commande")
                    engine.say("Unrecognized by the system") 
                    engine.runAndWait()
            except sr.UnknownValueError:  
               print("Echec de la reconnaissance vocale") 
               engine.say('Vocal recognition failure   ! ') 
               engine.runAndWait()  
               
            except sr.RequestError as e:  
               print("error; {0}".format(e))
                
        continue    

if (vocal==True):
    print("test")
    erreur = 0
    """ Debut de la boucle de generation des erreurs vocales"""
    while (erreur<5):
        nbrandom = random.randint(1, 3)
        if (nbrandom == 1):
            print("cas 1")
            engine.say('I\'ve loose a part. Please acquit the error')
            engine.runAndWait()
            erreur += 1
            time.sleep(3)
            continue

        elif (nbrandom == 2):
            print("cas 2")
            engine.say('There is no more part. Waiting to continue')
            engine.runAndWait()
            erreur += 1
            time.sleep(3)
            continue

        else:
            print("cas 3")
            engine.say('The air pressure is too low. Security activated')
            engine.runAndWait()
            erreur += 1
            time.sleep(3)
            continue

engine.say('End of the vocal mode')
engine.runAndWait()
          
        
        
         
           