from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    html_content = """"""
                <html>
                <head>
                <style>
                        body { 
                            background-color: black;  
                            color: white;
                            font-family: 'Bangers', sans-serif;
                            margin: 0;
                            padding: 0;
                        }

                        .navbar {
                            position: fixed;
                            top: 0;
                            left: 0;
                            width: 100%;
                            background-color: rgba(34, 34, 34, 0.9); 
                            padding: 10px 0;
                            display: flex;
                            justify-content: center;
                            z-index: 1000;
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
                            font-family: Georgia; /* デフォルトのフォントに変更 */
                        }

                        .navbar a {
                            color: white;
                            text-decoration: none;
                            padding: 14px 30px;
                            font-size: 18px;
                            font-weight: bold;
                            transition: background 0.3s;
                            border-radius: 5px;
                        }

                        .navbar a:hover {
                            background-color: rgba(255, 255, 255, 0.1);
                        }
                    </style>

                    <link href="https://fonts.googleapis.com/css2?family=Bangers&display=swap" rel="stylesheet">
                    <style>
                        body { 
                            background-color: black;  
                            color: white;
                            font-family: 'Bangers', sans-serif;
                            margin: 0;
                            padding: 0;
                        }

                        .navbar {
                            position: fixed;
                            top: 0;
                            left: 0;
                            width: 100%;
                            background-color: rgba(34, 34, 34, 0.9); 
                            padding: 10px 0;
                            display: flex;
                            justify-content: center;
                            z-index: 1000;
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
                        }

                        .navbar a {
                            color: white;
                            text-decoration: none;
                            padding: 14px 30px;
                            font-size: 18px;
                            font-weight: bold;
                            transition: background 0.3s;
                            border-radius: 5px;
                        }

                        .navbar a:hover {
                            background-color: rgba(255, 255, 255, 0.1);
                        }

                        .hero-section {
                            text-align: center;
                            padding: 100px 20px;
                            position: relative;
                            z-index: 10;
                        }

                        .hero-section h1 {
                            font-size: 60px;
                            margin-bottom: 20px;
                        }

                        .hero-section p {
                            font-size: 24px;
                            margin-bottom: 40px;
                        }

                        .container {
                            position: relative;
                            display: flex;
                            margin-left: 40px;  
                            bottom: 130px;
                        }

                        .gif-container {
                            position: relative;
                            width: 100%;  
                            height: 480px;
                            overflow: hidden;
                            margin-right: 20px;  
                        }

                        .gif-background {
                            width: 100%;  
                            height: 125%;  
                            object-fit: cover;
                            opacity: 0.7;
                            margin-top: 68px;
                        }

                        .gif-overlay-image {
                            position: absolute;
                            top: 10%;
                            left: 30%;
                            transform: translate(-50%, -50%);
                            width: 500px;
                            height: auto;
                            z-index: 10;
                        }

                        .text-container {
                            position: absolute;
                            top: 30%;
                            left: 50%;
                            transform: translateX(-50%);
                            font-size: 50px;
                            font-weight: bold;
                            color: rgba(255, 255, 255, 0.9);
                        }

                        .text-second {
                            position: absolute;
                            top: 45%;
                            left: 50%;
                            transform: translateX(-50%);
                            font-size: 32px;
                            font-weight: bold;
                            color: rgba(255, 255, 255, 0.9);
                        }
                            /* Poppinsフォントのボタン */
                    .center-button {
                        position: absolute;
                        top: 75%;  /* 真ん中に配置 */
                        left: 50%;
                        transform: translate(-50%, -50%);
                        padding: 15px 25px;
                        font-size: 20px;
                        font-family: 'Poppins', sans-serif;
                        font-weight: 600;
                        background-color: rgba(255, 140, 0, 0.8);  /* 濃いオレンジ色で透明度を少し加える */
                        color: white;
                        border: none;
                        border-radius: 1px;
                        cursor: pointer;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        transition: background-color 0.3s ease, transform 0.3s ease;
                    }
                    }
                    .image-button {
                        position: relative;
                        display: inline-flex;
                        align-items: center; /* 画像とテキストを垂直中央揃え */
                        padding: 10px 20px;
                        background-color: rgba(255, 140, 0, 0.8);
                        color: white;
                        border: none;
                        border-radius: 5px;
                        font-size: 18px;
                        font-weight: bold;
                        cursor: pointer;
                        text-transform: uppercase;
                    }
                    .image-buttons {
                        position: absolute;
                        right: 60px;  /* 右から50pxの位置に配置 */
                        top: 75%;  /* 垂直中央に配置 */
                        transform: translateY(-50%);  /* 垂直方向で真ん中に調整 */
                        display: flex;
                        display: flex;  /* 画像ボタンを横に並べる */
                        flex-direction: row;  /* 横並び */
                        gap: 50px;  /* 画像の間隔 */
                        align-items: center;
                        margin-top: 20px; /* スクロールして到達する位置 */
                        }
                        .image-buttons img {
                            background-color: transparent;  /* 背景を透明にする */
                            cursor: pointer;  /* クリック可能に */
                            width: 150px;  /* サイズ調整 */
                            transition: transform 0.5s;  /* ホバー時のアニメーション */
                        }

                        .image-buttons img:hover {
                            transform: scale(1.1);  /* ホバー時に画像が少し拡大 */
                        }
                        .image-buttons img:hover {
                            transform: scale(1.1);
                        }
                        .hidden {
                            opacity: 0;
                            transform: translateY(20px);
                            transition: opacity 0.5s ease-out, transform 0.5s ease-out;
                        }
                        .visible {
                            opacity: 1;
                            transform: translateY(0);
                        }

                    </style>
                </head>
                <body>
                    <!-- 一番上のGIF -->
                    <div class="gif-container">
                        <img src="https://cdn.discordapp.com/attachments/1010395994841690134/1354879788572999720/120410702_p0_master1200.jpg?ex=6801ec62&is=68009ae2&hm=545879f7811d4d2fda287c1502b6b94e42da3af6a29ef3ee94bee91b700c66ad&" alt="jpg" class="gif-background">
                        <div class="text-container">O v e r w a t c h  2</div>
                        <div class="text-second">世界はヒーローを求めている！</div>
                        <button class="center-button" onclick="window.open('https://overwatch.blizzard.com/ja-jp/', '_blank')">今すぐプレイ</button>
                    </div>

                    <div class="navbar">
                        <a href="/">Home</a>
                        <a href="/game">Game</a>
                        <a href="https://discord.gg/dhKYX8WHYH" target="_blank">Discord</a>
                        <a href="https://open.spotify.com/user/31yjllbc5vbdqj7lfehodkudugky?si=2c321d3a17474270" target="_blank">Spotify</a>
                        <a href="/anime">Anime</a>
                    </div>
                    
                    <div class="hero-section">
                    </div>
                    <div class="image-buttons hidden">
                        <a href="https://discord.gg/dhKYX8WHYH" target="_blank">
                            <img src="https://i.pinimg.com/736x/a8/d9/c1/a8d9c185c09e91b9566e57ba3b6e2f8c.jpg" alt="ボタン1" class="image-btn">
                        </a>
                        <a href="https://open.spotify.com/user/31yjllbc5vbdqj7lfehodkudugky?si=2c321d3a17474270" target="_blank">
                            <img src="https://i.pinimg.com/736x/df/1e/40/df1e40b09dc11197908b22051b9ba94a.jpg" alt="ボタン2" class="image-btn">
                        </a>
                        <a href="https://www.youtube.com/channel/UCN6uj8hVdc6SHHt9bbBGsFQ" target="_blank">
                            <img src="https://i.pinimg.com/736x/7a/c8/17/7ac81782631c4f28812a834fade2d146.jpg" alt="ボタン3" class="image-btn">
                        </a>
                        <a href="https://www.instagram.com/latte223._/" target="_blank">
                            <img src="https://i.pinimg.com/736x/64/dc/0f/64dc0fb472958830de717bbc928b817c.jpg" alt="ボタン4" class="image-btn">
                        </a>
                    </div>
                    <script>
                        document.addEventListener("DOMContentLoaded", function() {
                            const observer = new IntersectionObserver(entries => {
                                entries.forEach(entry => {
                                    if (entry.isIntersecting) {
                                        entry.target.classList.add("visible");
                                    }
                                });
                            }, { threshold: 0.1 });
                            observer.observe(document.querySelector(".image-buttons"));
                        });
                    </script>

                <style>
                    .bottom-right-buttons {
                        position: fixed;
                        bottom: 20px;
                        right: 20px;
                        display: flex;
                    flex-direction: column;
                        gap: 10px;
                    }

                    .bottom-right-buttons button {
                        padding: 10px 20px;
                        font-size: 16px;
                        font-weight: bold;
                        background-color: rgba(255, 140, 0, 0.8);
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        transition: background 0.3s ease;
                    }

                    .bottom-right-buttons button:hover {
                        background-color: rgba(255, 100, 0, 0.9);
                    }
                </style>
                </body>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latte web</title>
    <style>
        /* ボタンスタイル */
        .gif-button {
            position: absolute; /* 追加：絶対位置 */
            left: 20px; /* 左から50px */
            top: 520px;  /* 上から400px（ボタンを下に移動） */
            display: inline-block;
            width: 1000px; /* ボタンの幅 */
            height: 500px; /* ボタンの高さを調整（下にスペースを作る） */
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            background-color: rgba(0, 0, 0, 0.5);
            text-align: center;
            transition: transform 0.3s ease;
            z-index: 10; /* 他の要素より手前に表示 */
        }

        .gif-button img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* ボタン上にマウスを乗せたときの効果 */
        .gif-button:hover {
            transform: scale(1.05);
        }

        /* 説明文のスタイル */
        .gif-button .description {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            font-size: 18px;
            font-weight: bold;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
        }

        /* 黒い画像のスタイル */
        .black-image {
            position: absolute;
            left: 50px; /* 左から50px */
            top: 1030px; /* 上から1050px（ボタン下から50px） */
            width: 1000px; /* 画像の幅 */
            height: 50px; /* 画像の高さ */
            background-color: black; /* 黒い画像 */
        }
    </style>
