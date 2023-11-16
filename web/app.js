const express = require('express');
const axios = require('axios');
const app = express();

app.get('/ratings', async (req, res) => {
    try {
        const response = await axios.get('http://api:5000/api/ratings');
        const data = response.data;
        res.send(renderData('Ratings', data));
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data');
    }
});

app.get('/top_users', async (req, res) => {
    try {
        const response = await axios.get('http://api:5000/api/top_users');
        const data = response.data;
        res.send(renderData('Top 10 Users by Ratings', data));
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data');
    }
});

app.get('/top_rated_users', async (req, res) => {
    try {
        const response = await axios.get('http://api:5000/api/top_rated_users');
        const data = response.data;
        res.send(renderData('Top 10 Users by Number of Ratings', data));
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data');
    }
});

function renderData(label, data) {
    let output = `<h1 style="color: #465615; font-size: 24px; text-align: center; margin-top: 50px; border-bottom: 2px solid #A4CB2F;">${label}</h1>`;
    if (data && data.length > 0) {
        output += `
            <table style="border-collapse: collapse; width: 60%; margin: 0 auto; border: 1px solid #ddd; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <thead style="background-color: #A4CB2F;">
                    <tr>
                        <th style="padding: 12px; text-align: left;">User ID</th>
                        <th style="padding: 12px; text-align: left;">Rating</th>
                    </tr>
                </thead>
                <tbody>`;
        data.forEach(item => {
            if (item.userId) {
                output += `
                    <tr style="border-bottom: 1px solid #ddd;">
                        <td style="padding: 8px;">${item.userId}</td>
                        <td style="padding: 8px;">${item.rating}</td>
                    </tr>`;
            } else {
                // Handle other types of data according to the consumed API
                // ...
            }
        });
        output += `
                </tbody>
            </table>`;
    } else {
        output += '<p style="color: #777; text-align: center;">No data available.</p>';
    }
    return output;
}

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
