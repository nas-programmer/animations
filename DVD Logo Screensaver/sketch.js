let x, y, velX, velY

let r, g, b

function preload() {
    img = loadImage("dvd_logo.png")
}


function setup() {
    createCanvas(window.innerWidth, window.innerHeight)
    x = random(100, window.innerWidth - img.width * 2)
    y = random(50, window.innerHeight - img.height * 2)
    velX = 5
    velY = 5
    colorchange()
}

function colorchange() {
    r = random(255)
    g = random(255)
    b = random(255)
}


function draw() {
    background(171, 251, 209)
    tint(r, g, b)
    image(img, x, y)

    x += velX
    y += velY

    if (x <= 0 || x + img.width >= window.innerWidth) {
        velX = -velX
        colorchange()
    }
    if (y <= 0 || y + img.height >= window.innerHeight) {
        velY = -velY

    }

}