</head>
<body>
    <!-- 2枚目のGIFを巨大なボタンとして埋め込み、説明文を追加 -->
    <div class="gif-button" id="draggableButton" onclick="window.open('https://overwatch.blizzard.com/ja-jp/heroes/kiriko/', '_blank')">
        <img src="https://i.pinimg.com/originals/25/c6/9d/25c69d9860a170abaa532cadb4c7cdb9.gif" alt="GIF">
        <div class="description">I　L O V E　L I O N 💗</div>
    </div>

    <!-- 黒い画像を追加 -->
    <div class="black-image"></div>

    <script>
        const gifButton = document.getElementById('draggableButton');
        
        let isDragging = false;
        let offsetX, offsetY;

        gifButton.addEventListener('mousedown', function(event) {
            if (event.button === 0) { // 0は左クリック
                isDragging = true;
                offsetX = event.clientX - gifButton.getBoundingClientRect().left;
                offsetY = event.clientY - gifButton.getBoundingClientRect().top;
                document.addEventListener('mousemove', drag);
                document.addEventListener('mouseup', stopDrag);
            }
        });

        function drag(event) {
            if (isDragging) {
                gifButton.style.left = (event.clientX - offsetX) + 'px';
                gifButton.style.top = (event.clientY - offsetY) + 'px';
            }
        }

        function stopDrag() {
            isDragging = false;
            document.removeEventListener('mousemove', drag);
            document.removeEventListener('mouseup', stopDrag);
        }
    </script>
