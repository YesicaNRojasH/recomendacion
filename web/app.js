const express = require('express');
const fetch = require('node-fetch');
const app = express();

app.get('/ratings', async (req, res) => {
    try {
        const response = await fetch('http://api:5000/api/ratings');
        const data = await response.json();
        res.send(renderData('Ratings', data));
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data');
    }
});

app.get('/top_users', async (req, res) => {
    try {
        const response = await fetch('http://api:5000/api/top_users');
        const data = await response.json();
        res.send(renderData('Top 10 Users by Ratings', data));
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data');
    }
});

function renderData(label, data) {
    let output = `<h1>${label}</h1>`;
    if (data && data.length > 0) {
        output += '<ul>';
        data.forEach(item => {
            if (item.userId) {
                output += `<li>User ID: ${item.userId} - Rating: ${item.rating}</li>`;
            } else {
                // Handle other types of data according to the consumed API
                // ...
            }
        });
        output += '</ul>';
    } else {
        output += 'No data available.';
    }
    return output;
}

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
