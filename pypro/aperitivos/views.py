from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 288344114},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 876176372},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
