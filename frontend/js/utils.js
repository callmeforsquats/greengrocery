const header=document.querySelector('header')
window.addEventListener('scroll',(event)=>{
    if (window.scrollY>50){
        header.classList.add(['active'])
    }else{
        header.classList.remove(['active'])
    }
})



const name = document.querySelector('.adding .item h3')
const nameInput=document.querySelector('.adding form input[type=text]')
nameInput.addEventListener('input',(event)=>{
    let value=""
    if (event.target.value){
        value=event.target.value
    }else{
        value="bread"
    }
    name.innerText=value
})

const price = document.querySelector('.adding .item .price')
const priceInput=document.querySelector('.adding form input[type=number]')
priceInput.addEventListener('input',(event)=>{
    let value=""
    if (event.target.value){
        value='$'+event.target.value
    }else{
        value='$100'
    }
    price.innerText=value
})

const description = document.querySelector('.adding .item h3+p')
const descriptionInput = document.querySelector('.adding form textarea')
descriptionInput.addEventListener('input',(event)=>{
    let value=""
    if (event.target.value){
        value=event.target.value
    }else{
        value="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Corrupti est, harum id amet maiores ea tenetur, dolore quasi recusandae quo excepturi possimus voluptatem quod. Explicabo numquam tempora quia quis? Laudantium"
    }
    description.innerText=value
})

const picture = document.querySelector('.adding .item img')
const fileInput = document.querySelector('input[type=file]')
fileInput.addEventListener('input',(event)=>{
    let file = event.target.files[0] 
    let span = event.target.parentElement.querySelector('span')
    span.innerText=file.name
    span.style="text-transform:none"

    picture.file=file;
    let reader = new FileReader()
    reader.onload =( function(f){
        return function (e){
            f.src = e.target.result
        };
    })(picture);
    reader.readAsDataURL(file)
})