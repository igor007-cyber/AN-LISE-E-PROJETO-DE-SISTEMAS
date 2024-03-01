// MusicPlayer com padrão Observer
class MusicPlayer {
    constructor() {
        this.observers = [];
        this.state = { song: 'Nenhuma', playing: false, playlist: [] };
    }

    addObserver(observer) {
        this.observers.push(observer);
    }

    removeObserver(observer) {
        const index = this.observers.indexOf(observer);
        if (index > -1) {
            this.observers.splice(index, 1);
        }
    }

    notifyObservers() {
        for (const observer of this.observers) {
            observer.update(this.state);
        }
    }

    play(song) {
        this.state = { song: song, playing: true, playlist: this.state.playlist };
        this.notifyObservers();
    }

    stop() {
        this.state = { song: 'Nenhuma', playing: false, playlist: this.state.playlist };
        this.notifyObservers();
    }

    proximo() {
        const currentSongIndex = this.state.playlist.indexOf(this.state.song);
        const ProximaMusicaIndex = (currentSongIndex + 1) % this.state.playlist.length;
        const ProximaMusica = this.state.playlist[ProximaMusicaIndex];
        this.play(ProximaMusica);
    }

    AdicionarMusica(song) { 
        this.state.playlist.push(song);
        this.notifyObservers();
    }
}

// Display implementa Observer para atualizar a interface do usuário
class Display {
    constructor(displayElement, playlistElement) {
        this.displayElement = displayElement;
        this.playlistElement = playlistElement;
    }

    update(state) {
        if (state.playing) {
            this.displayElement.innerHTML = `Tocando agora: ${state.song}`;
        } else {
            this.displayElement.innerHTML = "Música atual: Nenhuma";
        }

        // Atualizar a lista de reprodução
        this.playlistElement.innerHTML = state.playlist.map(song => `<li>${song}</li>`).join('');
    }
}

// Código "cliente" que usa as classes
// Instanciando o player e o display
const player = new MusicPlayer();
const display = new Display(document.getElementById('musicDisplay'), document.getElementById('playlist'));
player.addObserver(display);

// Configurando os listeners dos botões
document.getElementById('playButton').addEventListener('click', function() {
    player.play('Fear of the Dark - Iron Maiden');
});

document.getElementById('stopButton').addEventListener('click', function() {
    player.stop();
});

document.getElementById('ProximoButton').addEventListener('click', function() {
    player.proximo();
});

document.getElementById('AdicionarButton').addEventListener('click', function() {
    const newSong = prompt('Digite o nome da nova música:');
    if (newSong) {
        player.AdicionarMusica(newSong);
    }
});
