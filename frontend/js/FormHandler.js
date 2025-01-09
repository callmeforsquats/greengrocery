import { api_products_urls } from "./urls.js"
function serializeForm(formNode){
    return new FormData(formNode)
}

async function sendProduct(formData){
    let res = await fetch(api_products_urls.add,{
        method:'POST',
        body:formData,
        mode:'cors',
        cache:'no-cache',
        credentials:'same-origin',
        headers:{
            'Content-Type':'application/json'
        }
    })
    let ans = await res.json()
    return ans
}
async function sendPicture(picture,name){
    let formData = new FormData()
    formData.append('picture',picture)
    let res = await fetch(api_products_urls.update_picture_name+name,{
        method:"PATCH",
        body:formData,
        mode:'cors',
    })
    let ans = await res.json()
    return ans
}

export async function handleForm(event) {
    event.preventDefault()
    let data = serializeForm(form)
    let arr = Array.from(data.entries())
    let obj={}
    for (let i =0;i<arr.length-1;++i){
        obj[arr[i][0]]=arr[i][1]
    }
    let json = JSON.stringify(obj)
    let res = await sendProduct(json)
    console.log(res)
    let picture = arr[arr.length-1][1]
    res = await sendPicture(picture,obj.name)
    console.log(res)
}
const form = document.querySelector('.adding form')
form.addEventListener('submit',handleForm)