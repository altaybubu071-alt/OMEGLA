from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# %100 LOGOSUZ - TAM EKRAN - IP ODAKLI TASARIM
HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SISTEM IHLALI</title>
    <style>
        body { background: #000; color: #ff0000; font-family: 'Courier New', monospace; margin: 0; overflow: hidden; height: 100vh; width: 100vw; display: flex; justify-content: center; align-items: center; cursor: crosshair; }
        .warning { text-align: center; z-index: 10; transition: opacity 0.5s; }
        h1 { font-size: 2.2em; letter-spacing: 3px; margin: 10px 0; font-weight: 900; }
        .ip { color: #fff; font-size: 2em; border: 2px solid #ff0000; padding: 15px; display: inline-block; margin: 25px 0; background: rgba(255,0,0,0.1); }
        #video-wrapper { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: none; background: #000; z-index: 100; overflow: hidden; }
        /* YouTube logosunu ve basligini ekrandan disari itmek icin %130 buyutme */
        #player { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 130%; height: 130%; pointer-events: none; }
        .trigger { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 200; cursor: pointer; }
    </style>
</head>
<body>
    <div class="warning" id="screen1">
        <h1>YOU'RE USING OMEGLE</h1>
        <div class="ip">YOUR IP: {{ ip }}</div>
        <h1>YOU'RE HACKED</h1>
        <p style="color: #fff; font-size: 1em; margin-top: 40px; border: 1px solid #fff; padding: 10px;">CLICK TO ABORT SYSTEM OVERRIDE</p>
    </div>
    <div id="video-wrapper"><div id="player"></div></div>
    <div class="trigger" id="go"></div>

    <script src="https://www.youtube.com/iframe_api"></script>
    <script>
        var player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                videoId: 'ttt1ZngeN_A',
                playerVars: { 'autoplay': 0, 'controls': 0, 'showinfo': 0, 'modestbranding': 1, 'rel': 0, 'iv_load_policy': 3, 'playsinline': 1 },
                events: { 'onReady': (e) => { console.log("READY"); } }
            });
        }
        document.getElementById('go').addEventListener('click', function() {
            document.getElementById('screen1').style.display = 'none';
            document.getElementById('video-wrapper').style.display = 'block';
            player.playVideo();
            player.unMute();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    return render_template_string(HTML_KODU, ip=ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
