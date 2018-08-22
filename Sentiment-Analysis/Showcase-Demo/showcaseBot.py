from __future__ import print_function

opinion_file = "C:/Users/GARLA/Documents/Sentiment Analysis/Showcase Demo/robotDemo_opinions.txt"
prediction_file = "C:/Users/GARLA/Documents/Sentiment Analysis/Showcase Demo/robotDemo_predictions.txt"

DIMENSIONS = 80
MAX_WORDS = 20000
EPOCHS = 10
BATCH_SIZE = 200
MAX_LEN = 300
VAL_SPLIT= 0.1

from keras.models import model_from_json  
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Bidirectional
from keras.layers import LSTM
from keras.datasets import imdb
import numpy as np

###########################################################################
def save_model(model):
    # Save the weights
    model.save_weights('model_weights.h5')    
    # Save the model architecture
    with open('model_architecture.json', 'w') as f:
        f.write(model.to_json())
###########################################################################        
def load_model():  
    # Model reconstruction from JSON file
    with open('model_architecture.json', 'r') as f:
        model = model_from_json(f.read())
    
    # Load weights into the new model
    model.load_weights('model_weights.h5')
    model.compile(optimizer='rmsprop', loss='binary_crossentropy',metrics=['accuracy'])
    return model
###########################################################################
model = load_model()

###########################################################################
def writePredictionToFile(prediction): 
    predictionString = str(prediction[0,0])
    with open(prediction_file, 'a') as the_file:
        the_file.write(predictionString + '\n')
###########################################################################
def nLinesInFile():
    with open(opinion_file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

nKnownOpinions = nLinesInFile();
###########################################################################
fileChanged = False;
def newOpinionAdded():
    if nKnownOpinions != nLinesInFile():
        return True
    else: 
        return False       
###########################################################################
def readLastOpinionFromFile():
    with open(opinion_file, "r") as f:
        for line in f: pass
        return line.rstrip() #this is the last line of the file

readLastOpinionFromFile()      
###########################################################################

model.summary()
import time
starttime=time.time()
#ENCODE OWN STRING
OFFSET = 3
word_index = imdb.get_word_index()
   
while True: #Loop that runs once every 1 second
    if newOpinionAdded():
        my_blurb = readLastOpinionFromFile()
        print(my_blurb)
        listOfWords = my_blurb.split()

        encoded_review = [1]
        for word in listOfWords:
            if word in word_index and word_index[word] < MAX_WORDS:
                index = word_index[word] + OFFSET
            else:
                index = 2
    
            encoded_review.append(index)

        data = np.array(encoded_review)  
        data.shape = [1,len(encoded_review)]
        x_custom_test = sequence.pad_sequences(data, maxlen=MAX_LEN)                                                       
        results = model.predict(np.array(x_custom_test)) 
        writePredictionToFile(results)
        nKnownOpinions += 1
    else:
        print("tick")
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))