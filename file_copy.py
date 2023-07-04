# def split_tsv_file(input_file, output_file1, output_file2):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#     split_index = len(lines) // 2

#     # First half
#     with open(output_file1, 'w', encoding='utf-8') as file1:
#         file1.writelines(lines[:split_index])

#     # Second half
#     with open(output_file2, 'w', encoding='utf-8') as file2:
#         file2.writelines(lines[split_index:])


# # Usage example
# split_tsv_file('Fakeddit/all_train.tsv', 'output1.tsv', 'output2.tsv')



def split_tsv_file(input_file, output_file1, output_file2, output_file3):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    split_index1 = total_lines // 3
    split_index2 = split_index1 * 2

    # First third
    with open(output_file1, 'w', encoding='utf-8') as file1:
        file1.writelines(lines[:split_index1])

    # Second third
    with open(output_file2, 'w', encoding='utf-8') as file2:
        file2.writelines(lines[split_index1:split_index2])

    # Third third
    with open(output_file3, 'w', encoding='utf-8') as file3:
        file3.writelines(lines[split_index2:])


# Usage example
split_tsv_file('Fakeddit/all_train.tsv', 'train1.tsv', 'train2.tsv', 'train3.tsv')
