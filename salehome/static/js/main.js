const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Tắt hộp thông báo sau 3s
setTimeout(function(){
    $('#message').fadeOut('slow');
},3000);
