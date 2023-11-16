<!DOCTYPE html>
<html>
<head>
    <title>Recommendation System</title>
</head>
<body>
    <h1>Welcome to the Recommendation System!</h1>
    <p>This is a placeholder for the frontend display.</p>
    <?php
    // PHP code to interact with the API and display results
    // Example:
    $api_endpoint = 'http://api:5000/ratings_distribution';
    $data = file_get_contents($api_endpoint);
    $ratings_distribution = json_decode($data, true);

    // Process and display the ratings distribution data
    // Example:
    echo '<h2>Ratings Distribution</h2>';
    echo '<pre>';
    print_r($ratings_distribution);
    echo '</pre>';
    ?>
</body>
</html>
