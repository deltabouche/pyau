pyau
====

Python Audio Unit Host



Current features
================

* Hosts audio units
* Supports multiple tracks
* Can use midi files to bounce audio
* Listens to incoming midi messages (e.g. from a keyboard)


Requirements
============
A mac with at least Leopard (10.5) with the following installed

* Python 2.5 or higher (with pip)
* Xcode
* Swig (with python bindings)


Installation
============

    brew install swig

    git clone https://github.com/simlmx/pyau.git
    cd pyau
    python setup.py build  # Make sure you don't skip this step!
    python setup.py install

In the python interpreter (opened from a different directory), verify that the following works:

    import pyau


Usage
=====
* You can find a basic example in pyau/example.py


The audio unit 'tests' - 'sdfs' could not be foundTracks :
0: [ DLSMusicDevice ] => [ AUPitch ]
1: [ DLSMusicDevice ] => [ AUPitch ]
2: [ DLSMusicDevice ] => [ AUPitch ] => [ AUPitch ]

DLSMusicDevice by Apple
Tracks :
0: [ DLSMusicDevice ] => [ AUPitch ]
1: [ DLSMusicDevice ] => [ AUPitch ] -- ARMED
2: [ DLSMusicDevice ] => [ AUPitch ] => [ AUPitch ]

Some parameters for synth DLSMusicDevice :
Tuning = 0 Cents
Volume = 0.0 dB
Reverb Volume = 0.0 dB




TODOs
================
* Loading of carbon/cocoa audio units' gui




XCode Sample Project > 

Spit out a list of available 

------- SYNTHS -------

tonespace - mucoder
Kontakt 5 - Native Instruments
Spectral - LinPlug
DLSMusicDevice - Apple
AUMIDISynth - Apple
AUSampler - Apple
Omnisphere - Spectrasonics
Drone - Cognitone
Nexus - reFX
sforzando - Plogue Art et Technologie
Podolski - u-he
Zebra2 - u-he
Zebralette - u-he
Cream - Kirnu
Vienna Ensemble Pro Event Input - VSL
Vienna Ensemble Pro Surround - VSL
Vienna Ensemble Pro - VSL

------- EFFECTS -------

AUBandpass - Apple
AUDynamicsProcessor - Apple
AUDelay - Apple
AUDistortion - Apple
AUFilter - Apple
AUGraphicEQ - Apple
AUHipass - Apple
AUHighShelfFilter - Apple
AUPeakLimiter - Apple
AULowpass - Apple
AULowShelfFilter - Apple
AUMultibandCompressor - Apple
AUMatrixReverb - Apple
AUNBandEQ - Apple
AUNetSend - Apple
AUParametricEQ - Apple
AURoundTripAAC - Apple
AURogerBeep - Apple
AUSampleDelay - Apple
AUPitch - Apple
ArtsAcoustic Reverb - ArtsAcoustic
Vienna Ensemble Pro Audio Input - VSL

------- MUSIC EFFECTS -------

Altiverb 6 - Audio Ease
Melodyne - Celemony
Zebrify - u-he
ZRev - u-he

