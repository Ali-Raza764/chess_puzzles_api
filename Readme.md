# Puzzle API

This is a Flask-based API for retrieving puzzle data. The API supports filtering and pagination, and it includes caching for better performance.

## Endpoints

### GET /puzzles

Retrieve a list of puzzles with optional filters and pagination.

#### Query Parameters:

- **start** (integer, default: 0) - The starting index for pagination.
- **limit** (integer, default: 10) - The number of puzzles to return.
- **min_rating** (integer, default: 0) - The minimum rating to filter puzzles.
- **max_rating** (integer, default: 3000) - The maximum rating to filter puzzles.
- **themes** (string) - A comma-separated list of themes to filter puzzles.

#### Example Request:
```plaintext
GET /puzzles?start=0&limit=10&min_rating=1000&max_rating=2000&themes=adventure,logic
```

### GET /puzzle

Retrieve a puzzle by its ID.

#### Query Parameters:

- **puzzle_id** (string) - The ID of the puzzle to retrieve.

#### Example Request:
```plaintext
GET /puzzle?puzzle_id=12345
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-Caching
- pandas

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Ensure you have a `puzzles.csv` file in the root directory of your project.

### Running the App

1. Run the Flask app:
   ```sh
   flask run
   ```

2. Open your browser and go to `http://127.0.0.1:8000` to view the API documentation.

## Deployment

For deployment, you can use services like Heroku, AWS, or any other cloud provider. Ensure you have the necessary environment variables set up and a production-ready server configuration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.