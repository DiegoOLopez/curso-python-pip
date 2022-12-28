import matplotlib.pyplot as plt

def generateBarChart(labels, values, country):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{country}.png')
    plt.close()

def generatePieChart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig('chart_Pie_final_final_si.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 40, 8000]
    # generateBarChart(labels, values)
    generatePieChart(labels, values)