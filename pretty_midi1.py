import pretty_midi
#midiファイルのロード
midi_data = pretty_midi.PrettyMIDI('example.mid')

#テンポの経験的な予測
print(midi_data.estimate_tempo())

#曲全体での半音の相対的な量を計算する
total_velocity = sum(sum(midi_data.get_chroma()))
print([sum(semitone)/total_velocity for semitone in midi_data.get_chroma()])

#全ての音を５半音上にシフト
for instrument in midi_data.instruments:
    if not instrument.drum:
        for note in instrument.notes:
            note.pitch += 5

#サイン波を使用して、結果のMIDIデータを合成します
audio_data = midi_data.synthesize()