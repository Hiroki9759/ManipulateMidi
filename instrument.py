

import pretty_midi
import os 

midi_data = pretty_midi.PrettyMIDI('American_Idiot.mid')

print midi_data.get_piano_roll()

