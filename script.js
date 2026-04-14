function vote(candidate) {
    fetch('http://127.0.0.1:5000/vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ candidate: candidate })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    });
}