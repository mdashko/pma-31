function handlePOST(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  let payload = {
      'name': data.get('cat_name'),
      'age': data.get('cat_age')
  }
  var socket = io();
    socket.on('connect', function () {
        socket.emit('POST', payload);
    });
}

const form = document.getElementById('data_to_post');
form.addEventListener('submit', handlePOST);




function handleGET(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  let payload = {
      'id': data.get('cat_id')
  }
  var socket = io();
    socket.on('connect', function () {
        socket.emit('GET', payload);
    });
}


const form2 = document.getElementById('data_to_get');
form2.addEventListener('submit', handleGET);




function handleDELETE(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  let payload = {
      'id': data.get('cat_id')
  }
  var socket = io();
    socket.on('connect', function () {
        socket.emit('DELETE', payload);
    });
}


const form3 = document.getElementById('data_to_delete');
form3.addEventListener('submit', handleDELETE);




function handlePUT(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  let payload = {
      'id': data.get('cat_id'),
      'name':data.get('cat_name')
  }
  var socket = io();
    socket.on('connect', function () {
        socket.emit('PUT', payload);
    });
}


const form4 = document.getElementById('data_to_put');
form4.addEventListener('submit', handlePUT);