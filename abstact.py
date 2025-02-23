from abc import ABC,abstractmethod
class madia_player(ABC):
    @abstractmethod
    def play(self): # not have any implemenation
        pass
    
    #CONCRETE METHOD
    def display(self):
        print("i am in media player")
        
class video_player(madia_player):
    def play(self):
        print("playing video")
        
    
class audio_player(madia_player):
    def play1(self):
        print("playing audio")
        
video= video_player()
audio= audio_player()

video.play()
audio.play()

video.display()