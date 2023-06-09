// init variables
var canvas = document.querySelector('canvas')
var context = canvas.getContext('2d')
var image = document.getElementById('shibe')
image.style.display = 'none' //hides the image src
var shibeImage 


var newDogeBtn = document.getElementById("newDoge")
newDogeBtn.addEventListener("click", genImage)
var memeText = document.getElementById('changeText').value
var newText = document.getElementById('changeTextButton')
const downloadImage = document.getElementById("downloadImageButton")



// text stylization for the meme
var colorIndex = ['#FF0000' , '#FFFF00' , '#0000FF']
var colorRan = Math.floor(Math.random() * (3))
context.font = "bold 30px Comic Neue"
context.fillStyle = colorIndex[colorRan]

// functions to gen new image from dog.ceo API
function handleLoadImg () {
    context.font = "bold 30px Comic Neue"
    context.drawImage(image, 0, 0, 500, 300)
    image.removeEventListener('load', handleLoadImg)
}

function genImage () {
    $.ajax('https://dog.ceo/api/breed/shiba/images/random').done(function(data) {
    shibeImage = data.message
    image.src=shibeImage
    image.addEventListener('load', handleLoadImg)
})
}

// js to put text on canvas
newText.addEventListener('click', changeMemeText)
newText.addEventListener('click', newColorGen)
downloadImage.addEventListener('click', downloadMeme)

function downloadMeme () {
    var downloadMeme = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
    var link = document.createElement('a');
    link.download = "my-image.png";
    link.href = downloadMeme;
    link.click();
}

function newColorGen () {
    context.fillStyle = colorIndex[Math.floor(Math.random() * (3))]
}

function changeMemeText () {  
    memeText = document.getElementById('changeText').value
    context.fillText(memeText, Math.random() * (100) + 50, Math.random() * (150) + 50) //src txt, x, y
    
}

changeMemeText()