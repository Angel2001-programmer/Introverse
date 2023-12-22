const express = require('express');
const app = express();
const PORT = process.env.PORT || 8080;
const cors = require("cors");

const bookRoutes = require('./bookRoutes');
const animeRoutes = require('./animeRoutes');
const gameRoutes = require('./gameRoutes');
const suggestions = require('./suggestions');

app.use('/api/Books', bookRoutes);
app.use('/api/Anime', animeRoutes);
app.use('/api/Games', gameRoutes);
app.use('/api/suggestions', suggestions);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});