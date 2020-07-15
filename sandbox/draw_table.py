from sandbox.table import draw_table

data = {
    'header': ['asd', 'bla', 'test', 'aaaaaaaaa'],
    'body':
        [
            [10, 20, 30],
            ['', 50, 50, 50],
            ['', '', '----', '', 'extra column'],
            ['too long string', 'and', 'another', 'loooooooong string'],  # FIXME: add str cut
        ]
}


draw_table(data['header'], data['body'])
