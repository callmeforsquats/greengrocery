const base='http://localhost:5000'
const api_products = '/api/products'
const apb = base+api_products
export const api_products_urls ={
    'add':apb+'/add',
    'all':apb+'/all-products',
    'prod_name':apb+'/product/name/',
    'prod_id':apb+'/product/id/',
    'update_price_name':apb+'/update/product/price/',
    'update_picture_name':apb+'/update/product/picture/',
    'delete_id':apb+'/delete/product/'
}