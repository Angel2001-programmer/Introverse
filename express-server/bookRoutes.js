const express = require('express');
const router = express.Router();
const connection = require('./db');
const handleDatabaseErrors  = require('./errorHandling').default;

router.get('/', (req, res) => {
    console.log('Fetching books from the database...');
    connection.query('SELECT * FROM Books', (err, results) => {
        if (err) {
            console.error('Error querying MySQL - Books: Please check your query.', err);
            res.status(500).json({ error: 'Error querying MySQL Books' });
            return;
        }
        if (results.length === 0) {
            console.log('No books found in the database.');
        } else {
            console.log('Books fetched successfully.');
        }
        res.json(results);
    });
});

module.exports = { router, connection, handleDatabaseErrors };
