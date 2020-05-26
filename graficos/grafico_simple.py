from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('grafico_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores a generar? '))

    x_vals = list(range(total_vals))
    y_vals = []

    for i in x_vals:
        val = int(input(f'Dame y para {i}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
