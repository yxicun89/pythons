import csv
import sys
import numpy as np

def main():
    step=sys.argv[1]
    test_file = sys.argv[2]
    with open(test_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        test_data = [row for row in reader]
    
    headers = test_data[0]
    test_data = np.array(test_data[1:], dtype=object)

    if step == "step1":
        # test_data = np.array(test_data)
        columns = [test_data[:, i].tolist() for i in range(test_data.shape[1])]
        columns = columns[1:]
        columns = [
            [float(x) if x != '' else np.nan for x in row]
            for row in columns
            ]
        
        column_means = [np.nanmean(column) for column in columns]
        column_vars = [np.nanvar(column,ddof=1) for column in columns]
        column_mins = [np.nanmin(column) for column in columns]
        column_maxs = [np.nanmax(column) for column in columns]
        
        for i in [0,2,3,4]:
            print(column_means[i],column_vars[i],column_mins[i],column_maxs[i])
    
    elif step == "step2":
        columns = [test_data[:, i].tolist() for i in range(test_data.shape[1])]
        days = columns[0]
        columns = columns[1:]
        columns = [
            [float(x) if x != '' else np.nan for x in row]
            for row in columns
            ]
        column_means = [np.nanmean(col) for col in columns]
        column_mins = [np.nanmin(column) for column in columns]
        column_maxs = [np.nanmax(column) for column in columns]
        
        for i in [0,2,3,4]:  
            col = columns[i]
            mean = column_means[i]
            columns[i] = np.array([mean if np.isnan(float(x)) else float(x) for x in col])
        
        columns[1] = [float(1) if np.isnan(x) else x for x in columns[1]]
        for i in [2,3,4]:
            for j in range(len(columns[2])):
                columns[i][j] = (columns[i][j] - column_mins[i]) / (column_maxs[i] - column_mins[i])
        for i in range(len(days)):
            print(f"{days[i]},{columns[0][i]},{columns[1][i]},{columns[2][i]},{columns[3][i]},{columns[4][i]}")
    
    elif step == "step3":
        columns = [test_data[:, i].tolist() for i in range(test_data.shape[1])]
        days = columns[0]
        columns = columns[1:]
        columns = [
            [float(x) if x != '' else np.nan for x in row]
            for row in columns
            ]
        column_means = [np.nanmean(col) for col in columns]
        column_mins = [np.nanmin(column) for column in columns]
        column_maxs = [np.nanmax(column) for column in columns]
        
        for i in [0,2,3,4]:  
            col = columns[i]
            mean = column_means[i]
            columns[i] = np.array([mean if np.isnan(float(x)) else float(x) for x in col])
        
        columns[1] = [float(1) if np.isnan(x) else x for x in columns[1]]
        
        output_matrix = np.zeros((len(columns[1]), 4), dtype=float)

        for row_index, col_index in enumerate(columns[1]):
            output_matrix[int(row_index), int(col_index)] = 1
        
        output_matrix = [output_matrix[:, i].tolist() for i in range(output_matrix.shape[1])]
        

        # print(output_matrix)
        for 
        np.insert(columns, row_index, output_matrix, axis=0)
        
        # columns[1] = [output_matrix[:, i].tolist() for i in range(output_matrix.shape[1])]

        # print(columns)
        # or x != 0
        for i in [2,3,4]:
            for j in range(len(columns[2])):
                columns[i][j] = (columns[i][j] - column_mins[i]) / (column_maxs[i] - column_mins[i])


if __name__ == "__main__":
    main()