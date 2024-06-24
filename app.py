from flask import Flask, jsonify, request, render_template
import pandas as pd
from flask_caching import Cache

app = Flask(__name__)

# Configure caching
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})

# Load the CSV file with error handling for malformed lines
try:
    df = pd.read_csv('puzzles.csv', on_bad_lines='skip')
    df.set_index('PuzzleId', inplace=True)
except pd.errors.ParserError as e:
    print(f"Error reading the CSV file: {e}")

@app.route('/puzzles', methods=['GET'])
@cache.cached(query_string=True)
def get_puzzles():
    try:
        # Get pagination parameters from query string
        start = request.args.get('start', default=0, type=int)
        limit = request.args.get('limit', default=10, type=int)
        
        # Get filter parameters from query string
        min_rating = request.args.get('min_rating', default=0, type=int)
        max_rating = request.args.get('max_rating', default=3000, type=int)
        themes = request.args.get('themes', default=None, type=str)
        
        # Filter the DataFrame based on rating
        filtered_df = df[(df['Rating'] >= min_rating) & (df['Rating'] <= max_rating)]
        
        # Further filter the DataFrame based on themes if provided
        if themes:
            theme_list = themes.split(',')
            filtered_df = filtered_df[filtered_df['Themes'].apply(lambda x: any(theme in x for theme in theme_list))]
        
        # Apply pagination
        paginated_df = filtered_df.iloc[start:start+limit]
        
        # Convert to dictionary and return as JSON
        puzzles = paginated_df.reset_index().to_dict(orient='records')
        return jsonify(puzzles)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/puzzle', methods=['GET'])
@cache.cached(query_string=True)
def get_puzzle():
    try:
        puzzle_id = request.args.get('puzzle_id', default='', type=str)
        
        # Find the puzzle by ID
        if puzzle_id not in df.index:
            return jsonify({"error": "Puzzle not found"}), 404
        
        puzzle = df.loc[puzzle_id].to_dict()
        return jsonify(puzzle)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def documentation():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
