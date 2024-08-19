var fullUrl = window.location.href
let a = document.querySelector('.alolo')
let b = document.querySelector('.container-section')
let c = document.querySelector('.header')
let d = document.querySelector('.nav')
let g = document.querySelector('.register button')
if (fullUrl == 'http://127.0.0.1:8000/news/index_new/' || fullUrl != 'http://127.0.0.1:8000/news/'){
    a.style.display = 'none'
    b.style.display = 'none'
    c.style.padding = '10px 20px 10px 0px'
    d.style.width = "699px"
    d.style.height = "16px"
    g.style.padding = "3px 10px"
    g.style.border = "3px solid"
    g.style.color = "#FF7B01"
    g.style.backgroundColor = 'white'
}else {
    a.style.display = 'flex'
    g.style.color = "white"
    d.style.width = "395px"
    b.style.display = 'flex'
    g.style.backgroundColor = '#FF8C00'
    d.style.heigth = "34px"
    g.style.border = "none"
    g.style.padding = "10px 20px"
    c.style.padding = '10px 20px 10px 0px'
}

