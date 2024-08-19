var fullUrl = window.location.href
let a = document.querySelector('.alolo')
let b = document.querySelector('.container-section')
let c = document.querySelector('.header')
let d = document.querySelector('.nav')
let g = document.querySelector('.register button')
let v = document.querySelector('.container4')
if (fullUrl == 'http://127.0.0.1:8000/news/index_new/' || fullUrl != 'http://127.0.0.1:8000/news/'){
    a.style.display = 'none'
    b.style.display = 'none'
    c.style.padding = '10px 20px 10px 0px'
    d.style.width = "699px"
    d.style.height = "16px"
}else {
    a.style.display = 'flex'
    d.style.width = "395px"
    b.style.display = 'flex'
    d.style.heigth = "34px"
    c.style.padding = '10px 20px 10px 0px'
}

if (fullUrl === 'http://127.0.0.1:8000/workspace/register/') {
    v.style.marginTop = '147px'
    v.style.marginBottom = '150px'
} else {
    v.style.marginTop = '0px';
    v.style.marginBottom = '0px'
}
