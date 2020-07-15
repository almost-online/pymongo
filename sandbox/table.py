def draw_separator(num_column, column_width):
    print('-' * ((column_width + 1) * num_column + 1))


def draw_header(*args, num_column=0, column_width=0):
    """
    draw headers of table
    :param num_column:
    :param column_width:
    :param args: headers column
    :return: max width
    """
    # fin max length of the header's column
    column_width = column_width or int(max([len(i) for i in args]) / 2) * 2 + 2
    num_column = num_column or len(args)
    draw_separator(num_column, column_width)
    print(('|' + '{:^{width}}|' * num_column).format(*args, width=column_width))
    draw_separator(num_column, column_width)

    return num_column, column_width


def draw_row(table_row, num_column, column_width):
    table_row += [''] * (num_column - len(table_row))
    print(('|' + '{:^{width}}|' * num_column).format(*table_row, width=column_width))
    draw_separator(num_column, column_width)


def draw_table(headers, body):
    """
    Draw table with separate header and body
    Header are
    :param headers:
    :param body:
    :return:
    """
    columns, width = draw_header(*headers)
    for row in body:
        draw_row(row, columns, width)
