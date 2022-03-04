import re


def accuracy(data, cols):
    return (data[cols.index('TrueNegative')] + data[cols.index('TruePositive')]) / sum(data)


def precision(data, cols):
    return data[cols.index('TruePositive')] / (data[cols.index('TruePositive')] + data[cols.index('FalsePositive')])


def recall(data, cols):
    return data[cols.index('TruePositive')] / (data[cols.index('TruePositive')] + data[cols.index('FalseNegative')])


def f1(prec, rec):
    return 2 * (prec * rec)/(prec + rec)


def print_report(data, cols):
    with open('report.txt', 'w') as handler:
        for func, name in zip([accuracy, precision, recall], ['Accuracy', 'Precision', 'Recall']):
            output = f'{name}: {func(data, cols):.4f}'
            print(output)
            handler.write(f'{output}\n')
        output = f'F1: {f1(precision(data, cols), recall(data, cols)):.4f}'
        print(output)
        handler.write(output)


if __name__ == '__main__':
    with open(f'confusion_matrix_Tree.txt', 'r') as h:
        mat = h.read()
    out = re.findall('(\d+)', mat)
    out = [int(i) for i in out]
    print(out)
    names = ['TrueNegative', 'FalsePositive', 'FalseNegative', 'TruePositive']
    print_report(out, names)
