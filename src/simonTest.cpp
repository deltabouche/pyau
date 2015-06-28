/*
 *  simonTest.cpp
 *
 *  Created by simon on 14/03/09.
 *  Copyright 2009 . All rights reserved.
 *
 */

//#define DEBUG 1

#include <AudioToolbox/AudioToolbox.h>
#include <CoreAudio/CoreAudio.h>
#include "AHHost.h"
#include "AHAudioUnit.h"
#include "AHUtils.h"
#include "FileSystemUtils.h"


#include <iostream>
using namespace std;

void print_host(AHHost &host)
{
    for (int i=0; i<(int)host.GetTracks().size(); i++)
    {
        AHTrack* t = host.GetTracks()[i];
        cout << "track " << i << ": ";
        PrintCFStringRef(t->GetSynth()->GetName());
        PrintCFStringRef(t->GetSynth()->GetManu());
        list<AHAudioUnit*> effects = t->GetEffects();
        for ( list<AHAudioUnit*>::iterator it=effects.begin(); it != effects.end(); it++)
        {
            cout << " => [";
            PrintCFStringRef((*it)->GetName());
            cout << "]";
        }
        cout << endl;
    }
}

int main( int argc, const char* argv[] )
{
    PrintAllAudioUnits();
    AHHost host1 = AHHost();
    AHHost host2 = AHHost();
    
    
    AHTrack* track1 = host1.AddTrack("Zebra2");
    AHTrack* track2 = host2.AddTrack("Zebra2");
    
    track1->GetSynth()->LoadAUPresetFromFile("/Users/johnpope/Library/Audio/Presets/Native Instruments/Kontakt 5/alicia.aupreset");
    track2->GetSynth()->LoadAUPresetFromFile("/Users/johnpope/Library/Audio/Presets/Native Instruments/Kontakt 5/alicia.aupreset");
    
    // EFFECTS
    // AHAudioUnit* dub1 = track1->AddEffect("TAL dub III Plugin");
    //AHAudioUnit* dub2 = track2->AddEffect("TAL dub III Plugin");
    
    //dub1->LoadAUPresetFromFile("/Users/johnpope/Library/Audio/Presets/Native\ Instruments/Kontakt\ 5/emotive.aupreset ");
    // dub2->LoadAUPresetFromFile("/Users/johnpope/Library/Audio/Presets/Native\ Instruments/Kontakt\ 5/emotive.aupreset ");
    
    host1.LoadMidiFile("/Users/johnpope/Documents/gitWorkspace/pyau/Midi/10.mid");
    host2.LoadMidiFile("/Users/johnpope/Documents/gitWorkspace/pyau/Midi/9.mid");
    
    // you may need to wrap this in an autorelease pool
    
    
    // LISTEN TO MIDI
    //host1.ListenToMidi();
    //    host2.ListenToMidi();
    
    //
    //host2.Play();
    host2.BounceToFile("file://Users/johnpope/Documents/gitWorkspace/pyau/Midi/2.wav");

    //print_host(host1);
    //print_host(host2);
    //usleep(50000);
    //    host2.Stop();
    //    host2.ResetAudioUnits();
    //host1.Play();
    
    CFRunLoopRun();
}