</body>
</html>
            """"""
    return Response(html_content, content_type='text/html; charset=utf-8')

@app.route("/game")
def game():
    html_content = """"""
                <html lang="ja">
                <head>
                    <style>
                        body { 
                            background-color: black;  
                            color: white;
                            font-family: 'Arial', sans-serif;
                            margin: 0;
                            padding: 0;
                        }

                        .navbar {
                            position: fixed;
                            top: 0;
                            left: 0;
                            width: 100%;
                            background-color: rgba(34, 34, 34, 0.9); 
                            padding: 10px 0;
                            display: flex;
                            justify-content: center;
                            z-index: 1000;
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
                        }

                        .navbar a {
                            color: white;
                            text-decoration: none;
                            padding: 14px 30px;
                            font-size: 18px;
                            font-weight: bold;
                            transition: background 0.3s;
                            border-radius: 5px;
                        }

                        .navbar a:hover {
                            background-color: rgba(255, 255, 255, 0.1);
                        }

                        .hero-section {
                            text-align: center;
                            padding: 100px 20px;
                            position: relative;
                            z-index: 10;
                        }

                        .hero-section h1 {
                            font-size: 60px;
                            margin-bottom: 20px;
                        }

                        .hero-section p {
                            font-size: 24px;
                            margin-bottom: 40px;
                        }

                        .container {
                            position: relative;
                            display: inline-block;
                            margin-top: 50px;
                        }

                        .overlay-text {
                            position: absolute;
                            top: 30%;
                            left: 50%;
                            transform: translateX(-50%);
                            font-size: 32px;
                            font-weight: bold;
                            color: rgba(255, 255, 255, 0.9);
                            font-family: 'Raleway', sans-serif;
                        }
                    </style>
                    <head>
                        <style>
                            body {
                                font-family: 'Georgia', serif;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="navbar">
                            <a href="/">Home</a>
                            <a href="/game">Game</a>
                            <a href="https://discord.gg/dhKYX8WHYH" target="_blank">Discord</a>
                            <a href="https://open.spotify.com/user/31yjllbc5vbdqj7lfehodkudugky?si=2c321d3a17474270" target="_blank">Spotify</a>
                            <a href="/anime">Anime</a>
                        </div>
    
                    </body>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>gaem</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #000;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      overflow: hidden;
      flex-direction: column;
      transition: background-color 0.5s, color 0.5s;
    }
    #gameContainer {
      position: relative;
    }
    #gameCanvas {
      display: block;
      background-color: #000;
      border: 2px solid #fff;
      transition: background-color 0.5s, border-color 0.5s;
    }
    #score {
      position: absolute;
      bottom: -40px;
      left: 50%;
      font-family: Arial, sans-serif;
      transform: translateX(-50%);
      font-size: 20px;
      z-index: 10;
    }
    #lives {
      position: absolute;
      top: 10px;
      right: 10px;
      font-size: 20px;
      z-index: 10;
    }
    #restartButton, #startButton {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      padding: 10px 20px;
      font-size: 20px;
      background-color: #f00;
      color: #fff;
      border: none;
      cursor: pointer;
      z-index: 20;
    }
    #startButton {
      top: 50%;
    }
  </style>
