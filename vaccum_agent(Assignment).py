import time
import pyttsx3
engine = pyttsx3.init()


def vaccum_agent(dirt, vaccum):
    while dirt[0] or dirt[1]:
        if vaccum[0]:
            print('The vaccum is in room A\n')
            engine.say('The vaccum is in room A')
            engine.runAndWait()

            time.sleep(3)

            if dirt[0]:
                print('Dirt found in room A\n')
                engine.say('Dirt found in room A')
                engine.runAndWait()

                time.sleep(3)
                
                print('Cleaning dirt in room A\n')
                engine.say('Cleaning dirt in room A')
                engine.runAndWait()
                time.sleep(3)

                dirt[0] = False  # Clean the dirt

            print('Moving to room B\n')
            engine.say('Moving to room B')
            engine.runAndWait()

            time.sleep(3)

            vaccum[0] = False
            vaccum[1] = True

        elif vaccum[1]:
            print('The vaccum is in room B\n')
            engine.say('The vaccum is in room B')
            engine.runAndWait()
            time.sleep(3)

            if dirt[1]:
                print('Dirt found in room B\n')
                engine.say('Dirt found in room B')
                engine.runAndWait()
                time.sleep(3)

                print('Cleaning dirt in room B\n')
                engine.say('Cleaning dirt in room B')
                engine.runAndWait()
                time.sleep(3)

                dirt[1] = False  # Clean the dirt

            print('Moving to room A\n')
            engine.say('Moving to room A')
            engine.runAndWait()
            time.sleep(3)

            vaccum[1] = False
            vaccum[0] = True

    print('No dirt found!')
    engine.say('No dirt found!')
    engine.runAndWait()



def main():
    Truth_list_dirt = [True , True]
    Truth_list_vaccum = [False , True]
    vaccum_agent(Truth_list_dirt,Truth_list_vaccum)


if __name__ == '__main__':
    main()

           