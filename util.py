def quality_check(df):
    num_rows, num_columns = df.shape

    null_count = df.isnull().sum()
    columns_with_nulls = null_count[null_count > 0]
    
    # Summary
    print('DataFrame Quality Check Summary')
    print('-' * 40)
    print(f'Number of rows: {num_rows}')
    print(f'Number of columns: {num_columns}')
    print('-' * 40)
    if columns_with_nulls.empty:
        print('Null values: 0')
    else:
        print('Null values:')
        print(columns_with_nulls)
