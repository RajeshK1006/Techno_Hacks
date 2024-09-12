import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x300")
        
        self.playlist = []
        self.current_track = None
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Playlist box
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.playlist_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Buttons
        self.add_button = tk.Button(self.root, text="Add to Playlist", command=self.add_to_playlist)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.remove_button = tk.Button(self.root, text="Remove from Playlist", command=self.remove_from_playlist)
        self.remove_button.pack(side=tk.LEFT, padx=10, pady=5)
        
    def add_to_playlist(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for file in files:
            if file not in self.playlist:
                self.playlist.append(file)
                self.playlist_box.insert(tk.END, os.path.basename(file))
    
    def play_music(self):
        try:
            selection = self.playlist_box.curselection()[0]
            self.current_track = self.playlist[selection]
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play()
        except IndexError:
            messagebox.showwarning("Warning", "No track selected.")
    
    def stop_music(self):
        pygame.mixer.music.stop()
    
    def remove_from_playlist(self):
        try:
            selection = self.playlist_box.curselection()[0]
            self.playlist_box.delete(selection)
            self.playlist.pop(selection)
            if self.current_track and self.current_track in self.playlist:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                self.current_track = None
        except IndexError:
            messagebox.showwarning("Warning", "No track selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
