# VoiAuth

## Features to incorporate

Training Data - 1 min max per user
Confidence difference of 55% between match and no match classifications

## Endpoints:

Training Endpoint:
Takes a voice clip upload as input along with the persons name and trains the SVM using MFCC Co-efficients as feature vectors.

Authentication Endpoint:

Upload a voice clip and pick users stored in DB through drop-down to check if the audio clip is a match or no match

## PROCESS

MFCC is picked for speaker recognition as it helps pick features according to human hearing. 13 cepstrum coefficients are obtained.
The speech signal is segmented into 40ms windows and MFCC coefficients are obtained for each window. Each window is used as a training sample to be passed to the SVM.
SVC is used for multi-class classification with one-vs-one configuration.

For the testing procedure, the speech signal is broken down again into 40ms windows and majority voting is used to match the to the speaker

