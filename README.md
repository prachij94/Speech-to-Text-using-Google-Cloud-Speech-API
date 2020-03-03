# Speech-to-Text-using-Google-Cloud-Speech-API

This python script uses [the Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text) for transcribing audio file formats like *.flac* files to a text-formatted output about the communication. Please refer to their [pricing policy](https://cloud.google.com/speech-to-text/pricing) for further details. Currently we have used the standard model in the basic (free) tier.

## Prerequisites:

A google cloud account should be already created and billing enabled for the Speech-to-Text API project. The API environment should be set in the local system terminal/cmd using the setup steps given in the [documentation](https://cloud.google.com/speech-to-text/docs/quickstart).

This will allow you to set a private key and other credentials like project id, etc. required in the python script for communication with the API.

## Requirements:

- mutagen
- SpeechRecognition
- google-api-python-client

Please read the given links for more details about the utility of [Mutagen](http://mutagen.readthedocs.io/en/latest/) and [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) libraries in python.
