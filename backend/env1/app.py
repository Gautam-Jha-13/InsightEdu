from flask import Flask, request, jsonify
import pandas as pd
import xmltodict
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Integer, String, Float, Boolean, DateTime

app = Flask(__name__)

# SQLAlchemy engine (replace with your own database details)
engine = create_engine('mysql://root:Harsh@localhost:3306/AR_portal')

# Define allowed tables to prevent SQL injection (initially allowed tables)
ALLOWED_TABLES = {
    'users': 'users',
    'students': 'students',
    'company_recruitment': 'company_recruitment',
    'expenditure': 'expenditure',
    'admin_login': 'admin_login',
    'placements': 'placements',
    'departments': 'departments',
    'uploads': 'uploads',
    'reports': 'reports',
    'ip_applications': 'ip_applications',
    'projects': 'projects',
    'company_partnerships': 'company_partnerships',
    
    # Add other tables as needed
}

# Helper function to infer SQLAlchemy column types from Pandas dtypes
def infer_column_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return Integer
    elif pd.api.types.is_float_dtype(dtype):
        return Float
    elif pd.api.types.is_bool_dtype(dtype):
        return Boolean
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return DateTime
    else:
        return String(255)  # Default to String for other types

# Function to dynamically create a new table
def create_new_table(table_name, df):
    metadata = MetaData()
    
    # Define columns based on dataframe columns and inferred types
    columns = [Column('id', Integer, primary_key=True, autoincrement=True)]  # Add an id column as primary key
    for col in df.columns:
        col_type = infer_column_type(df[col].dtype)
        columns.append(Column(col, col_type))

    # Create the table dynamically
    new_table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)  # Create the table in the database
    return new_table

# Function to handle null values
def handle_null_values(df):
    # Identify numeric and non-numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64']).columns

    # Fill null values in numeric columns with mean
    for col in numeric_columns:
        mean_value = df[col].mean()
        df[col].fillna(round(mean_value, 2), inplace=True)

    # Remove rows with null values in non-numeric columns
    df.dropna(subset=non_numeric_columns, inplace=True)

    return df

@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # Check if the user has selected a file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Get the target table from the form data
    table_name_key = 'table_name'
    if table_name_key not in request.form:
        return jsonify({"error": "No target table specified"}), 400

    table_name_input = request.form[table_name_key].lower()
    
    # Determine the file type
    file_type = file.filename.split('.')[-1].lower()

    try:
        # Process the file based on its type
        if file_type == 'csv':
            df = pd.read_csv(file)
        elif file_type == 'json':
            df = pd.read_json(file)
        elif file_type == 'xml':
            data_dict = xmltodict.parse(file.read())
            df = pd.DataFrame(data_dict.get('root', {}).get('row', []))  # Modify 'root' and 'row' as per your XML structure
        else:
            return jsonify({'error': 'Unsupported file format'}), 400

        # Handle null values
        df = handle_null_values(df)

        # If the table doesn't exist in ALLOWED_TABLES, create it
        if table_name_input not in ALLOWED_TABLES:
            # Dynamically create the new table based on the data structure
            create_new_table(table_name_input, df)
            
            # Add the new table to the ALLOWED_TABLES dictionary for future use
            ALLOWED_TABLES[table_name_input] = table_name_input

        # Insert data into the specified or newly created table
        df.to_sql(table_name_input, engine, if_exists='append', index=False)

        return jsonify({'message': f'File uploaded and data inserted into {table_name_input} successfully'}), 200

    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific errors
        return jsonify({'error': f'Database error: {str(e)}'}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)
