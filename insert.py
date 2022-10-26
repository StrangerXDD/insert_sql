# Author: Tony


def insert_generator(table, num_of_columns):
    table_name = table[0].strip("'")
    columns = table[1 : num_of_columns + 1]
    columns = [column.replace("'", "`") for column in columns]
    all_data = table[num_of_columns + 1 :]

    size = len(all_data)
    datas_by_column = []
    split_i = num_of_columns
    start_i = 0
    end_i = 0

    for i in range(size):
        if i == split_i - 1:
            end_i = split_i
            datas_by_column.append(all_data[start_i:end_i])
            split_i += num_of_columns
            start_i = end_i
    # print(datas_by_column)
    query = f"INSERT INTO {table_name} ("
    query += (", ").join(columns)
    query += ") \nVALUES ("
    rows = []
    for row in datas_by_column:
        rows.append((", ").join(row))
    query += ("),\n(").join(rows)
    query += ");\n"

    return query


def write_query(tables, num_of_columns_list):
    query = ""
    start = 0
    for table in tables:
        query += insert_generator(table, num_of_columns_list[start])
        query += "\n"
        start += 1

    with open("query.sql", "w") as f:
        f.write(query)


def load_file(file):
    with open(file) as f:
        lines = f.readlines()

    if lines[-1] != "\n":
        lines.append("\n")
    # print(lines)
    tables = []

    start = 0
    for i, v in enumerate(lines):
        if v == "\n":
            newline_char = "\n"
            tables.append([f"'{line.strip(newline_char)}'" for line in lines[start:i]])
            start = i + 1
    return tables


def main():
    """
    A small program i wrote to help with my database homework

    First you need to copy data to a txt file such as data.txt
    Make sure that the first line is table name, followed by columns, at last the values.
    Each table is seperated with empty line

    For example in example.txt:
    table_name1
    column1
    column2
    row1_column1_data
    row1_column2_data
    row2_column1_data
    row2_column2_data

    table_name2
    column1
    column2
    column3
    row1_column1_data
    row1_column2_data
    row1_column3_data
    row2_column1_data
    row2_column2_data
    row2_column3_data
    row3_column1_data
    row3_column2_data
    row3_column3_data



    example:
    >python insert.py -f example.txt -c 2 3
    The first table has 2 column, second table has 3

    The sql it generate will be:

    INSERT INTO table_name1 (`column1`, `column2`) 
    VALUES ('row1_column1_data', 'row1_column2_data'),
    ('row2_column1_data', 'row2_column2_data');

    INSERT INTO table_name2 (`column1`, `column2`, `column3`) 
    VALUES ('row1_column1_data', 'row1_column2_data', 'row1_column3_data'),
    ('row2_column1_data', 'row2_column2_data', 'row2_column3_data'),
    ('row3_column1_data', 'row3_column2_data', 'row3_column3_data');
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="A program that generate sql insert script according to txt file."
    )

    parser.add_argument("-f", "--file", help="file path", required=True)
    parser.add_argument(
        "-c",
        "--columns_count",
        help="enter number of columns by table order in the txt file",
        required=True,
        nargs="*",
        type=int,
    )
    args = parser.parse_args()
    tables = load_file(args.file)
    write_query(tables, args.columns_count)


if __name__ == "__main__":
    main()
