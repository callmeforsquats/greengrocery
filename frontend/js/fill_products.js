import { api_products_urls } from './urls.js'
const url = api_products_urls.all
const item_container = document.querySelector('.menu .item-container')
function fillTemplate(obj){
    let html=`<div class="item">
                <img src="media/${obj.picture}" alt="">
                <h3>${obj.name}</h3>
                <p>
                    ${obj.description}
                </p>
                <p class="price">$${obj.price}</p>
            </div>`
    return html
}
export const fill=async()=>{
    let res = await fetch(url)
    let json = await res.json()
    let html
    for (let i = 0;i<json.length;++i){
        html=fillTemplate(json[i])
        item_container.insertAdjacentHTML('beforeend',html)
    }

}
fill()
import {fun} from './temp.js'
fun('fill_products')