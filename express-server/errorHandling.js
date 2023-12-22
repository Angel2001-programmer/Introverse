function handleDatabaseErrors(res, err, tablename, genre) {
    console.error(`Error fetching ${tablename} suggestions for ${genre}:`, err);
    res.status(500).json({ error: `Error fetching ${tablename} suggestions for ${genre}` });
}

module.exports = {handleDatabaseErrors} ;