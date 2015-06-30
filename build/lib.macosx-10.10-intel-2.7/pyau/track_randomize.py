# 
# Utils for randomizing a complete track, instead of doing it for individual tracks
#
# Simon Lemieux 
# march 27th 2010
#

 
from pyau import Host
import os.path
#from pyau.generators.factory import get_randomizer
from generators.factory import get_randomizer
import numpy as N

import logging ; log = logging.getLogger('track_randomize')

def get_track_randomizers(host, volumes=None, prob_on_effects=None):
    """ Returns a list of randomizers, one for each synth/effect in 'host', for the first track.
        volumes : Output volume for each synth/effect (a list).
                    If you're planning on actually randomize something, I'll *need* to pass the volumes
        prob_on_effects : Probability for the effects of being On.
    """
    if prob_on_effects is None:
        prob_on_effects = [1.]*len(host.tracks[0].effects)
    if volumes is None:
        volumes = [.4]*(len(host.tracks[0].effects) + 1)
        
    randomizers = [ get_randomizer(host.tracks[0].synth, host, volumes[0]) ]
    randomizers += [ get_randomizer(e, host, v, p) for e,v,p in zip(host.tracks[0].effects, volumes[1:], prob_on_effects) ]
    
    return randomizers
    
    
def randomize_track(host, randomizers=None, verbose=False):
    """ Randomizes the first track of the 'host' using the randomizers.
        Use get_track_randomizers(...) to generate the randomizers.
        We recommand to specity the `randomizers` since it's generally better to set their volume individually.
        Returns True if all went well, False if not. However, False should be very unusual, if randomizers were well implemented.
    """
    aus = [host.tracks[0].synth] + host.tracks[0].effects
    
    if randomizers is None:
        randomizers = get_track_randomizers(host)
    
    for au in aus:
        au.bypass = True
        
    everything_went_fine = True
    for au,r in zip(aus, randomizers):
        au.bypass = False
        nb_trials = r.randomize_parameters()
        if nb_trials == -1: # if something went wrong
            log.warning('Something went wrong for audiounit %s', au.name)
            #if verbose:
            #    print '%s had some problem!' % au.name
            everything_went_fine = False
    
    if verbose:
        print 'Used ',
        for r in randomizers:
            if r.au.bypass == False:
                print '%s ' %r.au.name,
        print
    return everything_went_fine
    
def save_aupresets(aupresets_dir, host):
    """ Saves the aupresets of each unit of the first track of the 'host' in 'aupresets_dir'.
        The name of thes files are the_name_of_the_audio_unit.aupreset    
        
        Also creates a audiounit.txt file with the list of the names of the audiounits.
    """
    if not os.path.exists(aupresets_dir):
        os.mkdir(aupresets_dir)
        
    info_file = open(os.path.join(aupresets_dir, 'audiounit.txt'), 'w')
    
    dir = aupresets_dir   
    aus = [host.tracks[0].synth] + host.tracks[0].effects
    for au in aus:
        if au.bypass == False:
            file_path = os.path.join(dir, au.name + '.aupreset')
            info_file.write('%s\n' % au.name)
            au.save_aupreset(file_path)
            
    # something special for kontakt 3
    # we need to save the path to the original .aupreset somewhere
    synth = host.tracks[0].synth
    if synth.name.lower() == 'kontakt 3':
        with open(os.path.join(aupresets_dir, 'kontakt3_original_preset.txt'),'w') as f:
            f.write(synth._last_aupreset)
                
def load_aupresets(aupresets_dir, host=None):
    """ Loads the .aupresets in 'aupresets_dir' back into the (single) track of the 'host'.
        The names of the .aupresets in the 'aupresets_dir' must match an audio unit of 'host'
        If there are effects in `host` that doesn't have a corresponding .aupreset, their bypass setting
        will be set to True.
        
        If the ``host`` is None, we will create it and use what is in audiounit.txt to create the audio units.
        In that case we will return the host. If it was supplied we won't.
    """
    # building the track if it was not already there
    host_was_none = False
    if host is None:
        host_was_none = True
        host = Host()
        info_file = open(os.path.join(aupresets_dir, 'audiounit.txt'))
        names = [l.strip('\n') for l in info_file.readlines()]
        t = host.add_track(names[0])
        for e in names[1:]:
            t.add_effect(e)
            
    # loading the .aupresets
    dir = aupresets_dir   
    aus = [host.tracks[0].synth] + host.tracks[0].effects
    for au in aus:
        file_path = os.path.join(dir, au.name + '.aupreset')
        if os.path.exists(file_path):
            au.load_aupreset(file_path)
            au.bypass = False
        else:
            au.bypass = True  
            
    if host_was_none:
        return host
            
    
        
def generate_data(host, randomizers=None):
    """ Returns an array of data for the "synth+effects" instrument in the (single) track of 'host'
        host : The host containing a track with a synth and the effects
        randomizers : A list of the randomizers for the synth/effects. Passed for speed up purposes, so we don't initialize them again.
        Must match the synth and effects in 'host'
    """
    
    if randomizers is None:
        randomizers = get_track_randomizers(host)

    data = N.hstack( ([r.get_parameters() for r in randomizers]) )

    return data
    
    
def load_data(data, host, randomizers=None):
    """ The opposite of generate data. Starts from the numpy array of 'data'
        and sets the params of the audio units of the 'host' with it.
        See generate_data for the parameters, those are the same.
    """
    
    if randomizers is None:
        randomizers = get_track_randomizers(host)

    for r in randomizers:
        n = r.get_parameters().shape[0]
        r.set_parameters(data[:n])
        data = data[n:]
    if len(data) != 0:
        log.warning('Something must certainly have gone wrong in load_data(...)')
    

    
