//REST API demo in Node.js
let express = require('express'); // requre the express framework
let app = express();
let fs = require('fs'); //require file system object

// Endpoint to Get a list of genres
app.get('/getGames', function(req, res){
    fs.readFile(__dirname + "/" + "games.json", 'utf8', function(err, data){
        console.log(data);
        res.end(data); // you can also use res.send()
    });
})

// Endpoint to Get a list of genres
app.get('/getAnime', function(req, res){
    fs.readFile(__dirname + "/" + "anime.json", 'utf8', function(err, data){
        console.log(data);
        res.end(data); // you can also use res.send()
    });
})

// Endpoint to Get a list of genres
app.get('/getBooks', function(req, res){
    fs.readFile(__dirname + "/" + "books.json", 'utf8', function(err, data){
        console.log(data);
        res.end(data); // you can also use res.send()
    });
})

// Create a server to listen at port 8080
let server = app.listen(8080, function(){
    let host = server.address().address
    let port = server.address().port
    console.log("REST API demo app listening at http://localhost:8080")
})