</head>
<body>
  <div id="gameContainer">
    <canvas id="gameCanvas" width="600" height="150"></canvas>
    <div id="score">スコア: 0</div>
    <div id="lives">❤️❤️❤️</div>
    <button id="restartButton" style="display:none;">リスタート</button>
    <button id="startButton">スタート</button>
  </div>

  <script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    let dino = {
      x: 50,
      y: 120,
      width: 20,
      height: 30,
      speed: 0,
      gravity: 0.6,
      jumpPower: -10,
      isJumping: false
    };

    let obstacles = [];
    let score = 0;
    let lives = 3;
    let gameOver = false;
    let colorInverted = false;
    let steps = 0;

    function drawDino() {
      ctx.fillStyle = colorInverted ? "#000" : "#fff";
      ctx.fillRect(dino.x, dino.y, dino.width, dino.height);
    }

    function generateObstacle() {
      const obstacle = {
        x: canvas.width,
        y: 120,
        width: 20 + Math.random() * 30,
        height: 30 + Math.random() * 40,
        speed: 4
      };
      obstacles.push(obstacle);
    }

    function moveObstacles() {
      obstacles.forEach((obstacle, index) => {
        obstacle.x -= obstacle.speed;
        if (obstacle.x + obstacle.width < 0) {
          obstacles.splice(index, 1);
          score += 10;
        }
      });
      steps++;
      if (steps % 3 === 0) {
        score++;
      }

      if (score >= 2500 && score % 1000 === 0) {
        colorInverted = !colorInverted;
      }
    }

    function drawObstacles() {
      ctx.fillStyle = colorInverted ? "#000" : "#fff";
      obstacles.forEach(obstacle => {
        ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
      });
    }

    function jump() {
      if (!dino.isJumping) {
        dino.isJumping = true;
        dino.speed = dino.jumpPower;
      }
    }

    function updateLives() {
      document.getElementById('lives').textContent = '❤️'.repeat(lives);
    }

    function update() {
      if (gameOver) return;

      document.body.style.backgroundColor = colorInverted ? "#fff" : "#000";
      document.body.style.color = colorInverted ? "#000" : "#fff";
      canvas.style.backgroundColor = colorInverted ? "#fff" : "#000";
      canvas.style.borderColor = colorInverted ? "#000" : "#fff";

      ctx.clearRect(0, 0, canvas.width, canvas.height);

      if (dino.isJumping) {
        dino.y += dino.speed;
        dino.speed += dino.gravity;
      }

      if (dino.y > 120) {
        dino.y = 120;
        dino.isJumping = false;
        dino.speed = 0;
      }

      moveObstacles();
      drawDino();
      drawObstacles();

      obstacles.forEach(obstacle => {
        if (dino.x < obstacle.x + obstacle.width && dino.x + dino.width > obstacle.x && dino.y < obstacle.y + obstacle.height && dino.y + dino.height > obstacle.y) {
          lives--;
          updateLives();
          obstacles.splice(obstacles.indexOf(obstacle), 1);

          if (lives <= 0) {
            gameOver = true;
            document.getElementById("restartButton").style.display = 'inline';
          }
        }
      });

      document.getElementById("score").textContent = `スコア: ${score}`;

      requestAnimationFrame(update);
    }

    function resetGame() {
      dino.x = 50;
      dino.y = 120;
      dino.speed = 0;
      dino.isJumping = false;
      score = 0;
      steps = 0;
      lives = 3;
      obstacles = [];
      gameOver = false;
      colorInverted = false;
      updateLives();
      document.getElementById("score").textContent = `スコア: ${score}`;
      document.getElementById("restartButton").style.display = 'none';
      update();
    }

    function startGame() {
      document.getElementById("startButton").style.display = 'none';
      update();
    }

    window.addEventListener("keydown", function(event) {
      if (event.key === " ") {
        jump();
      }
    });

    document.getElementById("restartButton").addEventListener("click", function() {
      resetGame();
    });

    document.getElementById("startButton").addEventListener("click", function() {
      startGame();
    });

    setInterval(generateObstacle, 2000);
    updateLives();
  </script>
</body>
</html>
    """"""
    return Response(html_content, content_type='text/html; charset=utf-8')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
