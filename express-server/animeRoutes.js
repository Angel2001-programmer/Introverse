const express = require('express');
const router = express.Router();
const connection = require('./db');
const handleDatabaseErrors  = require('./errorHandling').default;

router.get('/', (req, res) => {
    console.log('Fetching anime from the database...');
    connection.query('SELECT * FROM Anime', (err, results) => {
        if (err) {
            console.error('Error querying MySQL - Anime:', err);
            res.status(500).json({ error: 'Error querying MySQL Anime. Please check your query' });
            return;
        }
        if (results.length === 0) {
            console.log('No anime found in the database.');
        } else {
            console.log('Anime fetched successfully.');
        }
        res.json(results);
    });
});

module.exports = { router, connection, handleDatabaseErrors };