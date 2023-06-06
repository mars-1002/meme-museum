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

// text stylization for the meme
var colorIndex = ['#FF0000' , '#FFFF00' , '#0000FF']
var colorRan = Math.floor(Math.random() * (3 - 0) + 0)
console.log(colorRan)
console.log(colorIndex[colorRan])
// context.fillStyle = 'red'
context.fillStyle = colorIndex[colorRan]
context.font = "bold 30px Comic Neue"

console.log("Hello World")

// functions to gen new image from dog.ceo API
function handleLoadImg (e) {
    context.drawImage(image, 0, 0, 500, 300)
    image.removeEventListener('load', handleLoadImg)
}
function genImage () {
    $.ajax('https://dog.ceo/api/breed/shiba/images/random').done(function(data) {
    console.log(data)
    shibeImage = data.message
    console.log(shibeImage)
    image.src=shibeImage

    image.addEventListener('load', handleLoadImg)
})
}

// js to put text on canvas
newText.addEventListener('click', changeMemeText)
newText.addEventListener('click', newColorGen)

function newColorGen (e) {
    context.fillStyle = colorIndex[Math.floor(Math.random() * (3 - 0) + 0)]
    console.log(context.fillStyle)
}
function changeMemeText (e) {  
    memeText = document.getElementById('changeText').value
    context.fillText(memeText, Math.random() * (425 - 75) + 75, Math.random() * (225 - 75) + 75) //src txt, x, y
}