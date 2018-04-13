from bokeh.plotting import figure, output_file, show, ColumnDataSource

# x is where the bar sits on the x-axis
# top is the top of the bar line

def make_characters_graph(characters):

    # output to static HTML file
    output_file("tests/lines.html")
    # create a new plot with a title and axis labels
    labels = ["Michael", "Jim", "Pam", "Dwight", "Ryan", "Andy", "Robert"]
    p = figure(title="The Office Positivity Analysis", x_axis_label='Characters', y_axis_label='Positivity', x_range=labels)

    x = 0.33
    for char in characters:
        p.vbar(x, width = 0.33, bottom = 0, top = characters[char].percent_pos, fill_color = "green")
        x += 0.33
        p.vbar(x, width = 0.33, bottom = 0, top = characters[char].percent_neg, fill_color = "red")
        x += 0.5
    show(p)

def make_seasons_graph(seasons):

    # output to static HTML file
    output_file("tests/lines.html")
    # create a new plot with a title and axis labels
    p = figure(title="The Office Positivity Analysis", x_axis_label='Seasons', y_axis_label='Positivity')


    pos_line = []
    neg_line = []
    total_line = []
    norm_line = []

    for season in seasons:
        pos_line.append(seasons[season].percent_pos)
        neg_line.append(seasons[season].percent_neg)
        total_line.append(seasons[season].word_total)
        norm_line.append(seasons[season].sentiment)

    p.line(range(0, len(seasons)), pos_line, line_color = "green")
    p.line(range(0, len(seasons)), neg_line, line_color = "red")
    # p.line(range(0, len(seasons)), total_line)
    p.line(range(0, len(seasons)), norm_line)

    show(p)

if __name__ == "__main__":

    # output to static HTML file
    output_file("tests/lines.html")
    # create a new plot with a title and axis labels
    p = figure(title="The Office Positivity Analysis", x_axis_label='Characters', y_axis_label='Positivity')

    p.line([1,2,3,4,5,6],[4,5,3,4,6,4])
    show(p)