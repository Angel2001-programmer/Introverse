const express = require('express');
const router = express.Router();
const db = require('./db');
const suggestionsData = require('./suggestionsData'); 

router.get('/:tablename/:genre', (req, res) => {
    const { tablename, genre } = req.params;

    const query = `SELECT * FROM ${tablename} WHERE ${tablename}_genre = ?`;

    db.query(query, [genre], (err, results) => {
        if (err) {
            console.error(`Error fetching ${tablename} suggestions for ${genre}:`, err);
            res.status(500).json({ error: `Error fetching ${tablename} suggestions for ${genre}` });
            return;
        }

        const mergedResults = results.map(result => {
            const title = result[`${tablename}_Title`]; // Get the title from the fetched results
            const matchingSuggestion = suggestionsData[tablename][genre].find(suggestion => suggestion.title === title);

            if (matchingSuggestion) {
                return {
                    ...result,
                    image: matchingSuggestion.image 
                };
            }
            return result; 
        });

        res.json(mergedResults);
    });
});

// export default router;
module.exports = router;
