const express = require('express');
const router = express.Router();
const connection = require('./db');
const  handleDatabaseErrors  = require('./errorHandling').default;

router.get('/', (req, res) => {
    console.log('Fetching games from the database...');
    connection.query('SELECT * FROM Games', (err, results) => {
        if (err) {
            console.error('Error querying MySQL - Games: Please check your query.', err);
            res.status(500).json({ error: 'Error querying MySQL Games' });
            return;
        }
        if (results.length === 0) {
            console.log('No games found in the database.');
        } else {
            console.log('Games fetched successfully.');
        }
        res.json(results);
    });
});

module.exports = { router, connection, handleDatabaseErrors };