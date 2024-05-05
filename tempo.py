import librosa

def quantify_tempo(soundtrack_path, hop_length=512):
    # Load the audio file
    y, sr = librosa.load(soundtrack_path, sr=None)
    
    # Estimate tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)
    
    return tempo
    
    return tempo

# Example usage:
soundtrack_path = "D:\\vs_code\\DL\\proj\\resources\\audio_files\\mp3\\Rachel_Platten_-_Fight_Song_CeeNaija.com_.mp3"  
tempo = quantify_tempo(soundtrack_path)
print("Tempo:", tempo, "BPM")
