'''
This script utilises the Google Cloud Speech API to convert an audio having communication with Hindi and English words into the text format
'''

# Import required libraries
# speech_recognition is required to use the Google Cloud Speech API
# Mutagen is a Python module to handle audio metadata.
import speech_recognition as sr
import mutagen


# Creating a speech recognizing instance
r = sr.Recognizer()
 

# Reading the audio file
audiofile = sr.AudioFile('bb26a2ec-c028-478f-9d2e-1e60e4b2aa6c (FAQ).flac')


# Finding the duration length of the audio (in seconds) to find the number of iterations of 10 sec chunks required for conversion to text
audiotest = mutagen.flac.FLAC('bb26a2ec-c028-478f-9d2e-1e60e4b2aa6c (FAQ).flac')

audio_length = audiotest.info.length

number_of_iterations = int(audio_length/10)



if number_of_iterations == 0:
    number_of_iterations = 1

# Converting Speech to text with Hindi as the language/dialect
for i in range(number_of_iterations):
    with audiofile as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, offset = i*10, duration = 10)
    
    hindi=r.recognize_google(audio, language="hi-IN")
    print(hindi)

# Converting Speech to text with English as the language/dialect
for j in range(number_of_iterations):
    with audiofile as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, offset = j*10, duration = 10)    

    english=r.recognize_google(audio, language="en-US")
    print(english)
    
# Copy in the below json the correct complete contents of your project on the Google Cloud Speech API
credentials = '{"type": "service_account","project_id": "-----","private_key_id": "---","private_key": "-------","client_email": "---------","client_id": "----","auth_uri": "----","token_uri": "----","auth_provider_x509_cert_url": "-----","client_x509_cert_url": "----"}'
r.recognize_google_cloud(audiofile,credentials_json=credentials)
