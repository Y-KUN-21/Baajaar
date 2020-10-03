var update_cart_btn = document.getElementsByClassName('add_cart_btn')

for (var i = 0; i < update_cart_btn.length; i++) {
    update_cart_btn[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action: ', action)

        if (user == 'AnonymousUser') {
            console.log('Unauthenticated user !')
        } else {
            UpdateItem(productId, action)
        }
    })
}

function UpdateItem(productId, action) {
    console.log('Authenticated user! sending query ')
    var url = '/update-item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-csrfToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

    .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data,', data)
            location.reload()
        })


}
