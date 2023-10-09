import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == "__main__":
  labels = ['Marketing', 'Technology', 'Humans Resourses']
  costs = [100, 240, 145]
  # generate_bar_chart(labels, costs)
  # generate_pie_chart(labels, costs)