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
#include <CoreAudio/CoreAudioTypes.h>

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
    
    //OSType dataFormat = kAudioFormatLinearPCM;
    /* kAudioFormatLinearPCM               = 'lpcm',
     kAudioFormatAC3                     = 'ac-3',
     kAudioFormat60958AC3                = 'cac3',
     kAudioFormatAppleIMA4               = 'ima4',
     kAudioFormatMPEG4AAC                = 'aac ',
     kAudioFormatMPEG4CELP               = 'celp',
     kAudioFormatMPEG4HVXC               = 'hvxc',
     kAudioFormatMPEG4TwinVQ             = 'twvq',
     kAudioFormatMACE3                   = 'MAC3',
     kAudioFormatMACE6                   = 'MAC6',
     kAudioFormatULaw                    = 'ulaw',
     kAudioFormatALaw                    = 'alaw',
     kAudioFormatQDesign                 = 'QDMC',
     kAudioFormatQDesign2                = 'QDM2',
     kAudioFormatQUALCOMM                = 'Qclp',
     kAudioFormatMPEGLayer1              = '.mp1',
     kAudioFormatMPEGLayer2              = '.mp2',
     kAudioFormatMPEGLayer3              = '.mp3',
     kAudioFormatTimeCode                = 'time',
     kAudioFormatMIDIStream              = 'midi',
     kAudioFormatParameterValueStream    = 'apvs',
     kAudioFormatAppleLossless           = 'alac',
     kAudioFormatMPEG4AAC_HE             = 'aach',
     kAudioFormatMPEG4AAC_LD             = 'aacl',
     kAudioFormatMPEG4AAC_ELD            = 'aace',
     kAudioFormatMPEG4AAC_ELD_SBR        = 'aacf',
     kAudioFormatMPEG4AAC_ELD_V2         = 'aacg',
     kAudioFormatMPEG4AAC_HE_V2          = 'aacp',
     kAudioFormatMPEG4AAC_Spatial        = 'aacs',
     kAudioFormatAMR                     = 'samr',
     kAudioFormatAMR_WB                  = 'sawb',
     kAudioFormatAudible                 = 'AUDB',
     kAudioFormatiLBC                    = 'ilbc',
     kAudioFormatDVIIntelIMA             = 0x6D730011,
     kAudioFormatMicrosoftGSM            = 0x6D730031,
     kAudioFormatAES3                    = 'aes3'*/
    
    //  kAudioFileAIFFType, kAudioFileWAVEType, kAudioFileM4AType (using AAC audio encoding), and kAudioFileCAFType.
    
    //    CFStringRef theBaseStr = CFSTR("file:///Users/johnpope/Documents/gitWorkspace/pyau/");
    //    CFStringRef theRelativeStr = CFSTR("test1.wav");
    //
    //    CFURLRef theBaseURL = CFURLCreateWithString(NULL, theBaseStr, NULL);
    //
    //    CFURLRef url = CFURLCreateCopyAppendingPathExtension(NULL, theBaseURL, theRelativeStr);
    
    CFStringRef theBaseStr = CFSTR("file:///Users/johnpope/Documents/gitWorkspace/pyau/");
    CFStringRef theRelativeStr = CFSTR("test1.wav");
    CFURLRef theBaseURL = CFURLCreateWithString(NULL, theBaseStr, NULL);
    CFURLRef url = CFURLCreateCopyAppendingPathExtension(NULL, theBaseURL, theRelativeStr);
    host2.BounceToFile(url,kAudioFormatLinearPCM,kAudioFileWAVEType); // warning - check the
    
    //print_host(host1);
    //print_host(host2);
    //usleep(50000);
    //    host2.Stop();
    //    host2.ResetAudioUnits();
    //host1.Play();
    
    CFRunLoopRun();
}