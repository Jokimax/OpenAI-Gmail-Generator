async function generateEmail(){
    document.getElementById("message").style.color = "white";
    document.getElementById("message").innerHTML = "Loading..."
    response = await fetch("/",
    {        
    method: "POST",
    headers: {
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            subject: document.getElementById("emailPrompt").value
        })
    }).then((response) => {
        if (response.ok) {
          return response.json();
        }
        document.getElementById("message").innerHTML = "An error occured try again!";
        document.getElementById("message").style.color = "red";
        throw new Error('');
      });
    document.getElementById("message").innerHTML = "&#8203;"
    window.open('mailto:jonaxthedreadlord@gmail.com?subject='+response.subject+'&body='+response.text)
}