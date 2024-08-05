import vlc
import time

# Ruta del archivo de video
video_path = "ruta/al/video.mp4"

# Crear una instancia del reproductor VLC
player = vlc.MediaPlayer(video_path)

# Función para reproducir video en loop
def play_in_loop():
    while True:
        # Comenzar la reproducción del video
        player.play()

        # Esperar hasta que el video termine
        time.sleep(player.get_length() / 1000)

        # Reiniciar el video
        player.stop()
        player.set_media(vlc.Media(video_path))

# Llamar a la función para reproducir en loop
play_in_loop()
