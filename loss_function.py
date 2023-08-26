def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += ( y - (m*x + b)) ** 2
    total_error / float(len(points))
