# Description

A small program I wrote to help with my database homework.

First, you need to copy data to a txt file such as example.txt

Make sure that the first line is the table name, followed by columns, and at last, the values.

Each table is separated by an empty line.


For example, in example.txt:
```
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
```


Usage example:
```
python insert.py -f example.txt -c 2 3
```
The first table has 2 columns, the second table has 3

The query.sql it generates will be:
```
INSERT INTO table_name1 (`column1`, `column2`) 
VALUES ('row1_column1_data', 'row1_column2_data'),
('row2_column1_data', 'row2_column2_data');

INSERT INTO table_name2 (`column1`, `column2`, `column3`) 
VALUES ('row1_column1_data', 'row1_column2_data', 'row1_column3_data'),
('row2_column1_data', 'row2_column2_data', 'row2_column3_data'),
('row3_column1_data', 'row3_column2_data', 'row3_column3_data');
```
