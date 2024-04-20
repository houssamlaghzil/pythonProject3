import usb.core
import time
import simpleaudio as sa


# Trouver le périphérique NFC
def trouver_peripherique_nfc():
    dev = usb.core.find(idVendor=0x072f, idProduct=0x2200)  # ID du périphérique NFC
    if dev is None:
        raise ValueError("Périphérique NFC non trouvé.")
    return dev


# Vérifier si la carte NFC est détectée
def detecter_nfc(dev):
    if dev.ctrl_transfer(0xC0, 0xFF, 0x3700, 0x0000, 6) == [0x06, 0x75, 0x77, 0x88, 0x99,
                                                            0xAA]:  # Vérifier l'état de la carte NFC
        print("Carte NFC détectée !")
        jouer_musique()


# Fonction pour jouer la musique
def jouer_musique():
    wave_obj = sa.WaveObject.from_wave_file("votre_musique.wav")  # Charger la musique
    play_obj = wave_obj.play()  # Jouer la musique


# Boucle principale pour détecter la carte NFC en continu
def boucle_detection_nfc(dev):
    while True:
        detecter_nfc(dev)
        time.sleep(1)


# Fonction principale
def main():
    dev = trouver_peripherique_nfc()
    boucle_detection_nfc(dev)


if __name__ == "__main__":
    main()
