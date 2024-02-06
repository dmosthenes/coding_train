from perceptron import Perceptron
from training import Point
from visualise import Perceptron_Visualiser

def train_perceptron(p, points, visualiser):

    # Train perceptron on points
    for point in points:
        p.train(point.get_inputs(), point.get_label())
        visualiser.draw_line()
        visualiser.draw_point(point)
        visualiser.update_point_colour()
        visualiser.title()

    correct = 0
    for point in points:
        if p.predict(point.get_inputs()) == point.get_label():
            correct += 1

    visualiser.result(f"Correct = {correct}/{len(points)}")
    print(f"Correct = {correct}/{len(points)}")    

    visualiser.reset()

    return correct


def main():

    p = Perceptron()

    width, height = 1, 1

    correct = 0

    while correct < 100:

        # Create 100 points
        points = [Point(width, height) for x in range(100)]


        # Create visualiser
        animation = Perceptron_Visualiser(p, width, height)

        # Train perceptron
        # p.print_formula()
        correct = train_perceptron(p, points, animation)


if __name__ == "__main__":
    main()